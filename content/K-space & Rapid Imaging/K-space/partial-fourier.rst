Question-部分傅里叶技术：什么是部分傅里叶成像？
========================================================================================

:date: 2014-10-19
:tags: K-space & Rapid Imaging, K-space (Advanced)
:slug: partial-fourier
:authors: Chunshan
:summary: 部分傅里叶成像

原文链接:\ `What is partial Fourier imaging? <http://mri-q.com/partial-fourier.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/2100257_orig.png?270
    :alt: summary
    :align: center
    :width: 700

部分傅里叶成像技术是仅使用一半k空间数据产生完整MR图像的重建方法。怎样才能做到？

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3449851_orig.jpg
   :alt: Conjugate symmetry of k-space
   :align: right
   :width: 400

   P和Q的共轭对称性。如果已知其中一个点的值，另一个可以计算出来

这个有些惊奇的结果来源于这样一个事实，k空间中的一些信息是多余的。假设在数据采集过程中没有相位错误发生，k空间具有独特的镜像属性称为共轭（Hermitian）对称性。

一对点如P和Q的共轭对称性指的是它们关于k空间原点对称，如果P点的值为复数[a+bi]，那么Q点的值就是P点的共轭复数，[a-bi]。

对任何实数函数进行傅里叶变换，结果都有共轭对称性，这是一个高级但直接的结论。对于2D MR成像这个更具体的例子，共轭对称点代表两个相反相位编码步骤获得的回波中相呼应的两个上升和下降点。换句话说，一个使用正相位编码步骤获得的回波上升部分数据点的信号强度是另一个使用对应的负相位编码步骤获得的回波下降部分数据点信号强度的共轭复数。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/2172345_orig.gif?541
   :alt: Conjugate (Hermitian) symmetry of k-space.
   :align: center
   :width: 800

   k空间的共轭（Hermitian）对称性。k空间关于原点对称的镜像位置，实部相同但是虚部符号相反

理论上，共轭对称性造成的结果是只需采集k空间一半儿的数据，另一半儿可以计算出来。这可以减少成像时间，减少最小回波时间，或者两者同时减少。

所有图像数据集都会包含一些相位错误，因此使用共轭对称性进行近似并不完美。相位错误的根源包含那些常见的“嫌疑人”：B0不均匀性，磁敏感效应，涡电流，生理运动，射频不均匀性造成的空间变化或表面线圈敏感性。所以部分傅里叶技术的商业实现需要比k空间的一半儿稍微多采集一些（通常常规成像的60%，平面回波成像比例会更高）。这些多余的线用于产生k空间的相位校正图，可以对缺失的值进行更准确的预测。

日常使用中有两种类型的部分傅里叶成像技术，并且在多数主流扫描仪中都提供了这两种方法，这两种方法通常分别称为“读出共轭对称（read conjugate symmetry）”和“相位共轭对称（phase conjugate symmetry）”，后面两个Q&A分别详述这两个技术。

**高级讨论**

目前用于部分傅里叶估计的流行方法是零差重建。这个技术需对已获取的k空间数据使用两个串行的滤波器。第一个滤波器（高通滤波）将数据的幅值翻倍，然后丢弃傅里叶变换后的图像的虚部。第二个零差滤波器（低通滤波）根据已获取数据的一小部分，利用关于k空间中心的对称性创建一幅“校正图像”。在丢弃图像的虚部之前，从图像经过第一个滤波器（高通）的相位中减去“校正图像”的相位。

在平面回波成像（EPI）中，射频激发脉冲晚期获得的回波与早期获得的回波有不同的相位。这是相位误差额外的来源，使得相位估计更加困难。对EPI而言，部分傅里叶技术通常需采样k空间的6/8或7/8，才能准确估计剩余的部分。

**参考材料**
     * Feinberg DA, Hale JD, Watts JC et al. `Halving MR imaging time by conjugation: demonstration at 3.5 kG <http://mri-q.com/uploads/3/4/5/7/34572113/feinberg_conj_symm_radiology2e1612e22e3763926.pdf>`_.  Radiology 1986; 161:527-531.
     * MacFall JR, Pelc NJ, Vavrek RM. `Correction of spatially dependent phase shifts for partial Fourier imaging <http://mri-q.com/uploads/3/4/5/7/34572113/mcfall_partial_fourier539236.pdf>`_.  Magn Reson Imaging 1988; 6:143-145. 
     * McGibney G, Smith MR, Nichols ST, Crawley A. `Quantitative evaluation of several partial Fourier reconstruction algorithms used in MRI <http://mri-q.com/uploads/3/4/5/7/34572113/partial_fourier_methods_2010_pfi.pdf>`_. Magn Reson Med 1993;30:51-59
     * Williams LR. `Symmetry <http://mri-q.com/uploads/3/4/5/7/34572113/symmetry.pdf>`_. Lecture Notes for Computer Science 530, University of New Mexico, 2011. Available at `http://www.cs.unm.edu/~williams/cs530/symmetry.pdf <http://www.cs.unm.edu/~williams/cs530/symmetry.pdf>`_

**相关问题**
	* `相位共轭对称如何工作？为什么会使用这种技术？ <http://chunshan.github.io/MRI-QA/k-space/phase-symmetry.html>`_
	* `什么是读出共轭对称（部分回波）成像？为什么仅采样回波的一部分？ <http://chunshan.github.io/MRI-QA/k-space/read-symmetry.html>`_