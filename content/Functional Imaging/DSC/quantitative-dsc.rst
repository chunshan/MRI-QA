Question-DSC高级处理：如何使用动脉输入函数从DSC数据中提取更多量化的血流信息？
======================================================================================


:date: 2015-10-23
:tags: Perfusion, DSC
:slug: quantitative-dsc
:authors: Chunshan
:summary: DSC高级处理，使用动脉输入函数从DSC数据中提取更多量化的血流信息

原文链接:\ `How is the arterial input function used to extract more quantitative flow information from the DSC data? <http://www.mri-q.com/quantitative-dsc.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/235069_orig.png
    :alt: summary
    :align: center
    :width: 700

原始的DSC成像数据转化为定量的血流量测量值有三个步骤：
1. 将组织的MR信号s(t)转换为钆造影剂浓度c(t)；
2. 选择合适的动脉输入函数a(t)；
3. 数学建模和计算。

前两个步骤已经在前面的Q&A中有描述。本部分将介绍在知道c(t)和a(t)情况下如何计算血流信息的数学方法，这些分析基于线性系统理论，并且需要几个重要的假设。
1. 血流量（F）和血容量（V）在测量期间是常量；
2. 注射的所有示踪剂分子最终都会从系统中流出，换句话说，没有持久的陷阱或血池，组织内也没有示踪剂损失。
3. 系统对输入的响应是线性的并且遵循叠加原理。也就是说，两个独立输入的总输出响应与分别考虑这两个输入的响应再求和是一样的。

注：读者很快就会意识到这个简单的模型在实际中可能会失效。例如，血脑屏障泄露时脑肿瘤会聚集钆对比剂，这不满足假设2.

血容量（V）是第一个也是最容易提取的参数。假设没有泄露和再循环的影响，血容量与造影剂首次通过时组织浓度曲线c(t)下方的面积成正比。理论上，这种关系可以通过除以仅含血液的体素的钆造影剂浓度进行定量。通常选择一条供血动脉内的体素作为参考体素，也就是可以选择动脉输入函数的曲线a(t)。CT灌注研究中通常也会用大静脉中的一个体素作为参考体素。数学关系如下：

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/9722550_orig.png?171
   :alt:  calculation of blood volume
   :align: center
   :width: 300

血流量是（F）下一个可被计算的参数，但是这个计算过程有点“绕”。理解这个方法需要首先简要介绍一下线性系统理论。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/2297065_orig.png?399
   :alt:  linear system
   :align: right
   :width: 400

对线性系统（如组织的毛细血管床）进行分析，可以考虑它对一个假设的无限高强度，无限短时间的脉冲（狄拉克函数， Dirac delta function δ(t)）的响应。对我们的系统而言，δ(t)可视为在t=0 时刻将造影剂分子通过一个动脉口瞬间团注入组织。注射后，一些分子会找到通往静脉口比较直接的路径，其他的分子则会选择更加迂回的路径，花更长的时间才能通过毛细血管床。这导致注射的对比剂团在组织中变得分散，对比剂分子的通过时间也不一致。

这样一个脉冲注入之后，注射的对比剂分子留在组织中的部分是t的无量纲函数，称为残留函数，记为R(t)。刚注射后（没有任何分子离开系统前）R(t)处于最大值R(0) = 1。随着对比剂分子流出系统，R(t)变小，最终达到终值R（∞）= 0，也就是对比剂不残留在组织中。

残留函数宽度反映的是对比剂分子通过组织时间的分布，通过时间短的组织的残留函数曲线比较窄且陡峭，相反，通过时间长的组织残留函数曲线比较宽。残留函数下的面积反映对比剂分子通过组织毛细血管床花的平均时间，这就是平均通过时间MTT（Mean Transit Time），是一个重要的生理参数。数学表达式为:

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4357256_orig.png?139
   :alt:  calculation of MTT
   :align: center
   :width: 300

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8142532_orig.png?399
   :alt: AIF & linear system
   :align: left
   :width: 600

   上图：实际的动脉输入函数AIF和相应的组织浓度曲线c(t)；下图：由一组狄拉克函数建模的组织响应

在实际中，不可能将动脉注射的对比剂瞬间递送到组织，动脉输入函数a(t)，时间上总是分散的，如图所示。但是这种普遍的动脉输入可以表示为一组延迟不同时间(τ)的狄拉克函数，每一个产生一个独立的响应。对这些独立的脉冲响应缩放并求和以求得组织对比剂浓度曲线c(t)的数学操作成为卷积。数学上表示为：

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3401680_orig.png?344
   :alt: convolution
   :align: center
   :width: 500

其中F表示血流量，符号是卷积操作子。卷积过程就是对每个加权（乘以注射后不同延迟时间(τ)的残留函数）的动脉输入求和（积分）。事实上钆造影剂仅分布于血管的细胞外空间，这个方程的一些形式会在F前包含一个常数因子(ρ/h)，其中ρ是组织密度，单位是g/mL，h表示毛细血管和大血管间红细胞容积比的差。

在DSC灌注实验中，a(t) 和 c(t) 可以直接测量得到，但是不知道血流量F和残余函数 R(t)。因为这个方程中未知数比已知数多，唯一解不存在。但是，有不同的数学方法可以合理估计这些参数，尤其是血流量(F)。

有三种通用的策略可进行数学上的反卷积运算。最常用的方法是将这个方程转换为矩阵形式，用奇异值分解（SVD，Singular Value Decomposition）做迭代运算。第二种不太常用的方法被称为“参数化”，因为这种方法假设残余函数有事先确定的形状，如衰减的指数形式。其他反卷积技术需要用到傅里叶变换或随机估计。

所有反卷积方法的最终结果就是对血流量(F)的量化估计。由于血容量(V)已经计算出来，最后的步骤是使用中心容积定律（Central Volume Theorem）逐个体素计算平均通过时间MTT， MTT = V/F。

应该指出的是，选取的AIF不同，或者使用的商业软件计算方法不同，所得结果会有明显的差异。即使软件声称使用相同的方法，相同的原始数据可能也会给出不同的结果。建议谨慎地依赖这些定量方法所获得的绝对数。

卷积（反卷积）概念对那些没有很强数学背景的人而言会比较困惑，但是我的同事Josh Shimony在这个\ `YouTube视频 <https://youtu.be/8MB7iZmsoUI>`_\ 中（离开头约33分钟）浅显易懂地介绍了这个概念。整个视频是对DSC和ASL很好的介绍，如果你有时间，我建议你全部看完它。

