Question-Nyquist N/2鬼影：在EPI上，我们经常可以看到三个重叠的图像，看起来像相位卷折伪影，这是怎么产生的？
============================================================================================================================

:date: 2015-12-27
:tags: MR Artifacts, technique related artifacts
:slug: nyquist-n2-ghosts
:authors: Chunshan
:summary: Nyquist N/2鬼影

原文链接:\ `On EPI we commonly see three overlapping images. It looks somewhat like a phase wraparound artifact. What is causing this? <http://mriquestions.com/nyquist-n2-ghosts.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/2567680_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6562_orig.jpg?261
   :alt: Nyquist N/2 Ghost Artifact
   :align: right
   :width: 300

   Nyquist N/2 鬼影

这篇文章介绍的伪影被称为Nyquist N/2鬼影，发生于平面回波成像（EPI）序列中，EPI序列以zig-zag轨迹填充k空间。头部MRI中，这种伪影有时又被称为“三个脑袋伪影（Three Brains Artifacts）”。

EPI脉冲序列由一系列回波组成，每一个回波产生k空间中的一横行数据。在zig-zag采集中，每两个回波采集方向会交替一次。对于图像重建，偶数的回波必须时间上反转从而与奇数的回波相匹配，才能进行傅里叶变换。

如果向前和向后的回波不是彼此的完美镜像，图像处理过程中就会引入伪影。即使第一个回波的开始有微小的延迟，也会传播到所有后续的回波，导致偶数回波和奇数回波的峰值时间有轻微差别。当做傅里叶变换时，该相位误差导致信号强度在图像相位编码方向偏移一半。如果FOV内有N个像素，此混叠的鬼影看起来相对于正确位置的主图像平移了N/2个像素。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6214368_orig.gif
   :alt: Zig-zag k-space trajectory
   :align: right
   :width: 300

   zig-zag形式k空间轨迹填充时奇数和偶数回波的峰值时间有轻微的差别是Nyquist N/2鬼影的原因之一

Nyquist鬼影有许多可能的原因包括糟糕的匀场，梯度线圈发热，病人运动和重建误差。然而最常见的原因是梯度脉冲快速变化使线圈感生涡电流和磁体壳。涡电流反过来产生局部磁场干扰B0场，在数据中添加了相位偏移。偶数线和奇数线的读出梯度方向相反，这意味着涡电流引起的相位偏移在这些交替的线上是相反的。

使用倾斜层面也有助于产生Nyquist N/2鬼影。倾斜成像需要在图像采集过程中对三个物理梯度（Gx，Gy，Gz）同步进行不同的混合，但是，每一个物理梯度有独特的电感，对开关接通和关闭的响应不同。如果三个梯度不是在完全相同的时间点激活和失活，就会发生相位误差。有时简单调整层面倾斜度（多或少）就可以减少Nyquist伪影。

其他减小Nyquist N/2伪影的方法包括重新匀场，减少回波链长度，降低相位编码分辨率，使用多次激发（分段）EPI，和应用并行成像加速。如果这些方法不起作用，伪影仍在多个部位上存在，可能需要让工程师进行全面维修，重新调整梯度和涡电流补偿。

**参考材料**
     * Buonocore MH, Gao L. `Ghost artifact reduction for echo planar imaging using image phase correction <http://mriquestions.com/uploads/3/4/5/7/34572113/nyquist_ghost_1910380114_ftp.pdf>`_. Magn Reson Med 1997; 38:89-100.
     * Yang QX, Posse S, Le Bihan D, Smith MB. `Double-sampled echo-planar imaging at 3 Tesla <http://mriquestions.com/uploads/3/4/5/7/34572113/yang_nyquist_ghost_1995.pdf>`_. J Magn Reson 1996; 113:145-150.

**相关问题**
	* `I've heard that "eddy currents" cause problems for imaging.  What are they? <http://mriquestions.com/eddy-current-problems.html>`_