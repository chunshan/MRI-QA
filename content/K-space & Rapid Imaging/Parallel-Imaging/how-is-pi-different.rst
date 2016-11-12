Question-并行成像（PI）-进一步的不同：并行成像（PI）难道不就是使用多个接收线圈的“常规”MRI么？
======================================================================================================================

:date: 2014-11-11
:tags: K-space & Rapid Imaging, Parallel Imaging
:slug: how-is-pi-different
:authors: Chunshan
:summary: 并行成像（PI）进一步的不同

原文链接:\ `Isn't parallel imaging (PI) just "regular" MRI using multiple receiver coils? <http://mriquestions.com/how-is-pi-different.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5441047_orig.png?273
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/7115208_orig.jpg
   :alt: surface coil imaging
   :align: right
   :width: 550

并行成像和“常规”磁共振成像都会使用多个接收线圈，这一点上是相同的，但处理信息的方式完全不同。考虑如下两个接收线圈（#1 and #2）放置在头两侧的简单情况，正如预期的一样，从每个表面线圈接收到的信号在靠近线圈处最强，并随距离减弱。   

在“常规”磁共振成像中，我们将结合来自每个表面线圈的数据产生全视野（full field-of-view）大脑的组合图像。这种安排会比只使用一个大的头线圈增加信噪比和空间分辨率，但不会提高成像速度。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/3748180_orig.png?483
   :alt: parallel imaging
   :align: left
   :width: 550

   并行成像中相位编码太少会导致卷折伪影，大脑左侧（b）卷折到右侧（a），反之亦然。此处相位编码方向是从左到右。

为了缩短并行成像的时间，需要减少相位编码步骤的数目。要使分辨率不变而成像时间减半，需仅能采集k空间行数的一半。但是这种策略导致采集到的空间频率不能充分表示要成像的物体。在重建的图像上视野减小并且出现“卷折”伪影。

使用单个表面线圈（#1 和 #2）采集到的数据也会出现卷折和视野减小，常规图像重建（如在“常规”MRI所做的）由于对伪影未进行校正会导致许多重叠的边缘和阴影。并行成像中最基础的问题是如何使用线圈本身的信息“展开”卷折的数据。

在频域中也存在等效的问题，如何估计k空间中缺失的行从而避免卷折伪影。

已经开发了两种基本策略用于校正并行成像中的重叠伪影。第一种方法（SENSE，ASSET）中，从单个线圈重建图像，然后在图像/空间域进行校正。第二种方法（GRAPPA，ARC）是在频率域进行操作，也就是在k空间中校正然后进行重建。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9488066_orig.jpg
   :alt: unfolding problems
   :align: center
   :width: 700

后续的Q&A中会介绍两种技术的细节。

**参考材料** 
    * Deshmane A, Gulani V, Griswold MA, Seiberlich N. `Parallel MR imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/deshane_pi_review.pdf>`_. J Magn Reson Imaging 2012;36:55-72. (review)
    * Glockner JF, Hu HH, Stanley DW, et al. `Parallel MR imaging: a user's guide <http://mriquestions.com/uploads/3/4/5/7/34572113/glockner_radiographics_parallel_imaging_users_guide.pdf>`_. Radiographics 2005;25:1279-1297.
    * Larkman DJ, Nunes RG. `Parallel magnetic resonance imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/parallel_imaging_2007_review.pdf>`_. Phys Med Biol 2007;52:R15-R55 [review]

**相关问题**
  * `我们的扫描仪中并行成像有两种不同的选择SENSE和GRAPPA。它们的原理是什么？应该选择哪一个？ <http://chunshan.github.io/MRI-QA/parallel-imaging/two-types-of-pi.html>`_