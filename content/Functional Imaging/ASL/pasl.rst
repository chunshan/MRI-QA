Question-脉冲动脉自旋标记（PASL） - PASL是什么？它与CASL有何不同？
=======================================================================================

:date: 2015-11-05
:tags: Perfusion, ASL
:slug: pasl
:authors: Chunshan
:summary: PASL是什么

原文链接:\ `What is PASL and how does it differ from CASL? <http://www.mri-q.com/pasl.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/735514_orig.png
    :alt: summary
    :align: center
    :width: 700

上一个Q&A中介绍的CASL（Continuous Arterial Spin Labeling）技术现在仅具有历史和教学意义，从20世纪90年代末逐渐失宠。CASL的主要问题是组织能量沉积比较高，而且由于连续RF脉冲的使用，发射线圈的占空比要求也比较高。因此PASL诞生了，PASL是ASL方法的一个大类的统称，使用脉冲（而不是连续）RF激励。三个PASL的变种在下表中描述。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/_1006945_orig.gif
   :alt: Pulsed Arterial Spin Labeling (PASL) methods  
   :width: 600 

   脉冲动脉自旋标记方法（PASL）

最早的PASL方法由Edelman和他的同事在20世纪90年代中期提出，称为\ *EPISTAR（Echo-Planar Imaging-based Signal Targeting by Alternating Radiofrequency pulses）*\ 。EPISTAR的标记像序列首先进行层选择性的90°脉冲和使用扰相梯度初步饱和成像层面中的磁化。（此脉冲的轮廓通常会略宽于成像层面以最小化一侧射频带来的伪影，并确保饱和度一致性。）然后使用180°绝热RF脉冲反转近端一个比较厚层面中流动的自旋。控制像序列重复成像层面中静态组织的90°扰相饱和梯度，接着反转远端比较厚的镜像层面来创造与第一个厚层相同的MT效应。控制像与标记像相减就产生灌注加权的图像，其中MT效应已经最小化。

单层EPISTAR随后进化为几个多层的变种（STAR，PULSAR和QUASAR），其中几个已经被Philips开发为商用产品。在高级讨论中会对此简要介绍。

*PICORE (Proximal Inversion with Control of Off-Resonance Effects)* 是另一个与EPISTAR相似的非对称多层PASL技术。实际上，标记序列与EPISTAR相同，也会进行成像层面饱和和使用近端反转脉冲。控制序列的不同之处在于180°反转脉冲使用与成像层面相同的频率偏移，这点与标记序列一样，但是没有空间梯度。

*FAIR (Flow-sensitive Alternating Inversion Recovery)* 采用一个稍微不同的脉冲标记策略，标记脉冲关于成像层面对称。标记序列首先会在成像层面周围的一个小区域施加一个空间选择的反转脉冲（此脉冲的轮廓通常会略宽于成像层面以最小化一侧射频带来的伪影，并确保饱和度一致性。）。控制序列会施加相同的反转脉冲但是没有选层梯度场。这会导致射频线圈内整个敏感体积中的自旋反转。Siemens的产品中就使用了带Q2-TIPS饱和的PICORE和FAIR序列（见高级讨论）。

EPISTAR，PICORE和FAIR的选择部分取决于希望成像区域中血流的结构。PICORE只从一侧标记血流，因此对血供都来自颈部的轴向脑灌注成像是一个合理选择。血流来自多个或者未知方向的情况下（如矢状位脑灌注成像或如肝这样的复杂器官中），FAIR会是一个更好的选择，因为它会标记成像容积的两侧。另外一个方面，FAIR可能对不必要的静脉血流引起的污染更加敏感，由于反转的层面轮廓不完美实现多层模式更加困难。在某些情况下，EPISTAR相较于其他方法会更有优势，因为其控制序列和标记序列间平衡的厚层选择梯度，从而涡电流伪影更少。

**高级讨论**

三种PASL技术之间另一个不同之处在于标记状态（St）和控制状态（Sc）之间信号的极性不同。对EPISTAR和PICORE而言，流入的动脉自旋是反转的，因此St<Sc；对FAIR而言，标记状态时磁化不是反转的但是在控制状态时磁化是反转的，因此St>Sc。

**上文提到的EPISTAR变种**

* 多层STAR（Signal Targeting by Alternating Radiofrequency pulses）以快速连续的两个一半幅度的近端反转层面取代了EPISTAR控制序列中单一的远端反转层面。这与CASL方案2有相同的效果，能够在成像层面上创建相同的MT效应但是对流动的自旋没有净效应。
* PULSAR（PULsed StAR）使用与STAR相同的反转策略但是使用更复杂的4光谱水抑制脉冲替代成像层面中90°选层脉冲和扰相梯度预饱和。
* QUASAR（QUantitative Star labeling of Arterial Regions）使用PULSAR中的标记和控制模块，紧接着施加Look-Locker策略采样多个时间点用于T1估计，和一个重复的类似于Q2-TIPS的饱和机制使得动脉血流更锐利。其他高级功能包括使用动脉输入函数（AIF）卷积方法进行的灌注量化。

**锐化动脉血团**

由于传输延迟和分散，血团的前边缘和后边缘可能都有些不明确。几个脉冲序列的改进版被提出来用于“锐化“也就是提升血团边缘的定义。比较早的一个称为QUIPSS (Quantitative Imaging of Perfusion using a Single Subtraction)，QUIPSS涉及PASL序列读出之前增加一个额外的用于层面选择的90°、18叶sinc饱和脉冲，如果应用于成像容积称为QUIPSS I或者应用于标记容积称为QUIPSS II。我们使用的一个流行的变种是Q2TIPS (QUIPSS II with Thin-slice TI1Periodic Saturation)，其使用标记区域远端一系列的厚层饱和脉冲取代单一的厚层饱和脉冲。两个操作者可选的参数可用于确定饱和链的开始和结束时间（也就是血团的边缘）。我们的Q2TIPS序列使用16个非常有选择性的抑制（VSS）脉冲，在最初反转后800-1200ms的时间窗内每隔25ms施加一次。这将饱和一个2cm厚的组织层面，留下距第一个成像层面大约1cm的间隔。

**参考材料**
    * Edelman RR, Chen Q. `EPISTAR MRI: Mulitslice mapping of cerebral blood flow <http://www.mri-q.com/uploads/3/2/7/4/3274160/edelman-mrm1998.pdf>`_. Magn Reson Med 1998; 40:800-805. (Later iteration of EPISTAR with modifications and multi-slice acquisition)
    * Edelman RR, Siewert B, Darby DG, et al. `Qualitative mapping of cerebral blood flow and functional localization with echo-planar MR imaging and signal targeting with alternating frequency <http://www.mri-q.com/uploads/3/2/7/4/3274160/edelman_siwert_radiology_epistar.pdf>`_. Radiology 1994; 192:513-520. (one of the early descriptions of EPISTAR)  
    * Golay X, Hendrikse J, Lim TCC. `Perfusion imaging using arterial spin labeling <http://www.mri-q.com/uploads/3/2/7/4/3274160/asl_review_2004.pdf>`_. Top Magn Reson Imaing 2004; 15:10-27. (Good review plus a description of ASL of variants and acronyms such as FAIRER, TILT, BASE, and others).
    * Golay X, Peterson ET, Hui F. `Pulsed Star labeling of arterial regions (PULSAR): a robust regional perfusion technique for high field imaging <http://www.mri-q.com/uploads/3/2/7/4/3274160/star-pulsar_20338_ftp.pdf>`_. Magn Res Med 2005; 53:15-21. 
    * Kim S-G. `Quantification of relative cerebral blood flow change by Flow-sensitive Alternating Inversion Recovery (FAIR) technique: application to functional mapping <http://www.mri-q.com/uploads/3/2/7/4/3274160/kim_sg_mrm_1995_fair.pdf>`_. Magn Reson Med 1995; 34:293-301. (original description of FAIR technique)
    * Luh W-M, Wong EC, Bandettini PA, Hyde JS. `QUIPSS II with thin-slice TI1 periodic saturation: a method for improving accuracy of quantitative perfusion imaging using pulsed arterial spin labeling <http://www.mri-q.com/uploads/3/2/7/4/3274160/quipss-ii.pdf>`_. Magn Reson Med 1999; 41:1246-1254 (description of the Q2TIPS method).
    * Petersen ET, Lim T, Golay X. `Model-free arterial spin labeling quantification: approach for perfusion MRI <http://www.mri-q.com/uploads/3/2/7/4/3274160/quasar_petersen06.pdf>`_. Magn Reson Med 2006; 55:219-232. (QUASAR method)
    * Wong EC, Buxton RB, Frank LR. `Implementation of quantitative perfusion imaging techniques for functional brain mapping using pulsed arterial spin labeling <http://www.mri-q.com/uploads/3/2/7/4/3274160/wong_pasl-picore.pdf>`_. NMR in Biomed 1997; 10:237-249. (description of the PASL/PICORE method)

**相关问题**
	* `您能解释一下各种ASL方法的不同之处么？哪一种最好？ <http://chunshan.github.io/MRI-QA/asl/pasl.html>`_  
	* `What is pCASL and how does it differ from CASL and PASL? <http://www.mri-q.com/pcasl.html>`_  