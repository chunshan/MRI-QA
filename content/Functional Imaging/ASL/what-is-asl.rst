Question-动脉自旋标记（ASL） -  什么是动脉自旋标记（ASL）？它是如何工作的？
======================================================================================

:date: 2015-11-02
:tags: Perfusion, ASL
:slug: what-is-asl
:authors: Chunshan
:summary: 什么是动脉自旋标记

原文链接:\ `What is arterial spin labeling (ASL) and how does it work? <http://www.mri-q.com/what-is-asl.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/9325976_orig.png?305
    :alt: summary
    :align: center
    :width: 700

动脉自旋标记（ASL），也被称为动脉自旋标记法，是一种利用患者自身的水分子作为示踪剂测量灌注的磁共振成像方法。与动态磁敏感对比成像（DSC）和动态对比增强成像（DCE）不同，ASL不需要注射钆造影剂或任何其他的外源性对比剂。

ASL的基本原理是，首先，采集感兴趣区图像（下图中为大脑半球）作为“控制像”；然后，“标记”脉冲施加于成像平面的上游层面，使此层面中水分子的自旋方向反转。在接下来的几秒钟内，大部分血管中“磁标记”的分子会流向成像区域，这些标记的水分子会与静态组织中的水分子交换磁化强度，使后者的平衡磁化强度略有降低（1%-2%）。感兴趣区域被重新成像，称为“标记像”，“控制像”与“标记像”逐像素相减得到的图像就是灌注加权的图像。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5714904_orig.gif?665
   :alt: Generic ASL method showing basic principles of image contrast
   :align: center
   :width: 700

   ASL中产生图像对比的基本原理的说明

与钆造影剂相比，水是一种扩散性示踪剂，这意味着标记的水分子不会局限于血管外空间，而是在ASL实验的过程中可以自由地从毛细血管进入到组织细胞。这会影响定量灌注的数学建模和计算。

除了测量灌注，ASL方法也可应用于磁共振血管造影产生血管图像。ASL还被越来越多地在功能磁共振成像中用于记录大脑激活区域，作为BOLD（血氧水平依赖技术）的替代方法。

有几种方法可用于ASL标记和成像，并没有单一的无可争议的最佳方法产生。这些技术的优点和缺点将会在后续的Q&A中探讨。

**高级讨论**

说明ASL基本原理的上图有厚厚的标记层面，一般用于PASL。对于CASL和pCASL，反转区域应该被压缩为一个窄带，对流经的血液进行标记。

此外，并非所有的ASL序列都会导致标记层面中的血流信号相对于“控制像”降低。在PASL的变种FAIR序列中，控制层面中的组织被抑制，流入血液具有比背景稍高的信号。

**参考材料**
    * Borogovac A, Asllani I. `Arterial spin labeling (ASL) fMRI: advantages, theoretical constrains and experimental challenges in neurosciences <http://www.mri-q.com/uploads/3/2/7/4/3274160/asl_technical_review_818456.pdf>`_. Int J Biomed Imaging 2012; Article ID 818456:1-13. 
    * Diebler AR, Pollock JM, Kraft RA, et al. `Arterial spin-labeling in routine clinical practice, Part 1: techniques and artifacts <http://www.mri-q.com/uploads/3/2/7/4/3274160/deibler_asl1.pdf>`_. AJNR Am J Neuroradiol 2008; 29:1228-1234.
    * Essig M, Shiroishi MS, Nguyen TB, et al. `Perfusion MRI: the five most frequently asked technical questions <http://www.mri-q.com/uploads/3/2/7/4/3274160/essig_5_questions_ajr2e122e9543.pdf>`_. AJR Am J Roentgenol 2013; 200:24-34.
    * Ferré J-C, Bannier E, Raoult H, et al. `Arterial spin labeling (ASL) perfusion: techniques and clinical use <http://www.mri-q.com/uploads/3/2/7/4/3274160/asl_review_1156841300209x_1-s2.0-s221156841300209x-main.pdf>`_. Diagn Interv Radiol 2013; 94:1211-1223
    * Jahng G-H, Li K-L, Ostergaard l, Calamante F. `Perfusion magnetic resonance imaging: a comprehensive update on principles and techniques <http://www.mri-q.com/uploads/3/2/7/4/3274160/perfusion_review_article_kjr-15-554.pdf>`_. Korean J Radiol 2014; 15:554-577. (good recent review).
    * McGehee BE, Pollock JM, Maldjian JA. `Brain perfusion imaging: how does it work and what should I use <http://www.mri-q.com/uploads/3/2/7/4/3274160/mcgehee_whitlow_review.pdf>`_? J Magn Reson Imaging 2012; 36:1257-1272.

**相关问题**
	* `What is arterial spin labeling (ASL) and how does it improve MRA? <http://www.mri-q.com/mra-with-asl.html>`_  
	* `Can you briefly explain the difference between the various ASL methods? Which is the best? <http://www.mri-q.com/asl-methods-overview.html>`_  