Question-DSC信号与钆：DSC中，能够从采集信号中得到量化的钆浓度实际值么？
==============================================================================

:date: 2015-10-21
:tags: Perfusion, DSC
:slug: dsc-signal-v-gd
:authors: Chunshan
:summary: 从采集信号中如何得到量化的钆浓度实际值

原文链接:\ `What parameters can be extracted from the DSC intensity curve? <http://www.mri-q.com/dsc-curve-analysis.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5135509_orig.png
    :alt: summary
    :align: center
    :width: 700

在前面的Q&A中，我们已经阐述了随着钆造影剂团的通过，T2*加权的DSC图像中MR信号强度如何降低。从这些原始数据中，一些有用的半定量参数可以提取出来，例如达峰时间（反映血流量）。为了从该数据提取更精确的和有意义的生理信息，第一步是将信号强度信息转换为实际钆浓度。

通常使用的从信号强度到钆浓度的转换假设钆浓度[Gd]正比于观察到的T2*弛豫率（ΔR2* = 1/ΔT2*）的改变，也就是正比于相对信号强度的负对数。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/1703874_orig.png?216
   :alt:  relationship between [Gd] and T2*-relaxation rate
   :align: center
   :width: 400

这里的So是给定体素的基线信号强度，St 是钆对比剂团通过时时刻t的信号强度。这个方程的推导在高级讨论中给出。

信号强度与钆浓度之间的转换本质上是一个对数变换，从一个商业灌注软件中得到如下的图示。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3992770_orig.gif
   :alt: signal intensity versus time curve
   :align: center
   :width: 600

   DSC信号强度随时间变化的曲线（原始数据）

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/2287116_orig.gif
   :alt: concentration curve
   :align: center
   :width: 600

   变换后的浓度曲线，用伽马变量函数拟合

**高级讨论**

下面是上文提到的钆浓度[Gd]和信号强度转换方程的简要推导。

根据造影剂生理浓度的简化理论，观察到的弛豫率改变(ΔR2=1/ΔT2 and ΔR2*=1/ΔT2*) 与钆浓度[Gd]线性相关，因此测量对比剂团通过时一个体素的弛豫率改变，此位置任意时刻的钆浓度可以近似计算出来。

回想一下，DSC实验中的信号（S）由一个简单的梯度回波序列产生，强度随时间指数衰减，表示如下：
    S = k e−TE/T2* = k e−TE•R2*

其中k是常量，由组织相关属性（如T1, ρ, χ）和技术参数（如Bo, TR, NEX, α）共同决定。通过对方程两边取对数并重排，R2*可以计算出来。
    ln(S/k) = − TE • R2*
    R2* = − (1/TE) • ln(S/k)

在钆造影剂团到达前，我们假设组织体素的初始弛豫率为R2*o，信号强度为So。在造影剂通过的时刻t时，我们假设弛豫率升高至 R2*t，信号强度下降为St，也就是
    R2*o = − (1/TE) • ln(So /k)
    R2*t = − (1/TE) • ln(St /k)
    
R2*的改变正比于钆浓度，可以写为：
    ΔR2* = R2*t − R2*o = − (1/TE) • [ ln(St /k) – ln(So /k) ]

使用对数的定义 ln(A) − ln(B) = ln(A/B) ，重写最后一个方程为：
    ΔR2* = − (1/TE) • ln(St /So)

弛豫率的改变与钆浓度成正比这一主要假设可能会被质疑，具体上讲，这样的线性关系仅对稀释匀质水溶液，并且使用自旋回波脉冲序列时成立。

**参考材料**
    * Kiselev VG. `On the theoretical basis of perfusion measurements by dynamic susceptibility contrast MRI <http://www.mri-q.com/uploads/3/2/7/4/3274160/kiselev2001_perfusion.pdf>`_. Magn Reson Med 2001; 46:1113-1122.
    * Østergaard L, Johannsen P, Host-Poulsen P, et al. `Cerebral blood flow measurements by magnetic resonance imaging bolus tracking: comparison with [15O]H2O positron emission tomography in humans <http://www.mri-q.com/uploads/3/2/7/4/3274160/ostergard_compare_dsc_to_o15.pdf>`_. J Cerbral Blood Flow Metab 1998; 18:935-940. (Early paper showing good agreement between DSC and PET measurements of cerebral blood flow. However, the MR data had to be "calibrated" to absolute flow rates measured by PET, meaning that absolute quantification of CBF by DSC alone was not possible).
    * Simonsen CZ, Østergaard L, Smith DF, et al. `Comparison of gradient- and spin-echo imaging: CBF, CBV, and MTT measurements <http://www.mri-q.com/uploads/3/2/7/4/3274160/simonsen_cz_et_al_j_mag_res_imaging_2000.pdf>`_. J Magn Reson Imaging 2000; 12:411-416. (spin-echo techniques may be more accurate than GRE for quantification of microvascular flow)

**相关问题**
	* `What is meant by the relaxivity of a contrast agent? How is it measured? <http://www.mri-q.com/what-is-relaxivity.html>`_ 
	* `Question-注钆效应：在常规MR增强图像中钆对比剂用于增强信号，为什么在DSC灌注图像中信号减弱? <http://chunshan.github.io/MRI-QA/dsc/bolus-gd-effect.html>`_     