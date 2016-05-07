Question-相位共轭对称：相位共轭对称如何工作？为什么会使用这种技术？
========================================================================================

:date: 2014-10-20
:tags: K-space & Rapid Imaging, K-space (Advanced)
:slug: phase-symmetry
:authors: Chunshan
:summary: 相位共轭对称

原文链接:\ `How does phase-conjugate symmetry work? Why is it used? <http://mri-q.com/phase-symmetry.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6773554_orig.png?291
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4906970_orig.gif?222
   :alt: Phase-conjugate symmetry
   :align: right
   :width: 400

   相位共轭对称。通过减少相位编码步骤，仅采样大约k空间的一半即可，合成或重建k空间的另一半

相位共轭对称技术使用k空间的上半部分来估计k空间的下半部分。在二维自旋卷折成像中，ky方向通常是相位编码方向的同义词，因此，“相位共轭对称”是描述这种从顶部到底部数据合成（估计）的通用术语。

理论上，相位共轭对称可以仅采集正常相位编码步骤的一半数据，从而成像时间可以最多减少至50%。实际上，节省的时间接近40%，但这个收益仍然是相当可观的，在现代磁共振成像协议中被广泛使用。

相位共轭对称方法，不同的厂商有不同的商标名字。Siemens称之为“半傅里叶（Half Fourier）”，Toshiba使用简称AFI“非对称傅里叶成像（Asymmetric Fourier Imaging）”，Philips和Hitachi则称他们的序列为“半扫描（Half Scan）”。

GE一直称他们的技术为“1/2-NEX”，“3/4-NEX”或“部分NEX（Fractional NEX）”，取决于k空间数据获取:估计的比例。“1/2-NEX”有些误导，因为减半的是相位编码总的步数（Np），而不是每个步骤中激发（NEX）的次数。但GE的这个叫法提醒我们k空间欠采样的程度与成像时间的减少是相关的。

虽然相位共轭对称技术减少了成像时间的同时保持了空间分辨率，但这是以牺牲信噪比（SNR）为代价的。对半傅里叶成像而言，SNR比对应的使用全相位编码步骤的序列减少了约30%（√½）。

**参考材料**
     * Feinberg DA, Hale JD, Watts JC et al. `Halving MR imaging time by conjugation: demonstration at 3.5 kG <http://mri-q.com/uploads/3/4/5/7/34572113/feinberg_conj_symm_radiology2e1612e22e3763926.pdf>`_.  Radiology 1986; 161:527-531.
     * MacFall JR, Pelc NJ, Vavrek RM. `Correction of spatially dependent phase shifts for partial Fourier imaging <http://mri-q.com/uploads/3/4/5/7/34572113/mcfall_partial_fourier539236.pdf>`_.  Magn Reson Imaging 1988; 6:143-145. 
     * McGibney G, Smith MR, Nichols ST, Crawley A. `Quantitative evaluation of several partial Fourier reconstruction algorithms used in MRI <http://mri-q.com/uploads/3/4/5/7/34572113/partial_fourier_methods_2010_pfi.pdf>`_. Magn Reson Med 1993;30:51-59

**相关问题**
	* `什么是部分傅里叶成像？ <http://chunshan.github.io/MRI-QA/k-space/partial-fourier.html>`_