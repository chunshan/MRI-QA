Question-连续动脉自旋标记（CASL） - CASL是什么？
=======================================================================================

:date: 2015-11-04
:tags: Perfusion, ASL
:slug: casl
:authors: Chunshan
:summary: CASL是什么

原文链接:\ `What is CASL? <http://www.mri-q.com/casl.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5136495_orig.png?312
    :alt: summary
    :align: center
    :width: 700

我们现在称之为CASL（Continuous Arterial Spin Labeling，CASL）的技术是最早真正的ASL方法，由Williams，Detre，及其他们的同事在20世纪90年代初提出。CASL使用一个恒定，低幅度，连续的RF脉冲结合成像梯度场使得成像层面近端的血流自旋反转。当这些自旋反转的血液流到成像层面，就会使信号强度略微下降，通过减法技术可以检测出信号的变化。虽然CASL目前仅有其历史价值，但如果要理解更新和更复杂的ASL技术，仍然需要首先理解CASL所体现的基本概念。

CASL（及其他所有ASL技术）中使用的反转脉冲产生一个有趣的（带来麻烦的）MR现象，磁化传递（Magetization Transfer，MT）。如在前面一个\ `Q&A <http://www.mri-q.com/magnetization-transfer1.html>`_\ 提到的，集中在反转层面的RF脉冲一处“溢出”就会导致MT现象，间接降低成像层面的信号强度。MT效应是由于水-大分子偏共振的相互作用导致的，与由流动产生的ASL信号完全独立。

MT现象在通常成像中也会发生，但通常不会引人注意，因为它仅会影响相邻层面组织信号强度的百分之几。在ASL中，标记图像和控制图像中的信号变化本就小于1%，不希望的MT效应产生的信号变化可能会压倒希望的血流相关的信号变化。

所有的ASL技术都需要解决如何消除MT效应的影响。下图给出了“MT问题”的说明和CASL中两种可能的解决办法。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/_5681302_orig.gif
   :alt: The MT problem and two CASL solutions  
   :width: 600 

   MT问题和两种CASL方法

上图的顶部一行说明了MT问题。使用一个偏共振（不同的共振频率和位置）的反转脉冲会降低成像层面的信号强度。这会混淆反映灌注的期望的信号改变。

第二行说明了最初的CASL解决方案。控制像使用第二个反转脉冲得到，该脉冲与第一个反转脉冲相同但是施加在成像层面相反的另一面。成像层面内的MT效应在标记像和控制像上是相同的，两张图像相减时MT效应被消除。

CASL解决方案2是由Alsop和Detre（1998）提出的最初方案的改进版。这种方法中扫描控制像序列的反转脉冲使用振幅调制分为两部分（边带），每个边带的幅值是原来脉冲的一半儿，而且两个边带离得很近，因此成像层面上的MT效应保持不变，控制像和标记像相减就可消除MT效应。分开的两个脉冲会使得控制像序列中流动血液的自旋没有净反转，因为成对并排放置的两个180°脉冲相当于360°脉冲（双重反转）。

CASL技术从20世纪90年代末逐渐失宠，对现在主要是历史和教学意义。CASL的主要问题是组织能量沉积比较高，而且由于连续RF脉冲的使用，发射线圈的占空比要求也比较高。因此PASL诞生了，PASL是ASL方法的一个大类的统称，使用脉冲（而不是连续）RF激励。PASL及其变种在下一个Q&A中讨论。

**高级讨论**

流动自旋可以被组合的射频脉冲和梯度场选择性地反转的想法是CASL和pCASL有趣而独特的特征。其背后的物理基础有点复杂，需要引入流动相关的绝热反转概念。

一般的绝热现象已经在之前的一个Q&A中介绍过。简单来说，绝热激发是一种仅在某些限制条件下发生的特殊类型的RF刺激，会产生一个近乎完美的净磁化（M）反转，对B1场的不均匀性也相对不那么敏感。这种现象在核磁共振发展的早期就被描述，对一个恒定磁场中的试样进行连续的RF激发，激发频率从远低于共振频率到远高于共振频率进行扫描，假使B1场足够强而且应用地足够慢（绝热条件），净磁化（M）的章动在扫描结束时会完全反转。

令人惊讶的是，ASL中流动自旋的绝热反转在RF场即使保持在恒定频率和振幅时也会发生。如果流动方向正好有一个很强的空间梯度场，而且同时伴随RF激发，绝热反转就会发生。当流动自旋沿着梯度方向移动，质子的共振频率就会随位置变化，外部看起来固定的RF场对流动的自旋而言就像频谱范围比较大的RF场。因此它们就会进行绝热跟随和反转，假使它们的速度（v）与动脉血的T2驰豫时间相比既不太长也不太短，梯度场强度（G）和有效场（≈ B1）的振幅满足如下关系：1/T2 << G•v/B1 << γB1。

**参考材料**
    * Alsop DC, Detre JA. `Multisection cerebral blood flow MR imaging with continuous arterial spin labeling <http://www.mri-q.com/uploads/3/2/7/4/3274160/alsop_detre_multislice_casl_radiology_1998.pdf>`_. Radiology 1998; 208:410-416. (improvement of the CASL technique using an amplitude modulated inversion pulse to self-correct for off-resonance effects) 
    * Williams DS, Detre JA, Leigh JS, Koretsky AP. `Magnetic resonance imaging of perfusion using spin inversion of arterial water <http://www.mri-q.com/uploads/3/2/7/4/3274160/pnas-1992-williams-212-6.pdf>`_. Proc Natl Acad Sci USA 1992; 89:212-216. (first demonstration of ASL, using a single-slice continuous technique in a rat brain, later known as CASL)
    * Wong EC, Buxton RB, Frank LR. `Implementation of quantitative perfusion imaging techniques for functional brain mapping using pulsed arterial spin labeling <http://www.mri-q.com/uploads/3/2/7/4/3274160/wong_pasl-picore.pdf>`_. NMR in Biomed 1997; 10:237-249. (comparison of CASL to pulsed methods)

**相关问题**
	* `您能解释一下各种ASL方法的不同之处么？哪一种最好？ <http://chunshan.github.io/MRI-QA/asl/pasl.html>`_  
	* `What is pCASL and how does it differ from CASL and PASL? <http://www.mri-q.com/pcasl.html>`_  