Question-MR灌注概述：MRI中的DSC，DCE和ASL灌注方法有何不同？
=============================================================

:date: 2015-10-15
:tags: Perfusion, DSC, DCE, ASL
:slug: dsc-v-dce-v-asl
:authors: Chunshan
:summary: MRI中的DSC，DCE和ASL等灌注方法的不同之处

.. |Ktrans| replace:: K\ :sup:`trans`

原文链接:\ `What are the differences between DSC, DCE and ASL perfusion methods used in MRI? <http://www.mri-q.com/dsc-v-dce-v-asl.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/2402275_orig.png
    :alt: summary
    :align: center
    :width: 700

MRI测量灌注有三种常用方法：动态磁敏感对比度成像（DSC，Dynamic Susceptibility Contrast），动态对比增强成像（DCE，Dynamic Contrast Enhanced）和动脉自旋标记（ASL，Arterial Spin Labeling）。DSC和DCE都需要静脉注射钆螯合物，而ASL不需要外源性对比剂。这些技术将在下面简要说明，在后续的Q&A中有更详细的解释。

磁共振动态磁敏感性对比成像-DSC
____________________________________
DSC灌注成像首先静脉团注钆螯合物，随后对感兴趣器官快速获取一系列梯度回波或自旋回波图像。当钆螯合物首次通过局部循环时，它仍然主要局限在血管内空间。由于钆基的顺磁性特征，团注通过时钆基在血管周围产生局部磁场扰动，T2(T2*)失相位造成信号损失。通过测量随时间变化的信号强度，并且按照一定的数学模型拟合，各种灌注参数（如，血容量，血流量，平均通过时间）都能够计算出来。由于DSC成像仅依赖于对比剂的首次通过，它有时被称为造影剂跟踪检查。，图像采集时间非常短（约2分钟）。
             
+--------------------------------------------------------------------------+----------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/2636614_orig.jpg| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/1927254_orig.gif  |
|    :alt: T1 weighted image of Gd                                         |    :alt: CBV of DSC                                                        |
|    :width: 300                                                           |    :width: 300                                                             |
|                                                                          |                                                                            |
|    恶性脑肿瘤，钆螯合物增强的T1加权像                                    |    DSC的脑血容量参数图                                                     |
+--------------------------------------------------------------------------+----------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6485778_orig.gif| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/1126093_orig.jpg  |
|    :alt: Ktrans of DCE                                                   |    :alt: CBV of ASL                                                        |
|    :width: 300                                                           |    :width: 300                                                             |
|                                                                          |                                                                            |
|    DCE的K\ :sup:`trans` 参数图                                           |    ASL的脑血流量参数图                                                     |
+--------------------------------------------------------------------------+----------------------------------------------------------------------------+

磁共振动态对比增强成像-DCE
_______________________________
与DSC类似，DCE也需要注射钆基造影剂。但是DCE利用钆螯合物的T1缩短效应，在大约5-10分钟时间内重复获取T1加权图像。在此期间，钆造影剂在组织内的细胞外空间聚集，速度由灌注，毛细血管通透性和毛细血管表面积共同决定。这些图像数据可以直观地分析或半定量分析。应用房室模型可以得到量化结果，计算出多个生理参数，包括转移常数（|Ktrans|），血浆体积分数（VP）和组织细胞外空间的体积分数（VE）。

动脉自旋标记-ASL
______________________
与DSC和DCE不同，ASL不需要注射钆基对比剂，而是通过在近端血管用射频脉冲“磁标记”水分子，使用病人自己的水分子作为内源性扩散示踪剂。当这些水分子流到感兴趣的器官，他们会减少组织的信号强度，与灌注成比例。典型的ASL脉冲序列中，会在有标记脉冲和无标记脉冲情况下都采集图像，然后相减。通过应用数学模型，可以得到各种灌注参数（主要是血流量）。ASL技术本身的信噪比就比较低，所以需多次测量取平均，导致成像时间至少需要3-5分钟才能获得有用的数据。由于信噪比的限制，3T下的ASL明显好于1.5T。

DSC，DCE和ASL更详细的描述在后续的Q&A中会提供。如下的汇总表提供了各种技术的比较。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4213649_orig.png?640
   :alt: dsc-v-dce-v-asl
   :width: 700

**参考材料**
     * Borogovac A, Asllani I. `Arterial spin labeling (ASL) fMRI: advantages, theoretical constrains and experimental challenges in neurosciences <http://www.mri-q.com/uploads/3/2/7/4/3274160/asl_technical_review_818456.pdf>`_. Int J Biomed Imaging 2012; Article ID 818456:1-13. 
     * Diebler AR, Pollock JM, Kraft RA, et al. `Arterial spin-labeling in routine clinical practice, Part 1: techniques and artifacts <http://www.mri-q.com/uploads/3/2/7/4/3274160/deibler_asl1.pdf>`_. AJNR Am J Neuroradiol 2008; 29:1228-1234.
     * Essig M, Shiroishi MS, Nguyen TB, et al. `Perfusion MRI: the five most frequently asked technical questions <http://www.mri-q.com/uploads/3/2/7/4/3274160/essig_5_questions_ajr2e122e9543.pdf>`_. AJR Am J Roentgenol 2013; 200:24-34.
     * Ferré J-C, Bannier E, Raoult H, et al. `Arterial spin labeling (ASL) perfusion: techniques and clinical use <http://www.mri-q.com/uploads/3/2/7/4/3274160/asl_review_1156841300209x_1-s2.0-s221156841300209x-main.pdf>`_. Diagn Interv Radiol 2013; 94:1211-1223
     * Jahng G-H, Li K-L, Ostergaard l, Calamante F. `Perfusion magnetic resonance imaging: a comprehensive update on principles and techniques <http://www.mri-q.com/uploads/3/2/7/4/3274160/perfusion_review_article_kjr-15-554.pdf>`_. Korean J Radiol 2014; 15:554-577. (good recent review).
     * McGehee BE, Pollock JM, Maldjian JA. `Brain perfusion imaging: how does it work and what should I use <http://www.mri-q.com/uploads/3/2/7/4/3274160/mcgehee_whitlow_review.pdf>`_? J Magn Reson Imaging 2012; 36:1257-1272.
     * Tofts PS. `T1-weighted DCE imaging concepts: modelling, acquisition and analysis <http://www.mri-q.com/uploads/3/2/7/4/3274160/dce-mri_siemens.pdf>`_. MAGNETOM Flash 2010; 3:30-35.
     * Zaharchuk G. `Theoretical basis of hemodynamic MR imaging techniques to measure cerebral blood volume, cerebral blood flow, and permeability <http://www.mri-q.com/uploads/3/2/7/4/3274160/ajnr_zharchuk_perfusion_review.pdf>`_. AJNR Am J Neuroradiol 2007; 28:1850-8.

**相关问题**
	* `Question-DSC：如何做一个DSC灌注研究？ <http://chunshan.github.io/MRI-QA/dsc/how-to-perform-dsc.html>`_