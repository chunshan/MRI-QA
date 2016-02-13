Question-运动伪影：为什么运动伪影在相位编码方向传播而不是频率编码方向？
===================================================================================

:date: 2015-12-02
:tags: MR Artifacts, motion related artifacts
:slug: motion-artifact-direction
:authors: Chunshan
:summary: 为什么运动伪影在相位编码方向传播而不是频率编码方向？

原文链接:\ `Why are motion artifacts propagated in the phase-encode direction instead of the frequency-encode direction? <http://mri-q.com/motion-artifact-direction.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/1373222_orig.png?308
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/8958625_orig.gif?376
   :alt: Why are motion artifacts propagated in the phase-encode direction instead of the frequency-encode direction
   :align: left
   :width: 500

在2DFT成像中，频率和相位编码方向上数据采集的采样时间之间存在着相当大的差距。在频率编码方向，所有256-512个信号的采样是在一个回波的间隔中获得的（例如，5-80毫秒）。相反，在相位编码方向上获取一个采样的时间在几秒钟到几分钟的级别，因为基本上k空间中所有的线必须都收集获得完整的数据集用于傅里叶重建。

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/3712012_orig.jpg?323
   :alt: Why are motion artifacts propagated in the phase-encode direction instead of the frequency-encode direction
   :align: right
   :width: 400

   在此轴向头部检查中，选择从左到右的相位编码方向，从而眼窝的运动伪影不会溢出到大脑区域。

最严重的生理运动（呼吸，吞咽，心脏搏动）的周期在一百毫秒到几秒钟之间。由于这些运动相对于频率采样间隔是缓慢的，它们通常在频率编码方向上产生空间上的局部轻微模糊。相反，由于相位采样间隔通常等于或比大多数的生理运动周期更长，伪影在这个方向上将更加突出。此外，无论生理运动发生在频率编码，相位编码，或切片选择方向，这些伪影都将在相位编码方向传播。

一个对所有类型的运动简单有效的成像策略是交换相位编码轴和频率编码轴。虽然这不会改变运动伪影，它会将伪影移到一个不同的方向从而使得伪影不会溢出到感兴趣区域。比如，在轴向头颅成像中，相位编码方向通常选为从左到右，这样眼窝的运动伪影就不会溢出到大脑区域。

**参考材料**
     * Axel L, Summers RM, Kressel HY, Charles C.  `Respiratory effects in two-dimensional Fourier transform MR imaging <http://mri-q.com/uploads/3/4/5/7/34572113/axel_respiratory.pdf>`_.  Radiology 1986; 160:795-801.
     * Storey P, Chen Q, Li W, et al. `Band artifacts due to bulk motion <http://mri-q.com/uploads/3/4/5/7/34572113/storey_band_artifacts_due_toperiodic_motion_mrm.pdf>`_. Magn Reson Med 2002; 48:1028-1036.
     * Wood ML, Henkelman RM.  `MR image artifacts from periodic motion <http://mri-q.com/uploads/3/4/5/7/34572113/wood_and_henkleman_motion_artifacts.pdf>`_.  Med Phys  1985;12:143-151.

**相关问题**
	* `为什么运动伪影常会形成离散的鬼影？ <http://chunshan.github.io/MRI-QA/motion-related-artifacts/why-discrete-ghosts.html>`_