**高级讨论**

傅里叶方法用于反卷积，首先对求取血流量的卷积方程两边都进行傅里叶变换(FT, Fourier Transform)，这种方法根据的是著名的卷积定理，两个函数乘积的傅里叶变换是每个函数傅里叶变换的卷积。数学上表示为
    F • R(t) = FT−1{FT[c(t)] / FT[a(t)]}

注意残余函数的初始值为1（R(0) = 1），这个函数第一个时间点的幅度就等于血流量(F)。尽管概念上很直接，由于不稳定和噪声问题，这个方法并不常用。

最常用的奇异值分解（SVD， Singular Value Decomposition）方法也有许多变种。SVD是矩阵代数中一种常用的求解逆问题的分解方法。由于噪声和舍入误差SVD可能是病态的（不稳定），必须施加一些限制（正则化）。最直接的正则化方法（截断）是将所有低于一定水平的矩阵奇异值设为0。另一种正则化方法（Tikhonov 正则化）通过操纵对角线元素，从而对奇异值有更平滑的截断。

标准奇异值分解的第二个问题是结果对组织不同部分之间的对比剂到达延迟非常敏感。诸如reformulated SVD和block-recirculant SVD很大程度上可以克服这些限制，逐渐被软件制造商在他们的软件中实现。

一些较新的统计学方法更侧重提高残余函数的估计，减少其震荡。哪一种方法更具优势，现在还不好预测。

我为什么不喜欢T\ :sub:`max`\ 

在中风文献中，大量临床试验使用一种称为T\ :sub:`max`\ 的灌注度量参数，T\ :sub:`max`\ 被定义为残留函数R(t)到达最大值的时间，残留函数R(t)从反卷积中计算得到。理论上，Tmax是动脉输入函数（AIF）峰值与残留函数峰值之间的时间。

