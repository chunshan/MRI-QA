Question-伪连续动脉自旋标记（pCASL） - pCASL是什么？它与CASL和PASL有何不同？
=======================================================================================

:date: 2015-11-06
:tags: Perfusion, ASL
:slug: pcasl
:authors: Chunshan
:summary: pCASL是什么

原文链接:\ `What is pCASL and how does it differ from CASL and PASL? <http://www.mri-q.com/pcasl.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/221064_orig.png
    :alt: summary
    :align: center
    :width: 700

2008年，Dai等提出了CASL和PASL的一种混合方法称为pCASL（Pseudo-Continuous Arterial Spin Labeling）。pCASL使用比较窄的标记平面（与CASL相似），穿过此平面，就会发生动脉自旋流动相关的绝热反转。靠近成像部位标记会立刻进行，最大限度地减少由于标记血液延迟引起的信号损失。CASL使用连续的射频辐射，pCASL则是使用一连串非常短的射频脉冲，模仿单一的长CASL脉冲的作用，但是能量沉积则小得多，射频脉冲放大器占空比的要求也小得多。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/7981291_orig.png?324
   :alt: The pCASL technique
   :width: 600 

   pCASL技术：狭窄标记带靠近成像部位

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3168742_orig.png?386
   :alt: The pCASL technique
   :align: left
   :width: 500 

   pCASL技术：狭窄标记带靠近成像部位   

典型的pCASL实现会在1.5s时间内施加750个Hanning状的20°射频脉冲，每一个持续0.5ms。标记序列中层面选择梯度的重聚部分是不平衡的。这意味着流动自旋会在每一个施加的射频脉冲期间累计额外的相位偏移。控制序列使用平衡的梯度场去除这种效应，另外，控制序列中每一个RF脉冲的相位是交替的。

由于前面已经介绍的原因，pCASL非常受欢迎，是我们目前选择的ASL方法。与PASL相比，pCASL有更高的信噪比，而且对标记后血流的（示踪剂）分散更不敏感。与CASL相比，pCASL有更高的标记效率，能够在现代扫描器中仅通过软件修改就能实现。但是pCASL的标记效率没有PASL高，而且对血流速度，血流角度，B0和B1场的不均匀性非常敏感。

**高级讨论**

流动自旋可以被组合的射频脉冲和梯度场选择性地反转的想法是CASL和pCASL有趣而独特的特征。其背后的物理基础有点复杂，需要引入流动相关的绝热反转概念。CASL和pCASL中自旋反转的机制与PASL并不相同，PASL中使用传统的绝热反转脉冲，标记时不需要流动。

一般的绝热现象已经在之前的一个Q&A中介绍过。简单来说，绝热激发是一种仅在某些限制条件下发生的特殊类型的RF刺激，会产生一个近乎完美的净磁化（M）反转，对B1场的不均匀性也相对不那么敏感。这种现象在核磁共振发展的早期就被描述，对一个恒定磁场中的试样进行连续的RF激发，激发频率从远低于共振频率到远高于共振频率进行扫描，假使B1场足够强而且应用地足够慢（绝热条件），净磁化（M）的章动在扫描结束时会完全反转。

令人惊讶的是，ASL中流动自旋的绝热反转在RF场即使保持在恒定频率和振幅时也会发生。如果流动方向正好有一个很强的空间梯度场，而且同时伴随RF激发，绝热反转就会发生。当流动自旋沿着梯度方向移动，质子的共振频率就会随位置变化，外部看起来固定的RF场对流动的自旋而言就像频谱范围比较大的RF场。因此它们就会进行绝热跟随和反转，假使它们的速度（v）与动脉血的T2驰豫时间相比既不太长也不太短，梯度场强度（G）和有效场（≈ B1）的振幅满足如下关系：1/T2 << G•v/B1 << γB1。

**参考材料**
    * Dai W, Garcia D, de Bazelaire C, Alsop DC. `Continuous flow driven inversion for arterial spin labeling using pulsed radiofrequency and gradient fields <http://www.mri-q.com/uploads/3/2/7/4/3274160/dai_pcasl_nihms73391.pdf>`_. Magn Reson Med 2008; 60:1488-1497. (original description of pCASL)
    * Golay X, Hendrikse J, Lim TCC. `Perfusion imaging using arterial spin labeling <http://www.mri-q.com/uploads/3/2/7/4/3274160/asl_review_2004.pdf>`_. Top Magn Reson Imaing 2004; 15:10-27. (Good review plus a description of ASL of variants and acronyms such as FAIRER, TILT, BASE, and others). 
    * Luh W-M, Wong EC, Bandettini PA, Hyde JS. `QUIPSS II with thin-slice TI1 periodic saturation: a method for improving accuracy of quantitative perfusion imaging using pulsed arterial spin labeling <http://www.mri-q.com/uploads/3/2/7/4/3274160/quipss-ii.pdf>`_. Magn Reson Med 1999; 41:1246-1254.
    * Petersen ET, Lim T, Golay X. `Model-free arterial spin labeling quantification: approach for perfusion MRI <http://www.mri-q.com/uploads/3/2/7/4/3274160/quasar_petersen06.pdf>`_. Magn Reson Med 2006; 55:219-232. (QUASAR method)
    * Wong EC, Buxton RB, Frank LR. `Quantitative imaging of perfusion using single subtraction (QUIPSS and QUIPSS II) <http://www.mri-q.com/uploads/3/2/7/4/3274160/wong_quippsii_mrm_1998.pdf>`_. Magn Reson Med 1998; 39:702-708.

**相关问题**
	* `您能解释一下各种ASL方法的不同之处么？哪一种最好？ <http://chunshan.github.io/MRI-QA/asl/pasl.html>`_