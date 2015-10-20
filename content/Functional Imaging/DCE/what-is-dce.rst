Question-DCE概述：DCE成像是什么？与DSC成像有何不同？
======================================================================================

:date: 2015-10-24
:tags: Perfusion, DSC, DCE
:slug: what-is-dce
:authors: Chunshan
:summary: DCE成像概述及与DSC的不同之处

.. |Ktrans| replace:: K\ :sup:`trans`
.. |ve| replace:: v\ :sub:`e`
.. |vp| replace:: v\ :sub:`p`
.. |kep| replace:: k\ :sub:`ep`

原文链接:\ `What is DCE imaging and how does it differ from DSC imaging? <http://www.mri-q.com/what-is-dce.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8984630_orig.png
    :alt: summary
    :align: center
    :width: 700

动态对比增强（DCE，Dynamic Contrast Enhancement）成像测量注射钆造影剂后组织T1随时间的变化。它与动态磁敏性对比（DSC，Dynamic Susceptibility Contrast）不同，后者测量T2或T2*的变化。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/926004_orig.jpg
   :alt: Breakdown of BBB in a glioma
   :align: right
   :width: 400

   胶质瘤中血脑屏障被破坏

钆造影剂注射后，它会驻留在血浆中，并随血液流动到各个器官。这些相对小的药物分子（500-1000Da）会以被动扩散的方式穿过血管内皮细胞进入大多数组织的细胞外空间。唯一的例外是脑和脊髓，内皮细胞紧密连接构成了血脑屏障（BBB， Blood Brain Barrier）阻碍了扩散过程。如果血脑屏障被肿瘤，感染或者其他疾病破坏，钆造影剂就会累积，T1缩短使得T1对比度增强。

观察和量化对比度增强随时间的变化是DCE成像的主要目标。一般来讲，对比度增强的程度取决于局部血流量（F），血管的大小和数量（由组织单位质量的表面积S和渗透性P进行量化）。

虽然不可能将F，S，P每个部分单独分离出来，但是通过数学建模，我们可以测量它们的综合效应，反映在所谓的转移常数（|Ktrans|）中。|Ktrans|\ 表征钆对比剂穿过血管内皮细胞的扩散净流入。DCE计算出来的指标如K\ :sup:`trans`\ 在肿瘤治疗评价中越来越重要，特别是针对肿瘤血管的非细胞毒性靶向药物。|Ktrans|\ 也被用来评估肺，关节和其他器官的炎症过程。

除了K\ :sup:`trans`\ ，DCE也可以计算组织的其他参数，如：组织的血管外细胞外体积分数（|ve|），组织的血浆体积分数（|vp|）和钆造影剂从组织细胞外空间返流回血浆的流出常数（|kep|）。

这些不同DCE参数的意义和计算将在接下来的几个Q&A中阐述。

**参考材料**

**相关问题**
	* `Question-MR灌注概述：MRI中的DSC，DCE和ASL灌注方法有何不同？ <http://chunshan.github.io/MRI-QA/dsc/dsc-v-dce-v-asl.html>`_  
	* `Question-DCE成像：如何评估从DCE检查中获得的信息？ <http://chunshan.github.io/MRI-QA/dce/how-is-dce-analyzed.html>`_  
	* `What quantitative parameters can be extracted from the DCE data? <http://www.mri-q.com/dce-tissue-parmeters.html>`_  