T\ :sub:`max`\ 与MTT不同。MTT反映的是造影剂达到感兴趣组织后通过毛细血管床的时间。相反，T\ :sub:`max`\ 反映造影剂从测量AIF到到达毛细血管系统途中的延时和分散。

T\ :sub:`max`\ 高度依赖AIF的选择位置。AIF位置离感兴趣组织越远，计算得到的T\ :sub:`max`\ 值会越大。另外，矩阵奇异值分解（SVD）的正则化（滤波）可以通过产生震荡和峰值位移改变R(t)，从而减少反卷积中噪声的影响，这个过程也会影响T\ :sub:`max`\。

尽管T\ :sub:`max`\ 有些方法上的问题，许多中风神经学家似乎喜欢T\ :sub:`max`\ 并且推荐在临床实践中使用这个参数。我相信它如此受欢迎的原因之一是T\ :sub:`max`\ 参数图在脑的正常区域图像对比度相对比较“平”，而在低灌注或临界区域图像对比度有显著不同。

总之，T\ :sub:`max`\ 确实提供了一些对MTT和CBF互补的信息，但是这是一个“混乱”的参数，反映的是选择的AIF位置到感兴趣组织间造影剂的延迟和分散。因此它是非常依赖于AIF的选择，在比较不同患者的脑卒中研究中应谨慎使用。

**参考材料**
    * Boxerman JL, Rosen BR, Weisskoff RM. `Signal-to-noise analysis of cerebral blood volume maps from dynamic NMR imaging studies <http://www.mri-q.com/uploads/3/2/7/4/3274160/boxerman_jmri_1997.pdf>`_. J Magn Reson Imaging 1997; 7:528-37.
    * Calamante F, Christensen S, Desmond PM, et al. `The physiological significance of the time-to-maximum (Tmax) parameter in perfusion MRI <http://www.mri-q.com/uploads/3/2/7/4/3274160/stroke_tmax-2010-calamante-1169-74.pdf>`_. Stroke 2010; 41:1169-1174. (See Advanced Discussion tab for why I don't favor this parameter in practice.)
    * Fieselmann A, Kowarschik M, Ganguly A, et al. `Deconvolution-based CT and MR brain perfusion measurement: theoretical model revisited and practical implementation details <http://www.mri-q.com/uploads/3/2/7/4/3274160/review_perfusion_467563.pdf>`_. Int J Biomed Imag 2011; doi:10/1155/2011/467563
    * Orsingher L, Piccinini S, Crisi G. `Differences in dynamic susceptibility contrast MR perfusion maps generated by different methods implemented in commercial software <http://www.mri-q.com/uploads/3/2/7/4/3274160/differences_in_dynamic_susceptibility_contrast_mr.4.pdf>`_. J Comput Assist Tomogr 2014; 38:647-654. (different software gives different results, even when methods are said to be the same!)
    * Østergaard L, Weisskoff RM, Chesler DA, et al. `High resolution measurement of cerebral blood flow using intravascular tracer bolus passages. Part I. Mathematical approach and statistical analysis <http://www.mri-q.com/uploads/3/2/7/4/3274160/ostergaard_svd.pdf>`_. Magn Reson Med 1996; 36:715-725. (good description of deconvolution techniques including Fourier and SVD).
    * Zaharchuk G. `Theoretical basis of hemodynamic MR imaging techniques to measure cerebral blood volume, cerebral blood flow, and permeability <http://www.mri-q.com/uploads/3/2/7/4/3274160/ajnr_zharchuk_perfusion_review.pdf>`_. AJNR Am J Neuroradiol 2007; 28:1850-8.

**相关问题**
	* `Question-动脉输入函数（AIF）：动脉输入函数是什么，为什么需要测量动脉输入函数？ <http://chunshan.github.io/MRI-QA/dsc/arterial-input-aif.html>`_  
	* `Question-灌注参数：血流量（BF，Blood Flow），血容量（BV，Blood Volume），平均通过时间（MTT， Mean Transit Time）等参数是怎么定义的？在灌注成像中如何使用? <http://chunshan.github.io/MRI-QA/dsc/meaning_of_cbf_mtt_etc.html>`_  