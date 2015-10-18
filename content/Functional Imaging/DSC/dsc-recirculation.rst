Question-DSC再循环效应：为什么DSC曲线在对比剂通过后不能恢复到基线？
======================================================================

:date: 2015-10-19
:tags: Perfusion, DSC
:slug: dsc-recirculation
:authors: Chunshan
:summary: DSC曲线在对比剂通过后不能恢复到基线

原文链接:\ `Why doesn't the DSC curve return to its baseline after passage of the contrast bolus? <http://www.mri-q.com/dsc-recirculation.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/873392_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6149570_orig.png?316
   :alt: Blood-brain Barrier
   :align: left
   :width: 600

   DSC灌注研究中总观测信号的成分：团注首过（早）和再循环效应（晚）

当钆造影剂通过组织时，T2/T2*失相位，MR信号强度随之降低，占主导地位的负峰主要反映的是钆造影剂首次通过局部动脉循环时的情况。然而很快，第二波钆造影剂会穿过组织，影响了第一峰的大小和时间。这第二波表示含钆血的再循环，血液分流通过肾脏、冠脉循环后又返回心脏。除了影响主峰，再循环也防止DSC信号恢复到原来的基线。

研究者经常采用不同的数学方法校正或补偿DSC数据中的再循环效应。最常用的方法之一是使用伽马变量拟合，伽马变量函数与上图中团注首过红色动脉曲线类似，有比较陡峭并且较大幅度的下坡，然后逐渐回到基线。其他校正这些效应的方法有单室再循环和随机模型。

**高级讨论**

To be updated

**参考材料**
    * Boxerman JL, Rosen BR, Weisskoff RM. `Signal-to-noise analysis of cerebral blood volume maps from dynamic NMR imaging studies <http://www.mri-q.com/uploads/3/2/7/4/3274160/boxerman_jmri_1997.pdf>`_. J Magn Reson Imaging 1997; 7:528-37. (Disadvantages of gamma variate fitting).
    * Patil V, Johnson G. `An improved model for describing the contrast bolus in perfusion MRI <http://www.mri-q.com/uploads/3/2/7/4/3274160/gamma_variate_fitting_dsc.pdf>`_. Med Phys 2011; 38:6380-3. (An alternative to gamma variate fitting, the single compartment recirculation (SCR) model).
    * Thompson HK Jr, Starmer CF, Whalen RE, McIntosh HD. `Indicator transit time considered as a gamma variate <http://www.mri-q.com/uploads/3/2/7/4/3274160/gamma_variate_1964.pdf>`_. Circ Res 1964; 14:502-515. (Original classic paper describing gamma variate fitting in indicator dilution experiments)

**相关问题**
	* `Question-注钆效应：在常规MR增强图像中钆对比剂用于增强信号，为什么在DSC灌注图像中信号减弱? <http://chunshan.github.io/MRI-QA/dsc/bolus-gd-effect.html>`_  