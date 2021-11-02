# Grad-CAM-1D-pytorch

参考了https://github.com/agis09/grad_cam_1d/blob/master/grad_cam.py

不过我感觉最后他求平均的时候有些错误，应该是axis=1，进行求平均。。


这个模型直接输入一维振动信号就可以了。


如果这个项目帮助到你 欢迎cite


@article{ZHANG2022110242,
title = {Fault diagnosis for small samples based on attention mechanism},
journal = {Measurement},
volume = {187},
pages = {110242},
year = {2022},
issn = {0263-2241},
doi = {https://doi.org/10.1016/j.measurement.2021.110242},
url = {https://www.sciencedirect.com/science/article/pii/S0263224121011507},
author = {Xin Zhang and Chao He and Yanping Lu and Biao Chen and Le Zhu and Li Zhang},
keywords = {Convolutional neural network, Bidirectional gated recurrent unit, Attention mechanism, Rolling bearings, Small samples, Fault diagnosis},
abstract = {Aiming at the application of deep learning in fault diagnosis, mechanical rotating equipment components are prone to failure under complex working environment, and the industrial big data suffers from limited labeled samples, different working conditions and noises. In order to explore the problems above, a small sample fault diagnosis method is proposed based on dual path convolution with attention mechanism (DCA) and Bidirectional Gated Recurrent Unit (DCA-BiGRU), whose performance can be effectively mined by the latest regularization training strategies. BiGRU is utilized to realize spatiotemporal feature fusion, where vibration signal fused features with attention weight are extracted by DCA. Besides, global average pooling (GAP) is applied to dimension reduction and fault diagnosis. It is indicated that DCA-BiGRU has exceptional capacities of generalization and robustness by experiments, and can effectively carry out diagnosis under various complicated situations.}
}
