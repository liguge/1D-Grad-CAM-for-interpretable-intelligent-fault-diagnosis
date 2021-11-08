# Grad-CAM-1D-pytorch
故障诊断（fault diagnosis）  
参考了https://github.com/agis09/grad_cam_1d/blob/master/grad_cam.py

不过我感觉最后他求平均的时候有些错误，应该是axis=1，进行求平均。。


这个模型直接输入一维振动信号就可以了。


如果这个项目帮助到你 欢迎cite：


@article{ZHANG2022110242,  
title = {Fault diagnosis for small samples based on attention mechanism},  
journal = {Measurement},  
volume = {187},  
pages = {110242},  
year = {2022},  
issn = {0263-2241},  
doi = {https://doi.org/10.1016/j.measurement.2021.110242},  
url = {https://www.sciencedirect.com/science/article/pii/S0263224121011507},  
author = {Xin Zhang and Chao He and Yanping Lu and Biao Chen and Le Zhu and Li Zhang}  
}
@ARTICLE{9374403,  
author={Luo, Hao and He, Chao and Zhou, Jianing and Zhang, Li},  
journal={IEEE Access},   
title={Rolling Bearing Sub-Health Recognition via Extreme Learning Machine Based on Deep Belief Network Optimized by Improved Fireworks},   
year={2021},  
volume={9},  
number={},  
pages={42013-42026},  
doi={10.1109/ACCESS.2021.3064962}}
