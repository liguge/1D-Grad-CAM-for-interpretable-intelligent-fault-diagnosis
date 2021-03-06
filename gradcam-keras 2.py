import numpy as np
import tensorflow as tf
import keras.backend as K
from keras.models import Model
from keras.layers.core import Lambda


def target_category_loss(x, category_index, nb_classes):
    return tf.multiply(x, K.one_hot([category_index], nb_classes))


def target_category_loss_output_shape(input_shape):
    return input_shape


def normalize(x):
    # utility function to normalize a tensor by its L2 norm
    return x / (K.sqrt(K.mean(K.square(x))) + 1e-5)


def resize_1d(array, shape):
    res = np.zeros(shape)
    if array.shape[0] >= shape:
        ratio = array.shape[0]/shape
        for i in range(array.shape[0]):
            res[int(i/ratio)] += array[i]*(1-(i/ratio-int(i/ratio)))
            if int(i/ratio) != shape-1:
                res[int(i/ratio)+1] += array[i]*(i/ratio-int(i/ratio))
            else:
                res[int(i/ratio)] += array[i]*(i/ratio-int(i/ratio))
        res = res[::-1]
        array = array[::-1]
        for i in range(array.shape[0]):
            res[int(i/ratio)] += array[i]*(1-(i/ratio-int(i/ratio)))
            if int(i/ratio) != shape-1:
                res[int(i/ratio)+1] += array[i]*(i/ratio-int(i/ratio))
            else:
                res[int(i/ratio)] += array[i]*(i/ratio-int(i/ratio))
        res = res[::-1]/(2*ratio)
        array = array[::-1]
    else:
        ratio = shape/array.shape[0]
        left = 0
        right = 1
        for i in range(shape):
            if left < int(i/ratio):
                left += 1
                right += 1
            if right > array.shape[0]-1:
                res[i] += array[left]
            else:
                res[i] += array[right] * \
                    (i - left * ratio)/ratio+array[left]*(right*ratio-i)/ratio
        res = res[::-1]
        array = array[::-1]
        left = 0
        right = 1
        for i in range(shape):
            if left < int(i/ratio):
                left += 1
                right += 1
            if right > array.shape[0]-1:
                res[i] += array[left]
            else:
                res[i] += array[right] * \
                    (i - left * ratio)/ratio+array[left]*(right*ratio-i)/ratio
        res = res[::-1]/2
        array = array[::-1]
    return res

def register_gradient():
    if "GuidedBackProp" not in ops._gradient_registry._registry:
        @ops.RegisterGradient("GuidedBackProp")
        def _GuidedBackProp(op, grad):
            dtype = op.inputs[0].dtype
            return grad * tf.cast(grad > 0., dtype) * \
                tf.cast(op.inputs[0] > 0., dtype)

def compile_saliency_function(model, activation_layer='block5_conv3'):
    input_img = model.input
    layer_dict = dict([(layer.name, layer) for layer in model.layers[1:]])
    layer_output = layer_dict[activation_layer].output
    max_output = K.max(layer_output, axis=3)
    saliency = K.gradients(K.sum(max_output), input_img)[0]
    return K.function([input_img, K.learning_phase()], [saliency])

def modify_backprop(model, name):
    g = tf.get_default_graph()
    with g.gradient_override_map({'Relu': name}):

        # get layers that have an activation
        layer_dict = [layer for layer in model.layers[1:]
                      if hasattr(layer, 'activation')]

        # replace relu activation
        for layer in layer_dict:
            if layer.activation == keras.activations.relu:
                layer.activation = tf.nn.relu

        # re-instanciate a new model
        new_model = VGG16(weights='imagenet')
    return new_model

def deprocess_image(x):
    '''
    Same normalization as in:
    https://github.com/fchollet/keras/blob/master/examples/conv_filter_visualization.py
    '''
    if np.ndim(x) > 3:
        x = np.squeeze(x)
    # normalize tensor: center on 0., ensure std is 0.1
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1

    # clip to [0, 1]
    x += 0.5
    x = np.clip(x, 0, 1)

    # convert to RGB array
    x *= 255
    if K.image_dim_ordering() == 'th':
        x = x.transpose((1, 2, 0))
    x = np.clip(x, 0, 255).astype('uint8')
    return x

def grad_cam(input_model, data, category_index, layer_name, nb_classes):
    #def target_layer(x):
        #return target_category_loss(x, category_index, nb_classes)
    target_layer = lambda x: target_category_loss(x, category_index, nb_classes)
    x = input_model.layers[-1].output
    x = Lambda(target_layer, output_shape=target_category_loss_output_shape)(x)
    model = Model(input_model.layers[0].input, x)
    loss = K.sum(model.layers[-1].output)
    conv_output = [l for l in model.layers if l.name is layer_name][0].output


    grads = normalize(K.gradients(loss, conv_output)[0])
    gradient_function = K.function(
        [model.layers[0].input], [conv_output, grads])
    output, grads_val = gradient_function([data])
    output, grads_val = output[0, :], grads_val[0, :, :]
    weights = np.mean(grads_val, axis=(0))

    cam = np.ones(output.shape[0: 1], dtype=np.float32)
    
       for i, w in enumerate(weights):
           cam += w * output[:, i]
    
    #
    # cam = cv2.resize(cam, (224, 224))
    # cam = np.maximum(cam, 0)
    # heatmap = cam / np.max(cam)
    #
    #
    #
    # # Return to BGR [0..255] from the preprocessed image  
    # image = image[0, :]
    # image -= np.min(image)
    # image = np.minimum(image, 255)
    #
    # cam = cv2.applyColorMap(np.uint8(255 * heatmap), cv2.COLORMAP_JET)
    # cam = np.float32(cam) + np.float32(image)
    # cam = 255 * cam / np.max(cam)


    # cam = np.ones(output.shape[0: 1], dtype=np.float32)
    # for i, w in enumerate(weights):
    #     cam += w * output[:, i]


    cam = output.dot(weights)
    print(cam.shape,'cam')
    # print(cam)
    cam = resize_1d(cam, (data.shape[1]))
    cam = np.maximum(cam, 0)
    # heatmap = cam / np.max(cam)
    print(cam.shape,'cam')
    heatmap = (cam - np.min(cam))/(np.max(cam) - np.min(cam)+1e-10)
    return heatmap
