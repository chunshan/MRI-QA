Question-部分容积效应：什么是部分容积效应？
================================================================================

:date: 2015-12-18
:tags: MR Artifacts, technique related artifacts
:slug: partial-volume-effects
:authors: Chunshan
:summary: 什么是部分容积效应？

原文链接:\ `What is meant by "partial voluming"? <http://mri-q.com/partial-volume-effects.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/924183_orig.png
    :alt: summary
    :align: center
    :width: 700

部分容积效应/伪影是一个在断面成像中广为人知的一个概念，概念很简单甚至可以不包含在这个Q&A网站中。但是，这个概念非常重要，为了非放射学相关的人能够理解这里的话题，所以我提供简要的解释和一些例子。

参考下面这个例子，部分容积的概念很容易理解。这儿的红色和黄色圆圈表示脑脊液（CSF，蓝色）中的神经和瘢痕组织，它们各自的磁共振图像显示在下面。左边的图示和图像为5毫米厚，右边的图示和图像为1毫米厚。5毫米厚的体素分辨率低，反映的是神经/瘢痕与脑脊液的混合信号；右边的薄层图像混合信号更少，各种不同的组织之间有清晰的边界。

+-------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/4722094_orig.gif        |
|    :alt: Partial volume averaging                                             |
|    :width: 800                                                                |
|                                                                               |
+-------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/9068790_orig.jpg        |
|    :alt: Partial volume averaging                                             |
|    :width: 800                                                                |
|                                                                               |
|    部分容积平均效应。5毫米厚层图像（左）蛛网膜下腔中精细的神经                |
|    和瘢痕不能分辨出来，因为图像中的信号是脑脊液和其他组织的混合/平均。        |
|    薄层（1毫米厚）图像（右）显示更详细的解剖结构，更有优势。                  |
+-------------------------------------------------------------------------------+

从数学上讲，考虑一个包含A和B两种材料的体素，占比分别为fA和fB，整个体素的磁共振信号（SV）反映的是分别来自两种成分层面的信号SA和SB的加权平均

SV  =  fASA  +  fBSB

不完美的射频脉冲轮廓会激发期望层面外部的组织，也会导致部分容积效应。如果多个层面放在一起，这种干扰称为cross-talk（串扰）。

减少部分容积效应的主要策略是使用更小，更清晰的体素。这意味着使用更薄的切片，更小的视野（FOV），和(或)更大的成像矩阵尺寸。使用持续时间更长的射频脉冲（或至少避免使用“fast-RF”脉冲选项）会改进层面的轮廓，创造更多精确的体素，减少相邻组织的激发。

**参考材料**
     * Kneeland JB, Shimakawa A, Wehrli FW. `Effect of intersection spacing on MR image contrast and study time <http://mri-q.com/uploads/3/4/5/7/34572113/kneeland_cross-talk_radiology2e1582e32e3945757.pdf>`_. Radiology 1986; 158:819-822.
     * Simmons A, Tofts PS, Barker GJ, Arridge SR. `Sources of intensity nonuniformity in spin echo images at 1.5T <http://mri-q.com/uploads/3/4/5/7/34572113/b79_simmons_intensitynu_mrm94.pdf>`_. Magn Reson Med 1994: 32:121-128.

**相关问题**
	* `What is cross-talk and what can be done about it? <http://mri-q.com/cross-talk.html>`_