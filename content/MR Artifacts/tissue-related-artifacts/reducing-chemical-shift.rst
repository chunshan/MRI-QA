Question-减少化学位移伪影：怎么做可以消除或减少化学位移伪影
=================================================================================

:date: 2015-11-22
:tags: MR Artifacts, tissue related artifacts
:slug: reducing-chemical-shift
:authors: Chunshan
:summary: 减少化学位移伪影

原文链接:\ `What can you do to eliminate or reduce the chemical shift artifact? <http://www.mri-q.com/reducing-chemical-shift.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6647287_orig.png?271
    :alt: summary
    :align: center
    :width: 700

如果认识了化学位移伪影，化学位移伪影一般可以识别出来并且不会造成图像解释的主要困难。但如果试图检测视神经或肾皮质细小病变的轻微异常，化学位移伪影的大小可能会完全掩盖病变。

解决化学位移伪影的一种简单方法是在成像之前交换频率和相位编码轴，这样做不会消除化学位移伪影，但是会将伪影旋转到另外的解剖区域。这样的策略可能不会成功，因为可能会导致相位卷折伪影或流动相关伪影转移到别的感兴趣区。

另一种策略是调整成像参数以减小伪影的尺寸。这可以通过增加总的接收带宽（或等价地，增加视野或读出梯度场的幅度）达到。

最后一个策略，可能是最好的，是使用一些脂肪抑制技术减小脂肪信号，从而最大限度减少伪影。这样的技术包括使用短时反转恢复序列（STIR）和脂肪饱和脉冲，其他的 `Q&A <http://www.mri-q.com/fat-water-imaging.html>`_ 中讨论了这些技术。

**参考材料**
     * Hood MN, Ho VB, Smirniotopoulos JG, Szumowski J. `Chemical shift: the artifact and clincial tool revisited <http://www.mri-q.com/uploads/3/2/7/4/3274160/hood_chemical_shiftradiographics2e192e22eg99mr07357.pdf>`_. Radiographics 1999; 19"357-371.   

**相关问题**
	* `什么是化学位移伪影？ <http://chunshan.github.io/MRI-QA/tissue-related-artifacts/chemical-shift-artifact.html>`_
	* `水和脂肪质子的化学位移难道不会导致它们之间的相位变化么？如果如此，为什么化学位移伪影在相位编码方向没有出现？ <http://chunshan.github.io/MRI-QA/tissue-related-artifacts/chemical-shift-in-phase.html>`_
	* `What is STIR? <http://www.mri-q.com/stir.html>`_