Question-非相位卷折：相位过采样如何消除卷折伪影？
================================================================================

:date: 2015-12-23
:tags: MR Artifacts, technique related artifacts
:slug: phase-oversampling
:authors: Chunshan
:summary: 相位过采样如何消除卷折伪影？

原文链接:\ `How does phase oversampling eliminate the wrap-around artifact? <http://mri-q.com/phase-oversampling.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6844099_orig.png?313
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/4080625_orig.jpg?182
   :alt: Wrap-around artifact
   :align: right
   :width: 300

   卷折伪影

相位过采样，也被称为“非相位卷折”，是一种减少或消除卷折伪影（wrap-around artifacts）的技术。像在\ `前一个Q&A <http://chunshan.github.io/MRI-QA/technique-related-artifacts/eliminate-wrap-around.html>`_\ 中描述的，相位卷折是混叠的一种形式，当物体的解剖尺寸超出了定义的视野（FOV）时便会发生。物体超出FOV的部分在频率上出现错误，折叠到图像的边缘。卷折几乎只在相位编码方向出现。

减少或消除相位卷折伪影的几个直接的方法在\ `前面的Q&A <http://chunshan.github.io/MRI-QA/technique-related-artifacts/eliminate-wrap-around.html>`_\ 中已经讨论了，包括：1）增加FOV；2）交换相位和频率轴；3）使用表面线圈；4）应用饱和带。

所有的制造商也提供相位过采样技术控制相位卷折，这也是本Q&A的主题。如你所想到的，主要厂商对这一技术的命名并不相同：“相位过采样（Phase oversampling）”（Siemens），“非相位卷折（No phase-wrap）”（GE），“卷折抑制（Fold-over suppression）”（Philips），“反卷折（Anti-wrap）”（Hitachi），“相位卷折抑制（Phase-wrap suppression）”（Toshiba）。

所有的厂商都使用相同的技术，只有轻微的变化，说明如下。这个例子说明了100%相位过采样的情况，实际上大多数扫描仪上过采样因子是一定范围内可调节的。

相位过采样需要四个步骤，如果扫描仪软件中选择相位过采样这个选项，四个步骤就会自动进行。（1）相位编码方向上的视野（FOV）翻倍，（2）相位编码步数（Np）翻倍，（3）激励次数减半，（4）仅显示重建图像的中间部分。步骤（1）和（2）保证空间分辨率与不使用相位过采样时相同。步骤（3）保证信噪比和成像时间。

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/9110633_orig.gif?544
   :alt: phase oversampling
   :align: center
   :width: 700

尽管理论上使用相位过采样技术不会有额外损失，但还是有一些限制和特殊的考虑。首先，相位过采样不能与一些专门的多段技术（如POMP）结合使用，因为这些技术也要求增加FOV并且改变相位偏移。其次，由于激励次数减少以保证成像时间不变，相位过采样技术仅在原先采用至少两次激发的扫描中会没有时间损失。单次激发序列中也可以使用相位过采样，但需要使用半傅里叶（“½ NEX”）成像，会造成信噪比下降，相位错误增加。

最后，相位过采样技术不能阻止视野外组织的噪声和运动引入的相位偏移传播到成像体积（虽然对于稳定的组织可以有效去除）。例如，在矢状位颈椎检查中，如果相位编码方向是从上到下，图像质量仍然会因为呼吸和心脏搏动伪影导致退化，虽然心脏和胸部视觉上都没有卷折到脊椎图像中。

**参考材料**
     * Axel L, Morton D. `Correction of phase wrapping in magnetic resonance imaging <http://mri-q.com/uploads/3/4/5/7/34572113/axel_phase_wrapping.pdf>`_. Med Phys 1989;16:284-287.
     * Heiland S. `From A as in aliasing to Z as in zipper: artifacts in MRI <http://mri-q.com/uploads/3/4/5/7/34572113/artifacts_a_to_z.pdf>`_. Clin Neuroradiol 2008; 1:25-36.  
     * Pusey E, Yoon C, Anselmo ML, Lufkin RB. Aliasing artifacts in MR imaging. Comput Med Imag Graphics 1988;12:219-224.  
     * Zhuo J, Gullapalli RP. `AAPM/RSNA physics tutorial for residents <http://mri-q.com/uploads/3/4/5/7/34572113/zhuo_aritfacts_radiographics.pdf>`_. MR artifacts, safety, and quality control. Radiographics 2006;26:275-297.

**相关问题**
	* `为什么会发生相位卷折伪影？ <http://chunshan.github.io/MRI-QA/technique-related-artifacts/wrap-around-artifact.html>`_