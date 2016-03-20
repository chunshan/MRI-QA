Question-混叠：什么是混叠？
=======================================

:date: 2015-12-20
:tags: MR Artifacts, technique related artifacts
:slug: aliasing
:authors: Chunshan
:summary: 什么是混叠？

原文链接:\ `What is aliasing? <http://mri-q.com/aliasing.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/3716403_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6443188_orig.gif
   :alt: aliasing
   :align: right
   :width: 400

混叠(aliasing)是指由于数字采样频率不充分导致信号的频率测量得不准确。如果信号没有采样足够多的数据点，它的真实频率就会被低估。这种错误估计的信号将无法与另外真实低频率的信号进行区分（即混叠在一起）。

要正确地测量信号，数字采样频率必须至少为信号所含最高频率的两倍。这就是Nyquist采样定理（Nyquist sampling theorem）。

这种混叠现象不仅在磁共振成像中存在，而是存在于各种技术中，例如声音的失真，照片中的波纹状条纹，电影中不自然的动作等。“货车车轮效应”是一个常见的混淆现象的例子，在这个视觉错觉中，取决于视频中的数字帧率，车轮上的轮辐看起来会以不同的速率旋转，甚至会后退。

混叠是磁共振中一种重要的现象，是一种常见伪影（相位卷折，在下面几个Q&A中讨论）的根源。混叠伪影的其他形式包括MRS中远处体素的波谱污染和MRA中流速或流向的测量错误。混叠现象也可以利用，它也是并行成像技术如SENSE和GRAPPA的基础。

这种现象的物理基础可见如下的说明。注意到对相位编码梯度的每一个值，会分配相位周期的一个特定数字覆盖扫描视野。比如，在第一阶段相位编码步骤中，0°和360°之间的相移涵盖整个扫描视野，物体超出视野的部分，其相位小于0°，或大于360°。举例来说，示意图中的腹部左侧，超出了视野，相移为361°到450°。由于此相位编码步骤中所有有意义的频率已被定义到0°到360°之间，361°相移会被分配到1°相移的空间位置，450°相移会被分配到450°-360°=90°的空间位置。患者身体的左侧就会卷折，空间上错配到图像对侧（右）。患者的右侧卷折到左侧也是类似的过程。



**参考材料**
     * `"Aliasing" <https://en.wikipedia.org/wiki/Aliasing>`_. Wikipedia, the Free Encyclopedia.
     * Oldhasusen BA. `Aliasing <http://mri-q.com/uploads/3/4/5/7/34572113/aliasing.pdf>`_. (Lecture notes for Vision Science course, UC Davis, 10 Oct 2000, available on-line)

**相关问题**
	* `为什么会发生相位卷折伪影？ <http://chunshan.github.io/MRI-QA/technique-related-artifacts/wrap-around-artifact.html>`_