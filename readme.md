# Grad-CAM-1D-pytorch     (Pytorch)(Keras)
故障诊断（fault diagnosis） 

This is the 1D-Grad-CAM implementation of pytorch version of  [Fault diagnosis for small samples based on attention mechanism
](https://www.sciencedirect.com/science/article/pii/S0263224121011507)


However, in fact, the title [Fault diagnosis for small samples based on interpretable improved space-channel attention mechanism and improved regularization algorithms](https://doi.org/10.1016/j.measurement.2021.110242) fits the research content of the paper better.


Maybe you need a software called [OriginLab](https://www.originlab.com/) to visualize the class activation gradient **or** [Matlibplot](https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html#sphx-glr-gallery-lines-bars-and-markers-multicolored-line-py).

# Everyone can refer to 1D-Grad-CAM++(recommendation), and later we have made a lot of modifications compared to 1D-Grad-CAM.

# If this project helps you, welcome to cite it:

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
![image](https://user-images.githubusercontent.com/19371493/144694363-5e376c50-85fd-4a8f-b87c-b87199051439.png)



# Effect

![微信图片_20220404222733](https://user-images.githubusercontent.com/19371493/161565766-3689b89d-b447-4194-83ad-8796f9152f77.jpg)

![微信截图_20220509131105](https://user-images.githubusercontent.com/19371493/167344823-5d43a907-4370-4a4e-a364-da4da8477733.png)

# Reference

https://github.com/agis09/grad_cam_1d/blob/master/grad_cam.py

https://github.com/jacobgil/pytorch-grad-cam


This model can input one-dimensional vibration signals directly.




 
   
# Others works
```html
@ARTICLE{9374403,  
author={Luo, Hao and He, Chao and Zhou, Jianing and Zhang, Li},  
journal={IEEE Access},   
title={Rolling Bearing Sub-Health Recognition via Extreme Learning Machine Based on Deep Belief Network Optimized by Improved Fireworks},   
year={2021},  
volume={9},  
number={},  
pages={42013-42026},  
doi={10.1109/ACCESS.2021.3064962},  
url = {https://ieeexplore.ieee.org/document/9374403},  
}
```

# Environment

pytorch 1.10.0  
python 3.8  
cuda 10.2  
