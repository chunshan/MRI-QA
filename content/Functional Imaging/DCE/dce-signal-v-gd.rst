Question-DCE信号与钆浓度：如何根据DCE信号强度计算血液和组织中的钆浓度？
======================================================================================

:date: 2015-10-28
:tags: Perfusion, DCE
:slug: dce-signal-v-gd
:authors: Chunshan
:summary: 根据DCE信号强度计算血液和组织中的钆浓度

原文链接:\ `How is the concentration of gadolinium in blood and tissue determined from the DCE signal? <http://www.mri-q.com/dce-signal-v-gd.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3440651_orig.png
    :alt: summary
    :align: center
    :width: 700

完全量化的DCE研究第一步是根据MR信号强度计算组织中钆造影剂浓度[Gd]。该过程类似于DSC成像，T1弛豫率的改变ΔR1 (=1/ΔT1)，与[Gd]成正比。这个假设只在造影剂的稀释水溶液中是成立的，并不能严格适用于生物大分子之间的相互作用影响了弛豫或条块分割影响了水分子快速交换的组织。

通常的DCE脉冲序列时扰相梯度回波（FLASH/SPGR/T1-FFE），信号强度(S)由下式给出：

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/7502602_orig.png?348
   :alt: signal intensity 
   :align: center
   :width: 500

这里的k是一个比例常数，[H]是自旋密度，α是RF翻转角。信号强度与T1之间的关系不像在DSC中描述的那么直接，是一个简单对数比例关系，但关系仍然是确定的。计算的精度依赖于背景组织没有造影剂时的T1，这个T1值可以通过一个打造影剂前单独的校正序列得到，或者使用基于大样本的平均值。如果没有校正，从MR信号中只能得到相对的钆浓度。

最后，钆基造影剂分布在血浆中，而不是全部血液中，必须考虑有效的血浆浓度。全血中血浆的比例取决于红细胞容积比（Hct = 红细胞的百分比），有如下关系 [Gd]blood =  [Gd]plasma × (1−Hct)。对典型的正常红细胞容积比Hct = 40%，血浆中的造影剂浓度大约是基于全血测量的1.7倍。

注意，即使同一个病人，其红细胞容积比在不同时间也可能不同，尤其是正接受化疗的癌症患者。如果不做调整，变化的Hct 会显著影响不同时间进行的DCE量化测量。另一个在DCE计算中通常未被考虑的因素是毛细血管（钆造影剂交换发生）中的Hct 只是大一些动脉中的1/2或更少（Fåhraeus 效应）。

**高级讨论**

在心脏成像以及一些其他应用中，DCE成像可能使用饱和恢复（SR，Saturation Recovery）序列而不是扰相GRE序列。这种情况下，信号强度公式如下：
     S = k [H] (1 − e−TD/T1) e−TE/T2*

其中TD是90°脉冲和采集之间的延迟时间。

**参考材料**
    * Fåhraeus R, Lindqvist T. `The viscosity of the blood in narrow capillary tubes <http://www.mri-q.com/uploads/3/2/7/4/3274160/farhreus_1931.pdf>`_. Am J Physiol 1931; 96:562-568. (Classic paper demonstrating what is now known as the "Fåhraeus effect" - that hematocrit decreases strongly with reduced vascular size below about 0.3 mm diameter. This is because blood viscosity decreases and RBCs move more quickly than plasma down the center of capillaries.)
    * Parker GJM, Barker GJ, Tofts PS. `Accurate multislice gradient echo T1 measurement in the presence of non-ideal RF pulse shape and RF filed nonuniformity <http://www.mri-q.com/uploads/3/2/7/4/3274160/parker-mrm-2001-45-838pdf.pdf>`_. Magn Reson Med 2001; 45:838-845.      
    * Pries AR, Ley K, Gaehtgens P. `Generalization of the Fåhraeus principle for microvessel networks <http://www.mri-q.com/uploads/3/2/7/4/3274160/am_j_physiol_1986_pries.pdf>`_. Am J Physiol 1986; 251:H1324-H1332. 
    * Schabel MC, Parker DL. `Uncertainty and bias in contrast concentration measurements using spoiled gradient echo pulse sequences <http://www.mri-q.com/uploads/3/2/7/4/3274160/t1_estimation_nihms-59716.pdf>`_. Phys Med Biol 2008; 53:2345-2373.
    * Tofts PS. `T1-weighted DCE imaging concepts: modelling, acquisition and analysis <http://www.mri-q.com/uploads/3/2/7/4/3274160/dce-mri_siemens.pdf>`_. MAGNETOM Flash 2010; 3:30-35. 
    * Zaharchuk G. `Theoretical basis of hemodynamic MR imaging techniques to measure cerebral blood volume, cerebral blood flow, and permeability <http://www.mri-q.com/uploads/3/2/7/4/3274160/ajnr_zharchuk_perfusion_review.pdf>`_. AJNR Am J Neuroradiol 2007; 28:1850-8.

**相关问题**
	* `Question-DSC信号与钆：DSC中，能够从采集信号中得到量化的钆浓度实际值么？ <http://chunshan.github.io/MRI-QA/dsc/dsc-signal-v-gd.html>`_  
	* `Why would you want to use a spoiled-GRE technique?  How do you pick the parameters? <http://www.mri-q.com/spoiled-gre-parameters.html>`_  