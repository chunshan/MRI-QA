Question-共轭对称性：为什么读出共轭对称技术和相位共轭对称技术不结合使用？那样的话可以仅采集1/4的k空间数据，大大节省时间。
================================================================================================================================================

:date: 2014-10-22
:tags: K-space & Rapid Imaging, K-space (Advanced)
:slug: why-not-use-both
:authors: Chunshan
:summary: 共轭对称性

原文链接:\ `Why don't you combine the read conjugate symmetry and phase conjugate symmetry techniques? That way you really save time by collecting only 1/4 the k-space data. <http://mri-q.com/why-not-use-both.html>`_

**概要**
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/7563983_orig.png?286
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6818495_orig.gif?315
   :alt: conjugate symmetry
   :align: right
   :width: 500

   K空间“对角对称”的性质使得不能仅使用四分之一k空间数据重建图像

k空间对称性是读出共轭对称技术和相位共轭对称技术赖以成功的基础，这种对称性本质上是成对角的。仅采集k空间一个角上的数据可以估计/合成关于原点对称的另一个角上的数据（其它的数据不能合成），因此读出共轭对称技术和相位共轭对称技术不能一起使用，四分之一k空间不足以准确地重建整幅图像。

|
|
|
|
|
|

**参考材料**
     * McGibney G, Smith MR, Nichols ST, Crawley A. `Quantitative evaluation of several partial Fourier reconstruction algorithms used in MRI <http://mri-q.com/uploads/3/4/5/7/34572113/partial_fourier_methods_2010_pfi.pdf>`_. Magn Reson Med 1993;30:51-59
     * Williams LR. `Symmetry <http://mri-q.com/uploads/3/4/5/7/34572113/symmetry.pdf>`_. Lecture Notes for Computer Science 530, University of New Mexico, 2011. Available at `http://www.cs.unm.edu/~williams/cs530/symmetry.pdf <http://www.cs.unm.edu/~williams/cs530/symmetry.pdf>`_     

**相关问题**
	* `什么是部分傅里叶成像？ <http://chunshan.github.io/MRI-QA/k-space/partial-fourier.html>`_
	* `相位共轭对称如何工作？为什么会使用这种技术？ <http://chunshan.github.io/MRI-QA/k-space/phase-symmetry.html>`_	