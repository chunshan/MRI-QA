Question-并行成像的线圈和序列：并行成像是一种特殊的脉冲序列么？可以在任何线圈任何方向上进行么？
======================================================================================================================

:date: 2014-11-12
:tags: K-space & Rapid Imaging, Parallel Imaging
:slug: pi-coils-and-sequences
:authors: Chunshan
:summary: 并行成像的线圈和序列

原文链接:\ `Is PI a special type of pulse sequence? Can it be performed with any coil in any direction? <http://mriquestions.com/pi-coils-and-sequences.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5640189_orig.png
    :alt: summary
    :align: center
    :width: 700

两个问题的答案都是No。

并行成像（PI，Parallel Imaging）不是一种脉冲序列，而是一种\ **图像重建技术**。实际上任何一种脉冲序列（SE, GRE, DWI, IR, MRA等）都可以将并行成像作为一种选择。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/3486687_orig.jpg?276
   :alt: PI is performed in the S-I direction for spinal imaging
   :align: right
   :width: 400

   对脊柱成像而言，并行成像在S-I方向进行。

并行成像利用两个或多个接收线圈在空间和/或频率敏感性上的不同，每个线圈的输出都可以被独立地记录，数字化和处理。通常情况下，接收器线圈阵列使用4,8,16,32,64甚至更多的线圈。因此，并行成像不会是仅有一对正交输出通道的表面线圈，头线圈，膝盖线圈或大型的体线圈。

可进行并行成像的方向取决于线圈阵列的排列方向，具体而言，这些线圈沿并行成像的方向必须有不同的敏感性曲线。

对脊柱成像而言，接收线圈通常沿脊柱中轴以线性的方式排列，从头到尾骨。从上到下（S-I）的线圈敏感性差异最大，这是用于并行成像标准的方向。

下面的插图显示了两个可能的头接收线圈配置。左边所有的线圈在从上到下（S-I）的方向都有相似的敏感性曲线，但从左到右（L-R）和从前到后（A-P）敏感性曲线有显著差异。因此并行成像可在L-R方向或A-P方向进行，但不能在S-I方向进行。右边的多元线圈阵列则没有此限制。

+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/3320635_orig.jpg | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9980972_orig.jpg         |
|    :alt: PI is possible in the L-R or A-P directions only                     |    :alt: PI possible in all three directions                                          |
|    :width: 400                                                                |    :width: 400                                                                        |
|                                                                               |                                                                                       |
|    并行成像可能仅在L-R或A-P方向进行                                           |    并行成像也可能在所有方向进行                                                       |
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

**参考材料** 
    * Deshmane A, Gulani V, Griswold MA, Seiberlich N. `Parallel MR imaging <http://www.mri-q.com/uploads/3/4/5/7/34572113/deshane_pi_review.pdf>`_. J Magn Reson Imaging 2012;36:55-72. (review)
    * Glockner JF, Hu HH, Stanley DW, et al. `Parallel MR imaging: a user's guide <http://www.mri-q.com/uploads/3/4/5/7/34572113/glockner_radiographics_parallel_imaging_users_guide.pdf>`_. Radiographics 2005;25:1279-1297.

**相关问题**
  * `什么是并行成像？与常规成像有什么不同？ <http://chunshan.github.io/MRI-QA/parallel-imaging/what-is-pi.html>`_