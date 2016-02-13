Question-呼吸补偿：什么是呼吸补偿？与呼吸门控有何不同？
======================================================================================================

:date: 2015-12-06
:tags: MR Artifacts, motion related artifacts
:slug: respiratory-comp
:authors: Chunshan
:summary: 什么是呼吸补偿？与呼吸门控有何不同？

原文链接:\ `What is respiratory compensation? How does this differ from respiratory gating? <http://mri-q.com/respiratory-comp.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/4492525_orig.png
    :alt: summary
    :align: center
    :width: 700

如果呼吸模式比较规律，简单的呼吸门控对于减少运动伪影还是比较有效的。用带子或波纹管检测胸部扩张，呼吸曲线也显示在技师的控制台软件上，在呼吸曲线上选择触发数据采集的时间点。通常采集窗选择在呼气结束时，此时膈肌运动最小。由于仅在呼吸周期中的部分时间进行数据采集，简单的呼吸门控会延长成像时间50%-300%。

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/3512940_orig.gif?557
   :alt: Simple respiratory gating
   :align: center
   :width: 900

   简单呼吸门控。仅在呼气结束膈肌运动最小时进行数据采集。

与简单呼吸门控相比，呼吸补偿技术在整个呼吸周期连续采集数据。在呼气时进行低幅度相位编码采集（对运动非常敏感），在呼吸周期的其他时间进行高幅度相位编码采集（对运动不怎么敏感）。

最初的呼吸补偿方法是由Picker在1980年代发明，被称为ROPE（Respiratory Ordered Phase Encoding），现在主要的磁共振厂商都提供了此技术的变种，名字如“Respiratory Comp”（GE, Toshiba），“PEAR”（Phase Encoded Artifact Reduction, Philips），“PERRM”（Phase Encode Reordering to Reduce Motion, Hitachi）。这些方法可以有效抑制运动伪影，尤其对短TR成像。时间损失也比较轻微，大约10-15%（不包括安装和校准波纹管的时间）。典型的结果如下图所示。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/613260_orig.jpg      | .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/7262203_orig.jpg      |
|    :alt: Without respiratory compensation                                     |    :alt: With respiratory phase reordering                                     |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
|    没有呼吸补偿的图像                                                         |    根据呼吸相位重排的图像                                                      |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

**高级讨论**

不同厂商提供的呼吸补偿方法有些许变化和不同的选项。GE提供了“high sort”选项，类似于他们的“No Phase Wrap”技术。GE的“high sort”技术中，相位编码方向上的FOV和相位编码步数翻倍，而激发次数（NEX）减半。这有将呼吸运动伪影传播更远的效果，许多伪影就此移到显示FOV的外边。这种技术的缺点是血管运动导致的伪影可能会增加。

**参考材料**
     * Bailes DR, Gildendale DJ, Bydder GM et al.  `Respiratory ordered phase encoding (ROPE):  a method for reducing respiratory motion artifacts in MR imaging <http://mri-q.com/uploads/3/4/5/7/34572113/respiratory_ordered_phase_encoding__rope___a.39.pdf>`_.  J Comput Assist Tomogr 1985; 9:835-838. (The original method. Most respiratory compensation techniques in use today employ a variant or ROPE known as COPE - central ordered phase encoding).
     * Ehman RL, McNamara MT, Pallack M, et al. `Magnetic resonance imaging with respiratory gating: techniques and advantages <http://mri-q.com/uploads/3/4/5/7/34572113/ehman_respiratory_gating_1984_ajr.pdf>`_. AJR Am J Roentgenol 1984; 143:1175-1182.     
     * Lewis CE, Prato FS, Drost DJ, Nicholson RL. `Comparison of respiratory triggering and gating techniques for the removal of respiratory artifacts in MR imaging <http://mri-q.com/uploads/3/4/5/7/34572113/resp_gatingradiology2e1602e32e3737921.pdf>`_. Radiology 1986; 160:803-810.

**相关问题**
	* `怎么做心跳和呼吸门控? <http://chunshan.github.io/MRI-QA/motion-related-artifacts/gating-methods.html>`_