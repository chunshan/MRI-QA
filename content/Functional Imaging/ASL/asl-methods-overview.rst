Question-ASL方法概述 - 您能解释一下各种ASL方法的不同之处么？哪一种最好？
=======================================================================================

:date: 2015-11-03
:tags: Perfusion, ASL
:slug: asl-methods-overview
:authors: Chunshan
:summary: 各种ASL方法的不同之处

原文链接:\ `Can you briefly explain the difference between the various ASL methods? Which is the best? <http://www.mri-q.com/asl-methods-overview.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/7127732_orig.png?323
    :alt: summary
    :align: center
    :width: 700

所有动脉自旋标记（ASL）脉冲序列由两部分组成：1）准备模块，用于磁性标记血流；2）读出模块，产生目标组织成对的“控制像”和“标记像”。ASL方法可以根据上述两个模块如何构建进行分类。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/7060963_orig.png?328
   :alt: Classification of ASL techniques  
   :width: 600 

   ASL技术的分类

最早的ASL技术使用连续射频发射结合施加于血流方向的梯度磁场反转流动的自旋质子，称为连续动脉自旋标记（Continuous Arterial Spin Labeling，CASL）。这些序列在商用扫描仪上很难实用，因为会让组织显著发热。到20世纪90年代末， CASL方法基本上被抛弃，脉冲发射的方法受到青睐。统称为脉冲动脉自旋标记（Pulsed Arterial Spin Labeling， PASL）。PASL技术可进一步分为相对于成像平面不对称地标记（EPISTAR，PICORE）和相对于成像平面对称地标记（FAIR）。最近一种混合形式的ASL被开发出来，伪连续动脉自旋标记（pseudo-Continuous Arterial Spin Labeling）使用一系列短的射频脉冲和强大的切片选择梯度。pCASL结合了CASL（高信噪比）和PASL（低能量沉积）的优点。现在大多数市售的ASL产品基于pCASL或者PASL的变种。

最早的ASL方法中，读出（成像）模块只能为使用平面-梯度回波技术获得的单个平面，随后多平面成像技术也被开发出来。使用快速自旋回波和快速梯度回波成像的方法也随后诞生，而且多平面2D和3D采集方法都可采用。

*2D图像采集* 对头动不是那么敏感，用于血流定量的话，可能比3D采集更好。为了获得最佳的图像质量，推荐进行预扫描和场映射。2D采集方法的缺点是远端切片比近端切片有更长的标记延迟，由于驰豫效应的影响导致信号层与层之间不同。

*3D图像采集* 比2D图像采集所需时间稍长，但是更容易实现。3D采集方式有更高的信噪比和更高的空间分辨率，而且不同层之间的标记延迟是固定的。目前3D采集技术不能与fMRI研究兼容，因为不能获得短时间间隔内的灌注变化。3D图像采集时一般也会进行背景抑制，但是背景抑制会降低灌注信号，并且可能混淆绝对血流量的计算。

主要ASL序列的技术细节和更完整的描述在接下来的几个Q&A中。

**高级讨论**

第四种ASL方法称为速度选择性动脉自旋标记（Velocity-Selective Arterial Spin Labeling，VSASL），目前仍主要限于研究中心。与其它的ASL方法不同，VSASL基于血流速度标记血液，而不是空间位置。破碎梯度用于饱和比选定截止速度流动更快的自旋，因此允许标记更慢的血流。由于标签不是空间选择性的，VSASL比其他的ASL方法对长时间的传输延迟更不敏感。VSASL的缺点是SNR比较低，选择合适的截止速度也比较困难。

**参考材料**
    * Borogovac A, Asllani I. `Arterial spin labeling (ASL) fMRI: advantages, theoretical constrains and experimental challenges in neurosciences <http://www.mri-q.com/uploads/3/2/7/4/3274160/asl_technical_review_818456.pdf>`_. Int J Biomed Imaging 2012; Article ID 818456:1-13. 
    * Diebler AR, Pollock JM, Kraft RA, et al. `Arterial spin-labeling in routine clinical practice, Part 1: techniques and artifacts <http://www.mri-q.com/uploads/3/2/7/4/3274160/deibler_asl1.pdf>`_. AJNR Am J Neuroradiol 2008; 29:1228-1234.
    * Essig M, Shiroishi MS, Nguyen TB, et al. `Perfusion MRI: the five most frequently asked technical questions <http://www.mri-q.com/uploads/3/2/7/4/3274160/essig_5_questions_ajr2e122e9543.pdf>`_. AJR Am J Roentgenol 2013; 200:24-34.
    * Ferré J-C, Bannier E, Raoult H, et al. `Arterial spin labeling (ASL) perfusion: techniques and clinical use <http://www.mri-q.com/uploads/3/2/7/4/3274160/asl_review_1156841300209x_1-s2.0-s221156841300209x-main.pdf>`_. Diagn Interv Radiol 2013; 94:1211-1223
    * Jahng G-H, Li K-L, Ostergaard l, Calamante F. `Perfusion magnetic resonance imaging: a comprehensive update on principles and techniques <http://www.mri-q.com/uploads/3/2/7/4/3274160/perfusion_review_article_kjr-15-554.pdf>`_. Korean J Radiol 2014; 15:554-577. (good recent review).
    * McGehee BE, Pollock JM, Maldjian JA. `Brain perfusion imaging: how does it work and what should I use <http://www.mri-q.com/uploads/3/2/7/4/3274160/mcgehee_whitlow_review.pdf>`_? J Magn Reson Imaging 2012; 36:1257-1272.
    * Wong EC, Cronin M, Wu W-C, et al. `Velocity-selective arterial spin labeling <http://www.mri-q.com/uploads/3/2/7/4/3274160/wong06_vsasl.pdf>`_. Magn Reson Med 2006; 55:1334-1341.

**相关问题**
	* `What is PASL and how does it differ from CASL? <http://www.mri-q.com/pasl.html>`_  
	* `What is pCASL and how does it differ from CASL and PASL? <http://www.mri-q.com/pcasl.html>`_  