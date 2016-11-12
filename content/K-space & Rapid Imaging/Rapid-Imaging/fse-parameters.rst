Question-FSE参数：你如何选择快速自选回波的成像参数？有几个新参数需要设置。
======================================================================================================================

:date: 2014-10-26
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: fse-parameters
:authors: Chunshan
:summary: 如何选择快速自选回波的成像参数

原文链接:\ `How do you select parameters for fast spin echo imaging? There are several new ones to set. <http://www.mri-q.com/fse-parameters.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/2432613_orig.png?307
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/3316708_orig.gif
   :alt: fse
   :align: center
   :width: 800

传统自旋回波成像（Conventional Spin-Echo，CSE）中，仅需指定两个基本的时间参数，重复时间（TR）和回波时间（TE）。在快速自选回波（Fast/Turbo Spin-Echo，FSE/TSE）成像中，简单TE被有效回波时间（TEeff）代替，有效回波时间是填充k空间中中心线的时间。因此需要两个额外的新参数：
* 回波数量 -- GE和Toshiba称之为回波链长度（ETL），Siemens和Philips称之为Turbo因子，Hitachi称为Shot因子；
* 回波之间的时间 -- GE，Philips，Siemens和Toshiba称为Echo Spacing（ESP），Hitachi称之为Inter Echo Time（ITE）。

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/6809133_orig.jpg?360
   :alt: Increased T2 weighting with increasing ETL
   :align: left
   :width: 500

   随着ETL增加T2权重增加。所有图像TR=4000并且其它参数一致。

回波链长度（ETL，Echo Train Length）是最重要的一个参数。一般来说，图像采集时间与ETL成反比。换句话说，固定TR/TE/空间分辨率，如果一个传统自旋回波序列采集时间需要8分钟，ETL=8的快速自选回波序列只需要1分钟。

ETL还对图像质量有重要影响，ETL越长，T2加权效应越明显，因为TE越长，会有更多后期的回波对整体信号产生贡献。

ETL越长还会导致整体信噪比（SNR，Signal-to-Noise Ratio）和对比度噪声比（CNR，Contrast-to-Noise Ratio）下降，因为后期的回波较弱。

TE非常长的情况下，后期产生的回波会带来更多的空间模糊。空间模糊效应来自于晚期回波上T2相关的信号损失。这些回波是在高阶相位编码情况下采集的，高阶相位编码对应于图像中的高空间频率和细节。

给定TR间隔内采集覆盖一个解剖区域所需的层数也是ETL选择时需考虑的一个因素。回忆一下传统的二维傅里叶变换（2D FT）自旋回波成像中，每一个TR间隔末期的“死时间”并没有浪费，在多层采集中，这段时间被用于激发其它片层（如果需要温习一下，可以看一下 `之前的Q&A <http://www.mri-q.com/simultaneous-slices.html>`_）。FSE成像中，对于一个给定的TR，需要权衡ETL和能够采集的片层数。如果ETL太大，可能需要两次单独的FSE采集（双倍的成像时间）才能包含所需的层数。

增加回波间隔（ESP，Echo Spacing）使得TE更长，但是给SNR和CNR带来不利的影响，运动，磁敏感性和边缘相关的伪影增加。一般来说，增加ESP主要是给图像质量带来有害的后果，在大多数应用中应该选择所允许的最短的ESP。

如果将FSE的图像对比度与传统的自旋回波技术相类比，可以使用期望的TE值，将传统自旋回波在低阶相位编码采集的数据聚合在一起。这种对比是行得通的，因为图像的全局对比度主要是由k空间中心处低阶相位编码采集的信号决定（高阶相位编码步骤主要对边缘有贡献）。因此，尽管回波链中的每个回波用不同的TE采集，有效TE（决定图像整体对比度）是由进行低阶相位编码时的TE决定，一般选择在回波链的中间，但是在特殊的应用中也会往前移或者往后移。

**参考材料** 
     * Constable RT, Smith RC, Gore JC. `Signal-to-noise and contrast in fast spin echo (FSE) and inversion recovery FSE imaging <http://www.mri-q.com/uploads/3/4/5/7/34572113/signal_to_noise_and_contrast_in_fast_spin_echo.8.pdf>`_. J Comput Assist Tomogr 1992; 16:41-47. 
     * Li T, Mirowitz SA. `Fast T2-weighted MR imaging: impact of variation in pulse sequence parameters on image quality and artifacts <http://www.mri-q.com/uploads/3/4/5/7/34572113/li_effect_of_parameters_in_fse.pdf>`_. Mag Reson Imaging 2003;21:745-753. 
     * Sze G, Kawamura Y, Negishi C, et al. `Fast spin-echo MR imaging of the cervical spine: influence of echo train length and echo spacing on image contrast and quality <http://www.mri-q.com/uploads/3/4/5/7/34572113/sze_fse_spine.pdf>`_. AJNR Am J Neuroradiol 1993; 14:1203-13.


**相关问题**
	* `什么是快速自旋回波成像？ <http://chunshan.github.io/MRI-QA/rapid-imaging/what-is-fsetse.html>`_