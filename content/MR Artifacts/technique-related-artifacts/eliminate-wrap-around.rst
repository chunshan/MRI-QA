Question-减少卷折：如何消除相位卷折伪影？
================================================================================

:date: 2015-12-22
:tags: MR Artifacts, technique related artifacts
:slug: eliminate-wrap-around
:authors: Chunshan
:summary: 如何消除相位卷折伪影？

原文链接:\ `How do I get rid of phase wrap-around artifacts? <http://mri-q.com/eliminate-wrap-around.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/3644473_orig.png?292
    :alt: summary
    :align: center
    :width: 700

消除相位卷折伪影最简单的方法是增加相位的视野（FOV）使得覆盖扫描对象相位编码方向上整个的解剖尺寸。这个解决方案在下图说明，显示卷折随着相位FOV从15cm增加到20cm再到30cm过程中如何逐步消除。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6257815_orig.jpg?206    | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/4470085_orig.jpg?197     | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/9590518_orig.jpg?205     |
|    :alt: phase wrap-around                                                    |    :alt: phase wrap-around                                                     |    :alt: no phase wrap-around                                                  |
|    :width: 300                                                                |    :width: 300                                                                 |    :width: 200                                                                 |
|                                                                               |                                                                                |                                                                                |
|    FOV = 15 cm                                                                |    FOV = 20 cm                                                                 |    FOV = 30 cm                                                                 |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

上述方法也不是全无代价的，FOV增加空间分辨率就会受损失。为了保持空间分辨率，相位编码步数就必须增加。相位卷折可以被消除，但是成像时间会增加。

一种替代策略是，交换频率编码轴和相位编码轴使得扫描对象较短的维度正好在相位编码方向上。但是如果FOV非常小，对象短的解剖维度仍会超出视野，相位卷折还是会发生。此外，交换相位和频率轴也会引入其他不同的非期望的伪影（如运动引起的相位鬼影或化学位移伪影），因此限制了这种简单策略的实用性。

另一组技术通过最小化视野之外组织的信号消除相位卷折伪影。这些技术包括使用表面线圈（不能检测远离线圈的信号），在视野外应用饱和脉冲（消除视野外的信号）。

最后，“相位过采样（phase oversampling）”或者“非相位卷折（no-phase-wrap）”技术也可在很大程度上消除大多数情况下的相位卷折伪影。这些技术是\ `下面Q&A <http://chunshan.github.io/MRI-QA/technique-related-artifacts/phase-oversampling.html>`_\ 的主题。

**参考材料**
     * Axel L, Morton D. `Correction of phase wrapping in magnetic resonance imaging <http://mri-q.com/uploads/3/4/5/7/34572113/axel_phase_wrapping.pdf>`_. Med Phys 1989;16:284-287.
     * Heiland S. `From A as in aliasing to Z as in zipper: artifacts in MRI <http://mri-q.com/uploads/3/4/5/7/34572113/artifacts_a_to_z.pdf>`_. Clin Neuroradiol 2008; 1:25-36.  
     * Pusey E, Yoon C, Anselmo ML, Lufkin RB. Aliasing artifacts in MR imaging. Comput Med Imag Graphics 1988;12:219-224.  
     * Zhuo J, Gullapalli RP. `AAPM/RSNA physics tutorial for residents <http://mri-q.com/uploads/3/4/5/7/34572113/zhuo_aritfacts_radiographics.pdf>`_. MR artifacts, safety, and quality control. Radiographics 2006;26:275-297.

**相关问题**
	* `为什么会发生相位卷折伪影？ <http://chunshan.github.io/MRI-QA/technique-related-artifacts/wrap-around-artifact.html>`_