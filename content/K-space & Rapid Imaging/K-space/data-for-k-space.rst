Question-填充k空间：从哪儿获得数据填充k空间？
========================================================================================

:date: 2014-10-06
:tags: K-space & Rapid Imaging, K-space (Basic)
:slug: data-for-k-space
:authors: Chunshan
:summary: 从哪儿获得数据填充k空间？

原文链接:\ `Where do you get the data to fill k-space? <http://mriquestions.com/data-for-k-space.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/2419962_orig.png
    :alt: summary
    :align: center
    :width: 700

填充k空间的数据直接来自磁共振信号。由于使用梯度进行相位和频率编码，磁共振信号已经类似傅里叶格式，适合填充k空间矩阵。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_7316167_orig.gif
   :alt: Representation of the MR signal in terms of real and imaginary components.
   :align: right
   :width: 400

   用实部和虚部表示的磁共振信号

在\ `前面一个Q&A <http://www.mri-q.com/real-v-imaginary.html>`_\ 中，我们解释了磁共振信号如何用正交的方式检测。每一个数字化的磁共振信号数据点可以表示为一个复数，有实部和虚部。另外，也可以为每个数据点定义一个幅值和相位，通过简单的三角关系计算。

填充k空间的数据直接取自磁共振信号但是可以以任意的顺序获取。过去30年中，填充k空间的主流方法是逐线填充的笛卡尔方法。现在，螺旋和径向填充轨迹越来越流行。

在笛卡尔方法中，每一个数字化回波完整地填充k空间的一行。回波信号用正交的方式记录，所以k空间上每一个点包含了实部和虚部。k空间中每一行左边的值在回波产生的早期采集，右边的值随后采集。回波的中心（最大的值）发生在k空间每一行的中心附近。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5154143_orig.gif?543
   :alt: Cartesian (line-by-line) filling of k-space
   :align: center
   :width: 700

   笛卡尔方法（逐线）填充k空间

在2D傅里叶变换成像中，k空间中每一行对应于应用一个相位编码梯度采集得到的回波数据。按照惯例，定义接近k空间中心的行与低阶相位编码步骤相关联，靠近顶部和底部的行与高阶相位编码步骤相关联。由于回波幅度在低阶相位编码步骤中更大（有较少的梯度引起的失相位），因此k空间中的值在中心处比较大。

**参考材料**
     * Mezrich R. `A perspective on k-space <http://mriquestions.com/uploads/3/4/5/7/34572113/fourier.kspace.mezrich.1995.pdf>`_. Radiology 1995; 195: 297-315. [review].
     * Miller K. `MRI image formation (ppt) <http://mriquestions.com/uploads/3/4/5/7/34572113/miler-image_formation.ppt>`_. On-line lecture notes available at `users.fmrib.ox.ac.uk/~karla/teaching/image_formation.ppt <http://users.fmrib.ox.ac.uk/~karla/teaching/image_formation.ppt>`_

**相关问题**
	* `k空间是什么？ <http://chunshan.github.io/MRI-QA/k-space/what-is-k-space.html>`_
	* `我不明白你如何将数字化磁共振信号简单地直接插入到k空间中。这些点和空间频率是一致的么？ <http://chunshan.github.io/MRI-QA//k-space/why-signal-harr-k-space.html>`_