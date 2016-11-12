Question-并行成像：什么是并行成像？与常规成像有什么不同？
======================================================================================================================

:date: 2014-11-10
:tags: K-space & Rapid Imaging, Parallel Imaging
:slug: what-is-pi
:authors: Chunshan
:summary: 什么是并行成像

原文链接:\ `What is parallel imaging? How does this differ from "regular" imaging? <http://mriquestions.com/what-is-pi.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4277800_orig.png?304
    :alt: summary
    :align: center
    :width: 700

并行成像是广泛使用的技术，此技术使用已知放置位置和敏感度的接收线圈协助定位MR信号的空间位置。有了线圈的这些额外信息就可以在图像采集时减少相位编码步数，反过来，造成的潜在结果是成像时间成倍减少。

虽然特定的线圈数据如何转换为图像信息的细节有些复杂，但是并行成像的基本想法并没有这么复杂，实际上，并行成像的核心原理比频率编码和相位编码对大多数学生而言更容易掌握。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/2745685_orig.gif
   :alt: Principle underlying parallel imaging
   :align: right
   :width: 450

   并行成像基本原理：使用线圈敏感度信息辅助空间定位。

例如，使用一组围绕头部的4个接收线圈探测如左图中所示的一个像素产生的磁共振信号。因为每个线圈到此像素的距离不同，每个线圈记录的信号都不同，是其位置的函数（近的线圈信号强）。仅通过观察每个线圈信号的相对强度，就可以对MR信号的近似源位置进行粗略估计。即使不使用相位，频率或傅里叶变换，我们已经可以知道信号来自大脑左顶叶的某处！

在“常规”（非并行）成像中，也会使用多个表面线圈探测MR信号，但它们的单个输出组合成一个聚合的复杂信号，然后被数字化并被处理为最终的图像。相反，在并行成像中，来自单个线圈的信号被放大，数字化，并在各自的通道中同时（“并行”）处理，直到临近结束时仍保持它们的特性。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/791272_orig.jpg?385
   :alt: Massive parallel coil array
   :align: right
   :width: 600

   用于全身成像的并行线圈阵列（来自Siemens）

由于电子技术的进步显著降低了射频数字处理系统的成本，现代磁共振成像中并行成像已经成为现实。现在，磁共振厂商提供的商用系统能够支持2000+个线圈和128+个接收通道。

**参考材料** 
    * Blaimer M, Breuer F, Mueller M, Heidemann RM, Griswold MA, Jakob PM. `SMASH, SENSE, PILS, GRAPPA. How to choose the optimal method <http://mriquestions.com/uploads/3/4/5/7/34572113/blaimer_parallelreview.pdf>`_. Top Magn Reson Imaging 2004;15:223-236 [review]. 
    * Deshmane A, Gulani V, Griswold MA, Seiberlich N. `Parallel MR imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/deshane_pi_review.pdf>`_. J Magn Reson Imaging 2012;36:55-72. (review)
    * Glockner JF, Hu HH, Stanley DW, et al. `Parallel MR imaging: a user's guide <http://mriquestions.com/uploads/3/4/5/7/34572113/glockner_radiographics_parallel_imaging_users_guide.pdf>`_. Radiographics 2005;25:1279-1297.
    * Larkman DJ, Nunes RG. `Parallel magnetic resonance imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/parallel_imaging_2007_review.pdf>`_. Phys Med Biol 2007;52:R15-R55 [review]

**相关问题**
  * `How does the scanner know the locations of all the MR signals? <http://mriquestions.com/how-to-locate-signals.html>`_
  * `并行成像是一种特殊的脉冲序列么？可以在任何线圈任何方向上进行么？ <http://chunshan.github.io/MRI-QA/parallel-imaging/pi-coils-and-sequences.html>`_