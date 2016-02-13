Question-鬼影：为什么运动伪影常会形成离散的鬼影？
================================================================================

:date: 2015-12-01
:tags: MR Artifacts, motion related artifacts
:slug: why-discrete-ghosts
:authors: Chunshan
:summary: 为什么运动伪影常会形成离散的鬼影？

原文链接:\ `Why do motion artifacts often form into discrete ghosts? <http://mri-q.com/why-discrete-ghosts.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/9775139_orig.png
    :alt: summary
    :align: center
    :width: 700

当成像视野（Field-Of-View，FOV）内的结构的位置或信号强度有规律地运动或发生变化时，离散的“鬼影”可能沿相位编码方向产生。血液或脑脊液的搏动流，心脏运动，呼吸运动是临床磁共振成像中产生鬼影的与病人相关的最重要的原因。鬼影的强度与周期性运动的幅度正相关，也与运动组织的信号强度正相关。

如果运动是非周期性的（如蠕动），不会产生离散的鬼影，而是会形成弥散的图像噪声，而且沿相位编码方向广泛传播。

图像中离散鬼影的间隔依赖于运动的主要方向（沿x,y或z轴），位移的幅值，周期性运动相对于相位采样的间隔。一般情况下，运动速度越快，鬼影的间隔会更宽。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/3830667_orig.jpg        | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/5059116_orig.jpg         |
|    :alt: Ghost Artifacts                                                      |    :alt: Ghost Artifacts                                                       |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/7969365_orig.gif
   :alt: Ghost Artifacts
   :align: center
   :width: 800

   运动伪影的出现取决于它们如何调制主要的成像频率（fo）。随机/非周期运动代表宽范围的复杂调制频率，傅里叶变换（FT）后会导致上下边带的扩散，产生弥散的，未聚焦的伪影。频率为fs的简单/规则/周期性运动会产生离散的边带，以鬼影的形式出现在主图像的两边。

常规的2DFT磁共振成像中，连续的两个相位采样之间的间隔为TR x NEX（因为在增加相位编码梯度前，一般会执行重复激发）。如果运动的周期（TP）等于TR x NEX，鬼影间隔会比较密集。相反，如果 TP = 2 x TR x NEX，鬼影间隔会很疏松。

**参考材料**
     * Axel L, Summers RM, Kressel HY, Charles C.  `Respiratory effects in two-dimensional Fourier transform MR imaging <http://mri-q.com/uploads/3/4/5/7/34572113/axel_respiratory.pdf>`_.  Radiology 1986; 160:795-801.
     * Storey P, Chen Q, Li W, et al. `Band artifacts due to bulk motion <http://mri-q.com/uploads/3/4/5/7/34572113/storey_band_artifacts_due_toperiodic_motion_mrm.pdf>`_. Magn Reson Med 2002; 48:1028-1036.
     * Wood ML, Henkelman RM.  `MR image artifacts from periodic motion <http://mri-q.com/uploads/3/4/5/7/34572113/wood_and_henkleman_motion_artifacts.pdf>`_.  Med Phys  1985;12:143-151.

**相关问题**
	* `为什么运动伪影在相位编码方向传播而不是频率编码方向？ <http://chunshan.github.io/MRI-QA/motion-related-artifacts/motion-artifact-direction.html>`_