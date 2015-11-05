Question-注钆效应：在常规MR增强图像中钆对比剂用于增强信号，为什么在DSC灌注图像中信号减弱？
=====================================================================================================

:date: 2015-10-17
:tags: Perfusion, DSC
:slug: bolus-gd-effect
:authors: Chunshan
:summary: 在常规MR增强图像中钆对比剂用于增强信号,但在DSC灌注图像中信号减弱

原文链接:\ `If gadolinium contrast is used to increase signal intensity on routine MR images, why does it decrease signal on DSC perfusion images? <http://www.mri-q.com/bolus-gd-effect.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8041016_orig.png
    :alt: summary
    :align: center
    :width: 700

作为顺磁性对比剂，钆螯合物既能加速T1弛豫，又能加速T2（T2*）弛豫，哪种效应占主导地位取决于它的位置和浓度。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8677845_orig.jpg
   :alt: Gd effect
   :align: right
   :width: 400

   血管内阻隔钆化合物引起磁敏感性变化，导致主磁场（B0）畸变

传统磁共振成像中，钆浓度比较低并且广泛分布于组织细胞外空间时进行图像采集，这种情况下，T1缩短效应占据主导地位，钆化合物在T1加权像中比较明亮。

在DSC研究中，当钆化合物首次通过血管时进行图像采集，此时，钆螯合物浓度很高（通常超过2-3毫摩尔）。这缩短了T2（由于偶极-偶极相互作用）和T2*（由于血管壁内外对比剂浓度不同导致的磁敏感性变化）。周围扩散的水分子在变化的磁场中横向弛豫加速，导致T2或T2*加权序列中信号损失。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4971040_orig.jpg
   :alt: Gd effect image
   :width: 700

   DSC T2*加权图像，分别在钆对比剂经过前，经过时和经过后采集。中间图像为大脑信号减少的峰值，尤其是血管中


**高级讨论**

你可能已经想到，血管中的Gd和其T2*效应之间的关系比上面的简单讨论更加复杂。

首先，常规的钆造影剂被限制在血浆中，不进入血红细胞。因此，由于血管内血管外空间的分隔导致血管内空间有磁敏感性效应，分隔的程度与血细胞比容有关，而大血管和毛细血管的血细胞比容就是不同的。

磁场强度也很重要，磁敏感性效应一般与B0\ :sup:`2`\ 成正比。

所使用的脉冲序列也会决定不同血管中磁敏感性的相对贡献。GRE序列对所有血管中T2*失相位都很敏感，尤其是大血管；SE序列对小动脉，静脉和毛细血管中的T2效应更加敏感。

最后，血管相对于B0的方向影响血管内和血管外的磁敏感现象。例如血管平行于B0将没有血管外磁敏感性变化而垂直于B0的血管会有最强的磁敏感效应。这种奇怪的现象由偶极-偶极弛豫的角度依赖性导致，这在前面的一个Q&A中有解释。

**参考材料**
    * Boxerman J, Hambert L, Rosen B, Weisskoff R. `MR contrast due to intravascular magnetic susceptibility perturbations <http://www.mri-q.com/uploads/3/2/7/4/3274160/boxerman_1995.pdf>`_. Magn Reson Med 1995; 34:555-566. (explains susceptibility effect differences between large and small vessels).      
    * Villringer A, Rosen BR, Belliveau JW et al. `Dynamic imaging with lanthanide chelates in normal brain: contrast due to magnetic-susceptibility effects <http://www.mri-q.com/uploads/3/2/7/4/3274160/villringer_mrm_1988.png>`_. Magn Reson Med 1988; 6:164-174.

**相关问题**
	* `Can the T2-shortening effects of gadolinium ever be observed on routine MR imaging? <http://www.mri-q.com/does-gd-affect-t2.html>`_
	* `What is the difference between T2 and T2*? <http://www.mri-q.com/t2-vs-t2.html>`_   