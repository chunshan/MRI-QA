Question-k空间的不同部分：为什么k空间在中间有个大的亮斑？
========================================================================================

:date: 2014-10-09
:tags: K-space & Rapid Imaging, K-space (Basic)
:slug: big-spot-in-middle
:authors: Chunshan
:summary: k空间的不同部分

原文链接:\ `Why does k-space have a big spot in the middle? <http://mriquestions.com/big-spot-in-middle.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/2579366_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_7316167_orig.gif
   :alt: 2D and 3D pictures of k-space
   :align: right
   :width: 300

   k空间的2D和3D视图

k空间的正中间是kx = ky = 0的点，这个位置对应于图像傅里叶表示中的常数项，它的幅值等于图像的平均亮度。此中心点有比k空间中其他任何点更高的幅值，在3D表示中可以看得更明显（右图）。

k空间中心区域最亮，原因有二。首先，中心行（ky = 0）在没有相位编码梯度的情况下（因此没有相位编码步骤中破坏性的干扰波）采集，其次，k空间的中心列(kx = 0)与MR回波的峰值重叠。

这些特征说明如下，比较了k空间中心行(左)和外周(右)行的MR信号。

+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4678104_orig.jpg     | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/7099771_orig.jpg      |
|    :alt: MR signal from a line near the center of k-space                         |    :alt: MR signal from a line through periphery of k-space                        |
|    :width: 400                                                                    |    :width: 400                                                                     |
|                                                                                   |                                                                                    |
|    k空间接近中心行的MR信号幅值高                                                  |    k空间外周行的MR信号幅值低                                                       |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

**参考材料**
     * Mezrich R. `A perspective on k-space <http://mriquestions.com/uploads/3/4/5/7/34572113/fourier.kspace.mezrich.1995.pdf>`_. Radiology 1995; 195: 297-315. [review].

**相关问题**
	* `从哪儿获得数据填充k空间？ <http://chunshan.github.io/MRI-QA/k-space/data-for-k-space.html>`_