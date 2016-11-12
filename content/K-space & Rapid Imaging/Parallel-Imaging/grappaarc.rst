Question-GRAPPA/ARC：GRAPPA/ARC的原理是什么？
=================================================================================================================

:date: 2014-11-16
:tags: K-space & Rapid Imaging, Parallel Imaging
:slug: grappaarc
:authors: Chunshan
:summary: GRAPPA/ARC的原理

原文链接:\ `How does GRAPPA/ARC work? <http://mriquestions.com/grappaarc.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/36019_orig.png
    :alt: summary
    :align: center
    :width: 700

GRAPPA (GeneRalized Autocalibrating Partial Parallel Acquisition) 和 ARC (Autocalibrating Reconstruction for Cartesian imaging)都是多线圈并行成像技术。像其他的并行成像技术（如SENSE/ASSET）一样，GRAPPA/ARC仅采样数量有限的相位编码步骤。相位欠采样大大减少成像时间但是导致信号混叠，必须展开。SENSE/ASSET中，线圈敏感性用于在傅里叶变换后的图像域区分这些信号，而GRAPPA/ARC则是在傅里叶变换前的k空间中进行校正。可以说：

**SENSE/ASSET方法是先重建，然后校正**

**GRAPPA/ARC方法是先校正，然后重建**

下表说明了GRAPPA/ARC过程中四个主要的步骤：

1. 数据采集。对采集的MR信号进行数字化，解调，填充每个线圈的k空间矩阵。因为跳过了多个相位编码步骤，许多k空间中的线会丢失。然而穿过k空间中心的线是全采样的，构成自动校准信号（ACS）区域。这些额外的ACS线就是在图像采集过程中完成的（因此术语为“自校准”）。
2. 估计缺失的线。ACS中得到的已知数据用于计算每个线圈的权重因子。这些权重因子反应了每个线圈在全FOV的k空间数据中如何扭曲，变形和空间频率错置。估计k空间中缺失的点采用迭代方式，使用全局权重因子结合每个小区域（称为块或核）的局部已知数据。需要指出的是，使用所有线圈的权重因子和已知数据估计一个线圈的缺失数据。
3. 生成单个线圈的图像。将k空间中缺失的线填充后，进行傅里叶变换得到每个线圈的单张图像。与SENSE/ASSET中的线圈图像不同，GRAPPA/ARC得到的图像是没有混叠的。
4. 组合。最终对单个线圈的图像进行平方和运算得到最终的幅度图像。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4062968_orig.png?681
   :alt: GRAPPA/ARC
   :align: center
   :width: 700

   GRAPPA/ARC重建过程概览。注意：相位编码方向为水平轴。

GRAPPA/ARC中的关键步骤是估计缺失的点，这个步骤中有很多可能的变量，包括重建核的大小和使用参数的数目。GRAPPA和ARC主要的不同是后者使用3D的核，将所有三个方向邻域的源数据考虑进去计算缺失的数据。ARC中的估计过程也有一点不同，使得3D数据计算是可控的。

+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5088091_orig.jpg?527 | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9781580_orig.jpeg    |
|    :alt: GRAPPA/ARC                                                               |    :alt: GRAPPA/ARC                                                               |
|    :height: 450                                                                   |    :height: 450                                                                   |
|                                                                                   |                                                                                   |
+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+

GRAPPA/ARC中估计k空间中缺失的线。此处的相位编码沿垂直轴。

**高级讨论**

除了标准的产品，GE还提供了在“Turbo Mode”下使用ARC的选择，可使扫描速度再提高一倍。TurboARC调整数据采样模式，在k空间外围采集更少的数据点。数据的填充模式（中心圆vs中心椭圆）可能也会调整。

**参考材料** 
    * Blaimer M, Breuer F, Mueller M, Heidemann RM, Griswold MA, Jakob PM. `SMASH, SENSE, PILS, GRAPPA. How to choose the optimal method <http://mriquestions.com/uploads/3/4/5/7/34572113/blaimer_parallelreview.pdf>`_. Top Magn Reson Imaging 2004;15:223-236 [review]. 
    * Brau A. `New parallel imaging method enhances imaging speed and accuracy <http://mriquestions.com/uploads/3/4/5/7/34572113/arc_ge.pdf>`_. GE Signa Pulse, 2007; 36-38. (Promotional piece describing GE's ARC method).    
    * Brau ACS, Beatty P, Skare S, Bammer R. `Comparison of reconstruction accuracy and efficiency among autocalibrating data-driven parallel imaging methods <http://mriquestions.com/uploads/3/4/5/7/34572113/brau_comparison_of_ccdd_methodsnihms-388017.pdf>`_. Magn Reson Med 2008; 59:382-395
    * Deshmane A, Gulani V, Griswold MA, Seiberlich N. `Parallel MR imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/deshane_pi_review.pdf>`_. J Magn Reson Imaging 2012;36:55-72. (review)
    * Griswold MA, Jakob PM, Heidemann RM, et al. `Generalized autocalibrating partially parallel acquisitions (GRAPPA) <http://mriquestions.com/uploads/3/4/5/7/34572113/griswold-grappa.pdf>`_. Magn Reson Med 2002; 47:1202-1210

**相关问题**
  * `我们的扫描仪中并行成像有两种不同的选择SENSE和GRAPPA。它们的原理是什么？应该选择哪一个？ <http://chunshan.github.io/MRI-QA/parallel-imaging/two-types-of-pi.html>`_