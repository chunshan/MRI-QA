Question-平面回波成像（EPI）：什么是平面回波成像（EPI）？与快速自旋回波是一回事么？
======================================================================================================================

:date: 2014-11-03
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: echo-planar-imaging
:authors: Chunshan
:summary: 平面回波成像（EPI）

原文链接:\ `What is echo-planar imaging (EPI)? Is this the same as Fast Spin Echo (FSE)? <http://mriquestions.com/echo-planar-imaging.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5720410_orig.png?272
    :alt: summary
    :align: center
    :width: 700

梯度和数字化数据采集技术的进步使得50-100ms内获取一帧MR图像成为可能，从而最大限度减少患者运动的影响。一般来讲，这种采集模式称为平面回波成像（EPI，Echo-Planar Imaging）。

虽然EPI看起来像一个新的发展，实际上此技术是MRI中空间定位最早的方法之一，由Mansfield在1977年首先提出。Mansfield组在1981年产生第一幅跳动兔子心脏的生物学EPI图像，在1983年产生第一幅婴儿心脏图像。

MBEST是他们的一个早期EPI技术，在1980年代比较流行，如下图所示。一个自旋预备模块（可以就是一个简单的射频脉冲）之后，一个强切换频率编码梯度与一个间歇性的“尖峰状”低幅值相位编码梯度同时施加。随着每一个读出（频率）梯度的震荡采集梯度回波（GREs）。 

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6084364_orig.png?645
   :alt: MBEST
   :align: center
   :width: 800

   MBEST(Modulus-blipped echo-planar single-pulse technique)，早期EPI序列之一。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4287318_orig.png?216
   :alt: Zig-zag traversal of k-space from MBEST
   :align: right
   :width: 400

   MBEST中k空间的zig-zag遍历。频率编码沿水平轴，相位编码沿垂直轴。

最终的结果是对k空间的“zig-zag”遍历，第一个向下的频率和相位编码叶将最初的负相位偏移施加给所有的自旋，将信号从k空间中心移到左下角的一点，之前我们定义此点为（-kxmax，-kymax）。后续正的和负的频率编码叶分别从左到右和从右到左横扫k空间。同时，尖峰状的低幅值相位编码梯度脉冲产生沿ky轴的一个逐步阶跃增加。

如最初定义的那样，平面回波成像指的是整个2D平面k空间所有的数据是在一个RF激发脉冲之后采集的。最近，这个词已经扩展到包括任何快速梯度回波或自旋回波序列，只要k空间是在一个或少数几个激发后遍历的。使用现代的称呼，分别是单次激发EPI和多次激发EPI。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/8140851_orig.jpg?504
   :alt: Single Shot v.s. Multi Shot
   :align: center
   :width: 700

不同的厂商对这些概念定义了不同的术语，GE和Toshiba把一次激发中采集的k空间线（回波）的数目称为回波链长度（ETL，Echo Train Length），Siemens和Philips称之为“EPI factor”，Hitachi称为“shot factor”。多次激发序列中一次激发划分的k空间区域称为段（segment），因此，通常将每段所含的线（或视图）作为k空间覆盖力度的一个度量。

从广义上说，有非常高的turbo factor/ETL的快速自旋回波序列也可以认为是多次激发EPI序列。HASTE/SS-FSE技术就是一个例子。

**参考材料** 
    * Mansfield P. `Snap-shot MRI <http://mriquestions.com/uploads/3/4/5/7/34572113/mansfield-lecture.pdf>`_. Nobel Lecture, 8 Dec 2003 from www.nobelprize.org     Mansfield P. `Multi-planar image formation using NMR spin echoes <http://mri-q.com/uploads/3/4/5/7/34572113/mansfield-nmr_1977.pdf>`_. J Phys C: Solid State Phys 1977; 10:L55-L58.
    * Ordidge R. The development of echo-planar imaging (EPI):1977-1982. Magn Reson Mater Phys Biol Med 1999;9:117-121.
    * Poustchi-Amin M, Mirowitz SA, Brown JJ, et al. `Principles and applications of echo-planar imaging: a review for the general radiologist <http://pubs.rsna.org/doi/10.1148/radiographics.21.3.g01ma23767>`_. Radiographics May, 2001 (online only).
    * Redzian R, Mansfield P, Doyle M, et al. `Real-time nuclear magnetic resonance clinical imaging in paediatrics <http://mriquestions.com/uploads/3/4/5/7/34572113/redzian_539265.pdf>`_. Lancet 1983; 322:1281-2. (First human EPI image).
    * Stehling MK, Turner R, Mansfield P. `Echo-planar imaging: magnetic resonance imaging in a fraction of a second <http://mriquestions.com/uploads/3/4/5/7/34572113/stehling_epi_science_1991.pdf>`_. Science 1991; 254:43-50.

**相关问题**
  * `Who invented MR imaging? <http://mriquestions.com/who-invented-mri.html>`_
  * `什么是HASTE？ <http://chunshan.github.io/MRI-QA/rapid-imaging/hastess-fse.html>`_