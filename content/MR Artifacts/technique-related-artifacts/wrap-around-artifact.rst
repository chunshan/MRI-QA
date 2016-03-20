Question-磁共振伪影：为什么会发生相位卷折伪影？
================================================================================

:date: 2015-12-21
:tags: MR Artifacts, technique related artifacts
:slug: wrap-around-artifact
:authors: Chunshan
:summary: 为什么会发生相位卷折伪影？

原文链接:\ `Why does the phase wrap-around artifact occur? <http://mri-q.com/wrap-around-artifact.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6129701_orig.png
    :alt: summary
    :align: center
    :width: 700

相位卷折（Phase wrap-around）是一种常见的磁共振伪影，当一个物体的尺寸超出了定义的视野（field-of-view，FOV）就会发生，这是混叠（aliasing）现象的一种特殊表现，在前一个\ `Q&A <http://chunshan.github.io/MRI-QA/technique-related-artifacts/aliasing.html>`_\ 中已经有描述。混叠是当数字采样频率太低时信号频率的错误分配。

卷折伪影非常容易识别，表现为视野外的解剖结构折叠到感兴趣区域中。尽管该现象也会发生在频率编码方向，通常沿相位编码方向更严重。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/8789459_orig.jpg        | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/1819388_orig.jpg         |
|    :alt: phase wrap-around                                                    |    :alt: phase wrap-around                                                     |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/5097077_orig.jpg        | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/2980740_orig.jpg         |
|    :alt: phase wrap-around                                                    |    :alt: phase wrap-around                                                     |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/5127353_orig.gif?515
   :alt: phase wrap-around
   :align: center
   :width: 700

   卷折伪影的起因

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/8922810_orig.gif?222
   :alt: Wrap around in a 3DFT image
   :align: right
   :width: 250

   3DFT图像中的卷折

在3D成像中，末端的层面之间也会发生相位卷折伪影。对于3D傅里叶变换（体积）成像，相位编码用于定义各个层面。如果成像体积在层面选择方向超出了视野，在3D分区末端的层面之间也会发生相位卷折伪影。在右图3D头部MRI检查中，头顶部的头皮脂肪（白色椭圆）卷折叠加到颅底的组织上。   

**参考材料**
     * Axel L, Morton D. `Correction of phase wrapping in magnetic resonance imaging <http://mri-q.com/uploads/3/4/5/7/34572113/axel_phase_wrapping.pdf>`_. Med Phys 1989;16:284-287.
     * Heiland S. `From A as in aliasing to Z as in zipper: artifacts in MRI <http://mri-q.com/uploads/3/4/5/7/34572113/artifacts_a_to_z.pdf>`_. Clin Neuroradiol 2008; 1:25-36.  
     * Pusey E, Yoon C, Anselmo ML, Lufkin RB. Aliasing artifacts in MR imaging. Comput Med Imag Graphics 1988;12:219-224.  
     * Zhuo J, Gullapalli RP. `AAPM/RSNA physics tutorial for residents <http://mri-q.com/uploads/3/4/5/7/34572113/zhuo_aritfacts_radiographics.pdf>`_. MR artifacts, safety, and quality control. Radiographics 2006;26:275-297.

**相关问题**
	* `相位过采样如何消除卷折伪影？ <http://chunshan.github.io/MRI-QA/technique-related-artifacts/wrap-around-artifact.html>`_
	* `为什么卷折伪影在频率编码方向上看不到？ <http://chunshan.github.io/MRI-QA/technique-related-artifacts/aliasing.html>`_
	* `什么是混叠？ <http://chunshan.github.io/MRI-QA/technique-related-artifacts/aliasing.html>`_