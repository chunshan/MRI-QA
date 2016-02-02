Question-反转恢复序列中的反弹点伪影：我注意到T1-FLAIR图像中有时也会出现“印度墨水”样的轮廓，这也是一种化学位移伪影么？
===========================================================================================================================================

:date: 2015-11-25
:tags: MR Artifacts, tissue related artifacts
:slug: ir-bounce-point
:authors: Chunshan
:summary: 反转恢复序列中的反弹点伪影

原文链接:\ `I've noticed that T1-FLAIR images may show "India ink" outlines. Is this also a chemical shift artifact? <http://www.mri-q.com/ir-bounce-point.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/5438182_orig.png?296
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/6245172_orig.jpg?308
   :alt: Bounce point artifact
   :align: right
   :width: 400

   反弹点伪影

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/6208716_orig.gif?313
   :alt: Bounce Point occurs in magnitude-reconstructed IR images at intermediate time (TI)
   :align: right
   :width: 400

   反弹点发生在幅值重建的反转恢复序列图像的中间时间（TI），此时含两种物质的体素会穿过零轴

反转恢复（IR）序列图像某些解剖结构有时会看到黑色轮廓，这不是由于化学位移引起的，而是由边界像素磁共振信号的相位取消引起的，机制与化学位移伪影类似。

右图显示了一个例子。注意大脑与脑脊液（CSF）边界处锐利的蚀刻样黑线，这通常称为反弹点伪影（最初被命名为“反向磁化伪影”）。在反转恢复成像中，组织磁化（M）反转到与主磁场相反的方向，然后逐渐恢复，此过程中会穿过零点。因为组织的T1值不同，恢复曲线也不同。右边的图表中，脑脊液（CSF）的T1比脑组织长，恢复得比脑组织慢。在只重建幅值的反转恢复（IR）序列中，从零到每种组织恢复曲线的距离就是显示的信号强度。每个组织的跨零点分配为黑色，称为空点或反弹点。

考虑脑脊液（CSF）和脑组织边界的一个像素，假设此像素中有相同量的两种组织。假设反转时间（TI）为介于脑组织和脑脊液反弹点之间的一个值，此时脑组织曲线在零轴上方，脑脊液曲线在零轴下方，两条曲线到零轴的距离恰好是相等的。也就是说该点脑组织信号和脑脊液信号幅值相同但是相位差180，失相位。信号被完全抵消，边界像素被渲染为黑色。

虽然上面反弹点伪影使用传统的幅值校正反转恢复（IR）图像进行描述，相同的现象出现在所有带反转脉冲的序列中，所以反弹点伪影也会出现在MP-RAGE,FGATIR或准IR SPGR等序列中。

**参考材料**
     * Hearshen DO, Ellis JH, Carson PL, et al. `Boundary effects from opposed magnetization artifact in IR images <http://www.mri-q.com/uploads/3/4/5/7/34572113/boundary_effect_ir_artifactradiology2e1602e22e3014600.pdf>`_. Radiology 1986; 160:543-7.

**相关问题**
	* `What is phase-sensitive IR and why does it have a gray background? <http://www.mri-q.com/phase-sensitive-ir.html>`_
	* `How do you pick a TI value to null signal from a given tissue? <http://www.mri-q.com/ti-to-null-a-tissue.html>`_
	* `What is T1-FLAIR? <http://www.mri-q.com/t1-flair.html>`_