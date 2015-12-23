Question-ASL伪影 - 我们应该知道ASL的哪些伪影？
=======================================================================================

:date: 2015-11-08
:tags: Perfusion, ASL
:slug: asl-artifacts
:authors: Chunshan
:summary: ASL的伪影

原文链接:\ `What ASL artifacts should we know about? <http://www.mri-q.com/asl-artifacts.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/9624156_orig.png?318
    :alt: summary
    :align: center
    :width: 700

**磁敏感性伪影** ASL会遇到其他MR成像技术相同的伪影，包括磁敏感性，血流和运动。然而，与常规图像伪影问题相比，一些问题在ASL图像上以不同的方式显现。在左边的图像中，磁敏感性伪影很容易辨认，酷似ASL图像中的灌注不足/梗死区域。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6069428_orig.jpg
   :alt: Susceptibility artifact mimicking area of hypoperfusion on ASL
   :align: center
   :width: 500 

   酷似ASL灌注不足区域的磁敏感性伪影

**线圈灵敏度伪影** 接收线圈灵敏度空间变化导致的伪影也与ASL图像高/低灌注区域很像，在右边的图像中，箭头所指为虚假的灌注升高，通过检查原图像可以辨识其本质。通过图像滤波或者其他的后处理技术可以减轻线圈伪影。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5804793_orig.jpg
   :alt: Coil sensitivity artifact
   :align: center
   :width: 500

   线圈敏感性伪影 

**运动伪影** 控制序列和标记序列之间患者经常会有一定的运动，表现在感兴趣区域周围的光环。大脑ASL中，运动伪影通常表现为明显的头皮可视化，有时也表现为层与层之间亮度上的变化。一般进行后处理运动校正算法对齐对应的图像，减少患者总运动的影响。位置改变大的层面甚至可以丢弃，并不会引起信噪比的显著下降。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3619387_orig.jpg
   :alt: Motion artifact on ASL
   :align: center
   :width: 500

   连续ASL片层上的运动伪影表现为对比度改变和图像边缘明亮的光环 

**下游信号损失** 大多数ASL技术的一个共同特点是最下游（即反转层面的远端）的片层信号会降低。这种信号的损失由标记质子的从反转到读出这段时间的T1弛豫导致。这种现象在1.5T比3.0T更明显，因为血液固有的T1值在低场下更短。该伪影可通过使用三维读出和并行成像技术缩短图像采集时间减少。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/2639759_orig.gif?302
   :alt: Downstream signal loss in higher slices
   :align: center
   :width: 500

   顶部片层的下游信号衰减

**血管内信号伪影** 晚期到达的标记自旋在成像时刻可能来不及扩散到组织中，仍然存在于大动脉中。如果标记过程中反转的血团没有明确的划定，反转时间（TI）太短，或者动脉血团因病理延迟到达，这种伪影就会发生。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8226372_orig.gif?177 | .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/9403318_orig.gif?155  |
|    :alt: Intravacular signal artifact                                         |    :alt: Intravacular signal artifact                                          |
|    :width: 300                                                                |    :width: 300                                                                 |
|                                                                               |                                                                                |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6897319_orig.jpg?130
   :alt: Arterial signals in patient with carotid occlusion
   :align: right
   :width: 200

   颈动脉闭塞患者的动脉信号

灌注图像上的大血管信号也可表现为大脑或其他器官表面特别明亮的斑点。在上图中，我们看到右侧大脑中动脉（蓝色箭头，左边图像）和上矢状窦（白色箭头，右边图像）的明亮信号。

为了减少大血管信号，往往在读出图像之前立即沿几个轴使用大的双极性破碎梯度，而且还必须要考虑最优TI的选择，这取决于预期的血管流量。儿科患者TI须较短而老年患者TI须较长。尽管大血管信号通常是令人讨厌的伪影，但ASL中持续的高血管信号也是一个有用的临床体征，反映血管疾病导致的动脉延迟运输。右侧的图像显示了大脑动脉的高ASL信号，此患者长期颈内动脉闭塞导致血流缓慢。

**失败的背景抑制** 由于标记序列和控制序列之间的MR信号差异非常小，任何运动或者背景组织中的其他变化导致的噪声和伪影都可能淹没灌注加权图像，对3D ASL方法尤其如此。为了减少这种伪影，多数临床ASL序列采用几种类型的成像体积的背景抑制。

通常的方法是对静态组织应用额外的切片特定的反转或饱和脉冲，同时保证对血流敏感的部位相对不受影响。如果在ASL检查中背景饱和失败，后处理方法可以识别并且丢弃受影响的层面，从而避免一个完全不可用的检查。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4085312_orig.jpg
   :alt: Failed background suppression in ASL 
   :align: center
   :width: 600

   失败的ASL图像背景抑制显示由于T2穿透效应导致的脑室异常高信号（箭头）。原始数据图像显示了背景抑制在控制像（中）上如何失败，但是标记像上没有失败。

**参考材料**
    * Diebler AR, Pollock JM, Kraft RA, et al. `Arterial spin-labeling in routine clinical practice, Part 1: techniques and artifacts <http://www.mri-q.com/uploads/3/2/7/4/3274160/deibler_asl1.pdf>`_. AJNR Am J Neuroradiol 2008; 29:1228-1234.  
    * Petersen ET, Zimine I, Ho Y-C L, Golay X. `Non-invasive measurement of perfusion: a critical review of arterial spin labelling techniques <http://www.mri-q.com/uploads/3/2/7/4/3274160/bjr_67705974.pdf>`_. Br J Radiol 2006; 79:688-701.   
    * Ye FQ, Mattay VS, Jezzard P, et al. `Correction for vascular artifacts in cerebral blood flow values measured by using arterial spin tagging techniques <http://www.mri-q.com/uploads/3/2/7/4/3274160/ye_crushers_asl_1910370215_ftp.pdf>`_. Magn Reson Med 1997; 37:226–235. (use of bipolar crusher gradients to suppress ASL signal in large arteries)

**相关问题**
	* `Can gadolinium be given in conjunction with ASL? <http://www.mri-q.com/gadolinium-and-asl.html>`_