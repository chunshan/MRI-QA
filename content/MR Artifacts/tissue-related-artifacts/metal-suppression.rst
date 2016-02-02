Question-金属伪影抑制：我们最近为一个扫描仪买了金属伪影抑制软件。它的工作原理是什么？
======================================================================================================

:date: 2015-11-27
:tags: MR Artifacts, tissue related artifacts
:slug: metal-suppression
:authors: Chunshan
:summary: 金属伪影抑制

原文链接:\ `We recently purchased a metal artifact reduction software for one of our scanners. How does that work? <http://www.mri-q.com/metal-suppression.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/9770165_orig.png?301
    :alt: summary
    :align: center
    :width: 700

金属具有很高的内在磁化率(χ)，会产生显著的局部磁场扰动，使得共振频率在成像平面内和垂直成像平面方向都会发生变化。金属通过改变共振频率，使得图像像素偏移它们原来真实的位置，导致显著地几何变形，包括信号缺如（黑色区域）和信号累积（明亮区域）。存在几种最小化金属相关伪影的方法。

减少金属相关伪影重要的第一步是使用尽可能低强度的磁场。磁敏感性伪影与磁场强度成正比，因此对全髋关节置换术的患者，要想获得更好的扫描，首先选择更老的1.5T扫描仪而非崭新的3.0T机器。

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/2951317_orig.jpg?166
   :alt: Bounce Point occurs in magnitude-reconstructed IR images at intermediate time (TI)
   :align: right
   :width: 200

   金属伪影抑制技术

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/3560143_orig.jpg?173
   :alt: Metallic susceptibility artifacts in spine from pedicle screws
   :align: right
   :width: 200

   脊柱中由锥弓根螺钉导致的金属磁敏感伪影

即使没有购买专业软件，明智地使用标准技术也可以用来减少金属伪影。首先，应该使用回波间隔短的快速自旋回波序列，因为多个很短时间内施加的180°重聚脉冲可以部分校正由于磁场不均匀性导致的相散。接收器带宽也应提高到一个尽可能大的值使得与可接受的信噪比水平一致。减少层厚和使用并行成像加速也有助于降低金属伪影。

在承认失败前，对感兴趣区域至少从3个不同的平面成像或许值得一试。我在很多情况下惊奇地发现，金属伪影会使两个平面上的图像完全不可解释，第三个平面上却基本上不受伪影的影响，能够用来诊断。这需要不断尝试，在紧要关头却能够帮你一把。

主要的磁共振厂商还提供专门设计的软件减少金属伪影，有时一般称为MARS（Metal Artifact Reduction Sequences）。有几种方法可以实现这一目标。

**减少平面内的扭曲：视角倾斜（View Angle Tilting， VAT）**

自从1980年代的发展，VAT已经是普遍使用而且行之有效的减少由于磁敏感效应导致的平面内图像失真的技术。这种方法中，在信号读出时沿切片选择方向施加一个额外的梯度（VAT）。这个梯度造成成像像素的“错切”，一种看起来像从一个小角度观察成像层面的效应。因为VAT梯度场幅值与射频激发时的梯度场相同，它会恢复射频带宽内所有激发的自旋，完全取消局部的失共振效应。VAT方法理论上能够完全补偿读出方向上平面内像素的位移。

尽管可以充分校正平面内失真，VAT方法会因为几何层面错切和额外VAT梯度场造成的低通滤波效应造成图像模糊。这些效应可以通过使用更薄的片层，更高的矩阵分辨率和更高的带宽减少。

**减少平面间扭曲：SEMAC和MAVRIC**

由金属引起的平面间（片层与片层之间）的磁场扭曲更难校正。已经有两种密切相关的技术用于达到此目标：SEMAC（Slice Encoding Magnetic Artifact Compensation）和MAVRIC (Multi-Acquisition Variable Resonance Image Combination)。

SEMAC技术基于2D快速自旋回波序列，每一个片层在第三维上有额外的相位编码。在离散频率偏移上获得的重叠容积上的额外相位编码提供了金属磁敏感效应如何扭曲原来片层轮廓的信息。重建软件从而可以校正垂直于成像平面的信号平移。

MAVRIC是GE的产品，基于3D快速自旋回波序列，采用专有的频率选择性激发和多谱式VAT读出。这种方法也包括去模糊的后处理算法去除成像平面重建的伪影。

**参考材料**
     * Cho Z, Kim D, Kim Y. `Total inhomogeneity correction including chemical shifts and susceptibility by view angle tilting <http://www.mri-q.com/uploads/3/4/5/7/34572113/cho_vat.pdf>`_. Med Phys 1988; 15:7–11.     
     * Hargreaves BA, Worters PW, Pauly KB et al. `Metal-induced artifacts in MRI <http://www.mri-q.com/uploads/3/4/5/7/34572113/hargreaves_metal_artifacts_ajr_2011.pdf>`_. AJR Am J Roentenol 2011; 197:547-555. (A recent excellent review of metal artifacts and suppression techniques).
     * Koch KM, Lorbiecki JE, Hinks RS, King KF. A multispectral three-dimensional acquisition technique for imaging near metal implants. Magn Reson Med 2009; 61:381–390.
     * Lu W, Pauly KB, Gold GE, Pauly JM, Hargreaves BA. SEMAC: slice encoding for metal artifact correction in MRI. Magn Reson Med 2009; 62:66–76.
     * Olsen RV, Munk PL, Lee MJ et al. `Metal artifact reduction sequence: early clinical applications <http://www.mri-q.com/uploads/3/4/5/7/34572113/olsen_mars_radiographics2e202e32eg00ma10699.pdf>`_. Radiographics 2000; 20:699-712.

**相关问题**
	* `什么是磁敏感性伪影（susceptibility artifacts）? <http://chunshan.github.io/MRI-QA/tissue-related-artifacts/susceptibility-artifact.html>`_