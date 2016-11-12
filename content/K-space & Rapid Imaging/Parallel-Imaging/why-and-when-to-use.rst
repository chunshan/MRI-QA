Question-使用并行成像：任何情况下都应该使用并行成像进行加速么？
======================================================================================================================

:date: 2014-11-13
:tags: K-space & Rapid Imaging, Parallel Imaging
:slug: why-and-when-to-use
:authors: Chunshan
:summary: 任何情况下都应该使用并行成像进行加速么？

原文链接:\ `Should parallel imaging acceleration be used in every case? <http://mriquestions.com/why-and-when-to-use.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4595421_orig.png?268
    :alt: summary
    :align: center
    :width: 700

大多数现代磁共振系统建立在并行架构上，包含一个体发射线圈和一组局部接收线圈，可以接入并行通道进行信号放大和处理。当以并行成像（PI，Parallel Imaging）模式操作时，关于线圈位置和敏感性的信息就会用于减少相位编码步数加速成像。并行成像的加速因子可以用R量化表示，这个数字通常在2和6之间。

是否要使用并行成像进行加速取决于一个特定检查所需的空间和时间分辨率，进行此检查的场强和感兴趣的部位。

并行成像主要的优势可以简单列举为：

1. 图像采集时间的显著减少。这与加速因子（R）成反比，如R = 2，图像采集时间减半，节省下来的时间就是金钱（时间=美元/欧元），可以用于扫描额外的序列，或者在原来成像时间中获得更高的空间分辨率或时间分辨率。
2. 减少磁敏感伪影。使用并行采集和重建过程可以减少磁共振信号中相位相关的失真。这在平面回波成像中是特别有利的。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1821014_orig.png?503
   :alt: Reduced susceptibility distortions seen on these single-shot DW images using PI
   :align: center
   :width: 700

   在使用并行成像的弥散加权图像中可以看到磁敏感导致的失真变小

尽管有这些好处，也必须考虑并行成像的限制：

1. 信噪比（SNR，singal-to-noise）的减少。即使没有运动，所有的并行成像技术都会导致信噪比的显著降低，如果R = 2，图像信噪比减少√2，也就是40%。这个缺点在高场（高场时其本身的信噪比更高）和某些解剖区域（如相对对称并且均匀的大脑）通常不是问题。
2. 并行成像特有的伪影增加。因为并行成像取决于线圈敏感度或它们协调贡献的估计，额外图像处理相关的伪影总是会出现，并且非均匀地分布。这样的重建错误随着加速因子（R）增大而增加，但是随着线圈单元数量的增加而减少。

+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5715386_orig.jpg?290 | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6051950_orig.jpg?292  |
|    :alt: No acceleration (R=1)                                                    |    :alt: With acceleration (R=4) showing artifacts                                 |
|    :width: 400                                                                    |    :width: 400                                                                     |
|                                                                                   |                                                                                    |
|    没有加速（R=1）                                                                |    加速时（R=4）出现伪影                                                           |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

那么，什么时候应该选择并行成像加速，什么时候不应该？

没有明确“正确”或“错误”的答案，总体而言，需要根据成像时间和图像质量不断进行尝试才能做出最终的决定。如果不使用并行成像时时间仍可接受，并且能够获得所需的体素分辨率和空间覆盖，那么最好不要用并行成像技术。在我们中心，神经和肌肉骨骼成像一般不使用并行成像，但是胸部和腹部成像广泛使用并行成像，而且3T比1.5T时并行成像更常用。随着技术和线圈的不断发展，我们期待并行成像在所有领域的使用都会增加。

**参考材料** 
    * Deshmane A, Gulani V, Griswold MA, Seiberlich N. `Parallel MR imaging <http://www.mri-q.com/uploads/3/4/5/7/34572113/deshane_pi_review.pdf>`_. J Magn Reson Imaging 2012;36:55-72. (review)
    * Glockner JF, Hu HH, Stanley DW, et al. `Parallel MR imaging: a user's guide <http://www.mri-q.com/uploads/3/4/5/7/34572113/glockner_radiographics_parallel_imaging_users_guide.pdf>`_. Radiographics 2005;25:1279-1297.
    * Larkman DJ, Nunes RG. `Parallel magnetic resonance imaging <http://www.mri-q.com/uploads/3/4/5/7/34572113/parallel_imaging_2007_review.pdf>`_. Phys Med Biol 2007;52:R15-R55 [review]

**相关问题**
  * `什么是并行成像？与常规成像有什么不同？ <http://mriquestions.com/how-to-locate-signals.html>`_