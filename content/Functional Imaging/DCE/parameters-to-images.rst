Question-DCE参数与图像 -- 计算的DCE参数如何与我们在临床图像上看到的增强模式相联系？
========================================================================================

:date: 2015-10-30
:tags: Perfusion, DCE
:slug: parameters-to-images
:authors: Chunshan
:summary: 计算的DCE参数如何与我们在临床图像上看到的增强模式相联系？

原文链接:\ `How do calculated DCE parameters relate to patterns of enhancement we see on clinical images? <http://www.mri-q.com/parameters-to-images.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/534902_orig.png?338
    :alt: summary
    :align: center
    :width: 700

流行的Tofts模型包含与钆在组织中的药代动力学相关的四个参数。通过数学分析可以计算这些参数并且创建它们的解剖参数图。但是这些参数在实践中有何意义？它们与我们观察到的视觉上的动态增强图像有何关联？

+--------------------------------------------------------------------------+----------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/454033_orig.jpg | .. figure::  http://www.mri-q.com/uploads/3/2/7/4/3274160/4125760_orig.gif |
|    :alt: Gd-enhanced T1-image of malignant glioma                        |    :alt: Ktrans map                                                        |
|    :width: 400                                                           |    :width: 400                                                             |
|                                                                          |                                                                            |
|    钆增强的恶性胶质瘤T1加权像                                            |    Ktrans 参数图                                                           |
+--------------------------------------------------------------------------+----------------------------------------------------------------------------+

第一个也是最重要的一个DCE参数是Ktrans，钆在血浆和血管外细胞外间隙（EES）组织的体积转移常数。像化学反应速率，它的单位是1/time，如min-1,。简而言之，Ktrans反映的是钆从血浆流入EES所有过程的总和（主要是血流量和毛细血管渗透）。

Tofts模型中第二个独立的动力学参数是EES的体积分数，表示为Ve，正式定义是每单位体积组织中EES的体积，是一个介于0到1之间的无量纲的数字。Ve反映组织间质中聚集钆的可用空间的大小。

Tofts模型中的第三个参数是Kep，表示钆从EES返流回血管系统的时间常数。回想一下，Kep不是一个完全独立的参数，它被定义为前两者的比率（如Kep = Ktrans/Ve），所以Kep的增加反映的是Ktrans的增加或者Ve的减少，或者二者兼而有之。

扩展的Tofts模型中出现的第四个参数是Vp，血浆的体积分数。在许多病变中这个变量比较小而且无关紧要。然而在严重的血管肿瘤中，血管内对总信号的贡献会达到10%或更大，以至不能被忽略。

DCE参数Ktrans，Ve，kep，vp与不同组织的时间-信号强度（钆浓度）曲线的形态有直接联系。具体表现为，

  * Ktrans与时间-信号强度曲线的初始斜率（“wash-in”速率）相关
  * ve与时间-信号强度曲线的峰高和达峰时间（TTP）相关
  * kep控制曲线的形状，反映独立分量Ktrans和ve的相对贡献。
  * vp，如果比较小，对曲线的影响不大，但是如果vp比较大，导致时间-信号强度曲线更快速的上坡，更高更早的峰高，更快的造影剂流出，变得与动脉输入函数更为相似。

+---------------------------------------------------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3041172_orig.png | .. figure::  http://www.mri-q.com/uploads/3/2/7/4/3274160/4600917_orig.png?302 | .. figure::  http://www.mri-q.com/uploads/3/2/7/4/3274160/440331_orig.png |
|    :alt: With fixed ve, Ktrans correlates with initial up-slope           |    :alt: With fixed Ktrans, ve                                                 |    :alt: With fixed Ktrans, ve                                            |
|    :width: 300                                                            |    :width: 300                                                                 |    :width: 300                                                            |
|                                                                           |                                                                                |                                                                           |
|    固定ve，Ktrans与时间-信号强度曲线的初始上升斜率（“wash-in”速率）相关   |    固定Ktrans，ve与时间-信号强度曲线的峰高和达峰时间（TTP）相关                |    随着vp增大，时间-信号强度曲线变得与动脉输入函数更为相似                |
+---------------------------------------------------------------------------+--------------------------------------------------------------------------------+---------------------------------------------------------------------------+

**参考材料**
    * Ferrier MC, Sarin H, Fung SH, et al. `Validation of dynamic contrast-enhanced magnetic resonance imaging-derived vascular permeability measurements using quantitative autoradiography in the RG2 rat brain tumor model <http://www.mri-q.com/uploads/3/2/7/4/3274160/neoplasia_ktran_vs_ki_piis1476558607800790.pdf>`_. Neoplasia 2007; 9:546-555. (Good correlation between Ktrans and autoradiographically measured influx rate in a rat glioma model with high permeability).
    * Tofts PS. `Modeling tracer kinetics in dynamic Gd-DTPA MR imaging <http://www.mri-q.com/uploads/3/2/7/4/3274160/b103_tofts-modeling-jmri1997.pdf>`_. J Magn Reson Imaging 1997; 7:91-101.      
    * Tofts PS. `T1-weighted DCE imaging concepts: modelling, acquisition and analysis <http://www.mri-q.com/uploads/3/2/7/4/3274160/dce-mri_siemens.pdf>`_. MAGNETOM Flash 2010; 3:30-35. 

**相关问题**
	* `How do you evaluate the information obtained from a DCE imaging study? <http://www.mri-q.com/how-is-dce-analyzed.html>`_  