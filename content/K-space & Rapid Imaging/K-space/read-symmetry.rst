Question-读出共轭对称：什么是读出共轭对称（部分回波）成像？为什么仅采样回波的一部分？
========================================================================================================

:date: 2014-10-21
:tags: K-space & Rapid Imaging, K-space (Advanced)
:slug: read-symmetry
:authors: Chunshan
:summary: 读出共轭对称

原文链接:\ `What is read-conjugate symmetry (fractional echo) imaging? Why would one only want to sample part of an echo? <http://mri-q.com/read-symmetry.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/7563983_orig.png?286
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8058679_orig.gif
   :alt: Read-conjugate symmetry
   :align: right
   :width: 400

读出共轭对称是部分傅里叶技术的一种，使用k空间的一半数据合成(预测)另一半数据。与相位共轭对称不同的是，其使用的对称方向是读出方向（频率编码方向）。

因为图示中的kx轴通常用于表示频率编码，读出对称性可以看做是获取k空间的右半部分，估计左半部分的数据。k空间采样的右半部分来自每一个MR回波的后面部分。

各厂商对此技术的命名也反映了每个回波只采样一部分。“部分回波（Partial Echo）”（GE, Philips）；“半回波（Half Echo）”（Hitachi）；“不对称回波（Asymmetric Echo）”（Siemens）。与相位共轭对称性不同，全部的相位编码步骤都需要采集，因此不会直接节省时间。

为什么仅想采样一个回波的一部分？答案是通过仅采样回波的一部分，回波时间（TE）可以短于其他情况下可能的最小值。这对于快速成像技术和平面回波技术特别有用，但也在许多其他的应用中使用如磁共振血管造影和T1加权的自旋回波成像。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/2396857_orig.gif
   :alt: Read-conjugate symmetry
   :align: left
   :width: 400

当回波时间（TE）比较短时，RF脉冲所产生的自由感应衰减（FID）信号会混入回波的早期信号，通过只采样每个回波的后半部分，并且使用读出共轭对称重建前半部分，我们可以使用短TE获取图像，并且FID和回波信号之间干扰小。

此外，对于给定的回波时间（TE），回波右半部分有充分时间进行采样，因此部分回波技术可产生更好的信噪比（SNR）。由于采样时间更远的地方梯度幅值更小，读出共轭对称技术也可用于给定回波时间时采集更小的FOV，或者斜扫，不使用此技术时是不可能的。最后，读出共轭对称的另一个优势是读出方向上梯度场施加时间减少，减少了频率编码方向上的血流和运动伪影。

**参考材料**
     * Feinberg DA, Hale JD, Watts JC et al. `Halving MR imaging time by conjugation: demonstration at 3.5 kG <http://mri-q.com/uploads/3/4/5/7/34572113/feinberg_conj_symm_radiology2e1612e22e3763926.pdf>`_.  Radiology 1986; 161:527-531.
     * MacFall JR, Pelc NJ, Vavrek RM. `Correction of spatially dependent phase shifts for partial Fourier imaging <http://mri-q.com/uploads/3/4/5/7/34572113/mcfall_partial_fourier539236.pdf>`_.  Magn Reson Imaging 1988; 6:143-145. 
     * McGibney G, Smith MR, Nichols ST, Crawley A. `Quantitative evaluation of several partial Fourier reconstruction algorithms used in MRI <http://mri-q.com/uploads/3/4/5/7/34572113/partial_fourier_methods_2010_pfi.pdf>`_. Magn Reson Med 1993;30:51-59

**相关问题**
	* `什么是部分傅里叶成像？ <http://chunshan.github.io/MRI-QA/k-space/partial-fourier.html>`_
	* `相位共轭对称如何工作？为什么会使用这种技术？ <http://chunshan.github.io/MRI-QA/k-space/phase-symmetry.html>`_	