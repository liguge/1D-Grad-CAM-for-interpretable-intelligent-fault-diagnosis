# Grad-CAM-1D-pytorch     (Pytorch)(Keras)
故障诊断（fault diagnosis） 

This is the 1D-Grad-CAM implementation of pytorch version of  [Fault diagnosis for small samples based on attention mechanism
](https://www.sciencedirect.com/science/article/pii/S0263224121011507)


**However, in fact, the title [Fault diagnosis for small samples based on interpretable improved space-channel attention mechanism and improved regularization algorithms](https://doi.org/10.1016/j.measurement.2021.110242) fits the research content of the paper better.**


Maybe you need a software called [OriginLab](https://www.originlab.com/) to visualize the class activation gradient **or** [Matlibplot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html#sphx-glr-gallery-lines-bars-and-markers-multicolored-line-py).
# This model can input one-dimensional vibration signals directly.
# Everyone can refer to 1D-Grad-CAM++(Recommendation!), and later we have made a lot of modifications compared to 1D-Grad-CAM.

# If it is helpful for your research, please kindly cite this work:

```html
@article{ZHANG2022110242,  
title = {Fault diagnosis for small samples based on attention mechanism},  
journal = {Measurement},  
volume = {187},  
pages = {110242},  
year = {2022},  
issn = {0263-2241},  
doi = {https://doi.org/10.1016/j.measurement.2021.110242 },  
url = {https://www.sciencedirect.com/science/article/pii/S0263224121011507},  
author = {Xin Zhang and Chao He and Yanping Lu and Biao Chen and Le Zhu and Li Zhang}  
} 
```
# Algorithm
![image](https://user-images.githubusercontent.com/19371493/144694363-5e376c50-85fd-4a8f-b87c-b87199051439.png)



# Effect

![微信图片_20220404222733](https://user-images.githubusercontent.com/19371493/161565766-3689b89d-b447-4194-83ad-8796f9152f77.jpg)

![微信截图_20220509131105](https://user-images.githubusercontent.com/19371493/167344823-5d43a907-4370-4a4e-a364-da4da8477733.png)

# Note
If you need drawing code procedure in python, you can send an e-mail to **22110435 # bjtu.edu.cn ( please replace # by @ )** by **school e-mail**, I will send it to you by e-mail.

# Reference

https://github.com/agis09/grad_cam_1d/blob/master/grad_cam.py

https://github.com/jacobgil/pytorch-grad-cam


```html
@inproceedings{selvaraju2017grad,
  title={Grad-cam: Visual explanations from deep networks via gradient-based localization},
  author={Selvaraju, Ramprasaath R and Cogswell, Michael and Das, Abhishek and Vedantam, Ramakrishna and Parikh, Devi and Batra, Dhruv},
  booktitle={Proceedings of the IEEE international conference on computer vision},
  pages={618--626},
  year={2017}
}
```
```html
@inproceedings{chattopadhay2018grad,
  title={Grad-cam++: Generalized gradient-based visual explanations for deep convolutional networks},
  author={Chattopadhay, Aditya and Sarkar, Anirban and Howlader, Prantik and Balasubramanian, Vineeth N},
  booktitle={2018 IEEE winter conference on applications of computer vision (WACV)},
  pages={839--847},
  year={2018},
  organization={IEEE}
}
```
# Environment

pytorch == 1.10.0  
python ==  3.8  
cuda ==  10.2   

# Contact
- Chao He
- chaohe#bjtu.edu.cn   (please replace # by @)

## Views
![](http://profile-counter.glitch.me/liguge/count.svg)
