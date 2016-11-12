Question-并行成像中的伪影：并行成像中有什么特别的伪影么？
=================================================================================================================

:date: 2014-11-19
:tags: K-space & Rapid Imaging, Parallel Imaging
:slug: artifacts-in-pi
:authors: Chunshan
:summary: 并行成像中的伪影

原文链接:\ `Are there any artifacts specific to parallel imaging? <http://mriquestions.com/artifacts-in-pi.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/3989357_orig.png
    :alt: summary
    :align: center
    :width: 700

导致“常规”MR成像伪影的因素也同样会影响并行成像（PI），如噪声，运动，混叠，化学位移，吉布斯（Gibbs），磁敏感，射频干扰等。但是这些伪影在并行成像中可能看起来会略有差异因为它们受并行成像复杂重建过程的影响，包括线圈敏感性映射的产生，阈值化/蒙版，多项式拟合，和空间谐波或图像展开权重因子的估计。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9279128_orig.jpg?268
   :alt: The SENSE Ghost
   :align: right
   :width: 400

   SENSE鬼影

混叠（Aliasing）是公认的造成所有类型磁共振成像中伪影的原因。当采样频率不足信号最高频率的2倍时就会发生混叠，在非并行磁共振成像中混叠伪影通常表现为解剖结构的“卷折”，特别在频率编码方向。标准的混叠伪影及其补救措施在\ `后续的Q&A <http://mriquestions.com/aliasing.html>`_\ 中有详细的描述。

SENSE鬼影是在重建FOV（field-of-view）比成像物体小时发生的一种特殊类型的混叠伪影，SENSE鬼影是一种折叠伪影，出现在图像相位编码方向的中间（有时在边缘）。

SENSE算法须在执行展开步骤前考虑减小FOV后每个像素的所有贡献。如果FOV非常小，这等同于忽略成像物体FOV外部对信号的贡献，造成对成像像素的污染，SENSE算法不能打开这个额外的卷折。被排除的外围组织的鬼影沿重建图像等间距地重复出现，间距等于单个线圈数据减小的FOV。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1271440_orig.jpg
   :alt: Motion occurring between calibration phase and imaging in SENSE
   :align: right
   :width: 450

   SENSE中运动可能发生在校正阶段和成像阶段之间。

SENSE类型的并行成像序列中的运动伪影可能发生在校正扫描和图像采集开始之间的时间，由此产生的伪影在相位编码方向看起来像一组重复的边缘，图像的其他部分则没有什么异常。重复的边缘来自图像最明亮的部分，一般是皮下的脂肪，其信号在校正扫描中非常强。如果这种现象造成问题，解决方法是在训练患者和对成像部位采取更好的保护措施后重新进行校准扫描和成像序列。自校正并行成像序列（如mSENSE）也会消除这种特殊类型的运动伪影。

|
|
|

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5475630_orig.jpg?268
   :alt: Noise in PI is often non-uniformly distributed
   :align: left
   :width: 350

   并行成像中的噪声通常分布并不均匀。

并行成像中的噪声与使用更高的加速因子（R）直接相关。并行成像噪声的特有之处在于其在图像上的分布并不均匀，而是取决于有空间依赖性的参数称为几何因子（g）。这个现象可以在膝盖图像中得到很好的展示（左），噪声频带被投影在图像的前部和后部，中间部分却没有。这种非均匀的噪声分布在SENSE/ASSET中比在GRAPPA/ARC方法中更常见。

有几种方法可以用于减小并行成像中残留的混叠伪影和噪声。可以对校正步骤进行调整，如SENSE方法中重复进行线圈敏感性映射，GRAPPA方法中采集更多的ACS线。如果可能的话，还可以将有最多线圈元素的方向设置为相位编码轴。

减小加速因子R也会有帮助，尽管这样会增加成像时间。如果使用3D扫描，在相位编码和层面（分区）编码方向都进行加速通常会更好。例如，假设想要整体的加速因子为R=4，最好分解为在两个方向加速因子分别为R=2，好过在一个方向上R=4。先进的并行成像采集技术如CAIPIRINHA通过减少彼此混叠的像素数目也会提高图像质量。

**参考材料** 
    * Breuer F. `Artifacts and pitfalls in parallel imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/artifacts_in_parallel_imaging.pdf>`_. European Society for Magnetic Resonance in Medicine and Biology (ESMRMB) Teaching Session, Leipzig, 6 Oct 2011.
    * Goldfarb JW. `The SENSE ghost: field-of-view restrictions for SENSE imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/20204_ftp.pdf>`_. J Magn Reson Imaging 2004; 20:1046-1051.
    * Yanasak NE, Kelly MJ. `MR imaging artifacts and parallel imaging techniques with calibration scanning: a new twist on old problems <http://mriquestions.com/uploads/3/4/5/7/34572113/rg2e342135051_-_pi_artifacts.pdf>`_. Radiographics 2014; 34:532-548.

**相关问题**
  * `为什么并行成像的检查看起来噪声如此大？ <http://chunshan.github.io/MRI-QA/parallel-imaging/noise-in-pi.html>`_
  * `CAIPIRINHA是什么？难道不是一种饮料么？ <http://chunshan.github.io/MRI-QA/parallel-imaging/caipirinha.html>`_