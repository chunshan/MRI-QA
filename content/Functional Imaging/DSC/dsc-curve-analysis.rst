Question-半定量参数：从DSC时间强度曲线中能够提取什么参数？
======================================================================

:date: 2015-10-20
:tags: Perfusion, DSC
:slug: dsc-curve-analysis
:authors: Chunshan
:summary: 从DSC时间强度曲线中能够提取的参数

原文链接:\ `What parameters can be extracted from the DSC intensity curve? <http://www.mri-q.com/dsc-curve-analysis.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5135509_orig.png
    :alt: summary
    :align: center
    :width: 700

一些半定量灌注参数可以通过分析对比剂通过时各个体素的DSC信号强度曲线得到，这些参数很容易计算，因此被广泛使用。但是它们缺乏准确度和一致性，高度依赖于对比剂的有效性/紧凑性。这些参数的绝对值本身没有多大意义，但相对意义是有用的（如对大脑两侧比较对应区域）。这些被称为“摘要”参数的最常见几个在下面给出图示和定义。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5742607_orig.png?637
   :alt: semiquantitative analysis of DSC signal intensity curves
   :align: center

   简化的DSC信号强度曲线半定量分析

1. 到达时间（AT，Arrival Time）是从静脉注射造影剂到第一次在组织（或一个大的供血动脉）中被检测到的时间间隔。MR信号由于噪声和运动而随机变化，必须取对比剂到达前的十几个甚至更多时间点的平均作为基线，然后可以任意设置一个检测阈值（例如，低于基线5%）定义对比剂的到达。或者，该阈值可以通过观察信号强度曲线而手动设置。尽管AT可以计算，但它反映的是影响对比剂到达组织的所有因素（喷射率，心输出量，局部血流量等）的总和。大脑两侧对比剂到达时间明显不同可能预示单侧颈动脉狭窄。

2. 达峰时间（TTP，Time to Peak）通常被定义为从开始注射对比剂到感兴趣器官信号损失到达峰值（最大）的时间间隔。TTP与AT有相同的用处和局限，但是峰值非常容易识别，不需要设置对比剂首次到达的检测阈值，TTP较AT有一定的优越性。一些软件应用中，TTP不包括到达时间，被定义为首次检测到对比剂和信号损失峰值之间的时间间隔。

3. 负性增强积分（NEI，Negative Enhancement Integral）表示钆首次通过的信号强度下总面积（“积分”），有时候也被成为曲线下面积（AUC，Area Under Curve）。NEI表示穿过局部血管系统的对比剂总量，大致与血容量成正比。由于再循环效应，前面Q&A中解释过，基线在对比剂首过后不会恢复正常，为了处理基线漂移，必须要对积分的右方极限进行处理。通常会使用信号强度曲线的数学模型（如伽马变量函数）校正再循环和基线漂移效应，从而使NEI计算更有一致性。

4. 平均增强时间（MTE，Mean Time to Enhance）表示注射的全部造影剂团穿过组织区域的平均时间。MTE的绝对值高度依赖于到达的对比剂团的形状（紧凑性），其次是灌注的组织。MTE虽然经常与MTT（Mean Transit Time）混淆，要认识到MTE与MTT（平均通过时间）并不相同，MTT反映的是单个对比剂分子（不是整个对比剂团）穿过组织的平均时间。在模拟实验中，MTE可能比真正的MTT长3倍。不同的制造商对MTE可能有略微不同的名字，计算方法也不太相同，或者采用NEI的一阶矩（质心），或者采用信号强度曲线的半高全宽（FWHM）。一些软件应用还提供了使用这些数据，计算相对血流量（rBF）的简单方法，NEI/MTE，作为对真实血流量（BF = BV/MTT）的模拟，但是这种方法有比较明显的局限性和错误。

5. 基线峰值百分比（Percent Baseline at Peak）和信号恢复百分比（Percent Signal Recovery）分别被定义为信号强度的最小值（峰值）或再循环阶段（恢复）的强度值除以基线值得到的比值。这两个值虽然容易计算，但是受实验和生理现象同时影响，因此很少使用。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/274231_orig.gif?608
   :alt: Time-to-peak (TTP, left) and negative enhancement integral (NEI, right)
   :align: center

   达峰时间（TTP，左）和负性增强积分（NEI，右），根据一个DSC实验中逐个像素的首过信号强度曲线计算得到。虽然它们的绝对值没有意义，但是很容易计算，相对意义上比较大脑相应区域的灌注情况是有用的。

为了得到更多量化的参数图如血流量和血容量，需要进行更复杂的数学处理。这是后续几个Q&A的主题。

**参考材料**
    * Jahng G-H, Li K-L, Ostergaard l, Calamante F. `Perfusion magnetic resonance imaging: a comprehensive update on principles and techniques <http://www.mri-q.com/uploads/3/2/7/4/3274160/perfusion_review_article_kjr-15-554.pdf>`_. Korean J Radiol 2014; 15:554-577.
    * McGehee BE, Pollock JM, Maldjian JA. `Brain perfusion imaging: how does it work and what should I use <http://www.mri-q.com/uploads/3/2/7/4/3274160/mcgehee_whitlow_review.pdf>`_? J Magn Reson Imaging 2012; 36:1257-1272.
    * Perthen JE, Calamante F, Gadian DG, Connelly A. `Is quantification of bolus tracking MRI reliable without deconvolution <http://www.mri-q.com/uploads/3/2/7/4/3274160/perthen_2002_mrm.pdf>`_? Magn Reson Med 2002; 47:62-67. (The answer is NO).
    * Welker K, Boxerman J, Kalnin A, et al. `ASFNR recommendations for clinical performance of MR dynamic susceptibility contrast perfusion imaging of the brain <http://www.mri-q.com/uploads/3/2/7/4/3274160/white_paper_asfnr_on_dsc_ajnr.a4341.full.pdf>`_. AJNR Am J Neuroradiol 2015; 36: E41-E51.

**相关问题**
	* `Question-DSC：如何做一个DSC灌注研究？ <http://chunshan.github.io/MRI-QA/dsc/how-to-perform-dsc.html>`_