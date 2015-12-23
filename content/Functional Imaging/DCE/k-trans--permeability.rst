Question-Ktrans & 渗透性  Ktrans是否等同于渗透性?
======================================================================================

:date: 2015-10-31
:tags: Perfusion, DCE
:slug: k-trans--permeability
:authors: Chunshan
:summary: Ktrans是否等同于渗透性

原文链接:\ `Is Ktrans the same as permeability? <http://www.mri-q.com/k-trans--permeability.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4882327_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/7177973_orig.gif
   :alt: Volume transfer rate of gadolinium
   :align: right
   :width: 500

   钆（黑点）进入组织的体积转移速率（Ktrans）依赖于血浆流量（F），渗透性（P）和血管表面积（S）

体积转移常数（Ktrans）反映钆造影剂从血浆进入血管外细胞外空间（EES）组织的流出速率。Ktrans取决于于三个因素：血浆流量（F），血管通透性（P）和单位质量的毛细血管表面积（S）。在实践中，渗透性和表面积分别的贡献不能清楚地分离出来，因此一般把它们一起考虑，即乘积PS。

如下图所示，两个有相同血流和PS乘积的毛细血管网络中，钆将会以相同的速率进入组织，即使它们的渗透性和表面积可能不同。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6387590_orig.gif?575
   :alt: Two different capillary networks with the same flows
   :align: center
   :width: 700

   两种有具有相同流量（F）和PS乘积的毛细血管网络有相同的Ktrans值

一般而言，F,P,S分别对Ktrans的贡献不能分开。然而，两种特殊情况可以揭示这三个因素相对的重要性及它们的相互作用。

* 情况1 （渗透性有限） 这种情况下（下面的左图），血浆流量（F）比PS乘积大得多。大量钆随血流传送到组织，但进入组织间隙的量仅取决于毛细血管床的大小和渗透性。这种情况下，Ktrans = P×S。
* 情况2 （流量有限） 这种情况下血浆流量比PS乘积小的多，所有钆在到达毛细血管床的静脉端之前几乎都泄露到EES，因而，Ktrans = F。

+---------------------------------------------------------------------------+----------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/1715352_orig.gif | .. figure::  http://www.mri-q.com/uploads/3/2/7/4/3274160/8239895_orig.gif |
|    :alt: Gd-enhanced T1-image of malignant glioma                         |    :alt: Ktrans map                                                        |
|    :width: 400                                                            |    :width: 400                                                             |
|                                                                           |                                                                            |
+---------------------------------------------------------------------------+----------------------------------------------------------------------------+

**高级讨论**

毛细血管渗透性的单位（cm/min）并不是那么显而易见的。渗透性（P）定义为由于浓度（moles/cm³）差的驱动，一段时间内（min）一种溶质通过给定面积（cm²）薄膜的摩尔数。因此该单位可以写为：

P = [moles]/[cm²]/[min]/[moles/cm³] = cm/min

同样，S并不表示毛细血管的表面积（单位cm²），而是表示“每单位质量组织中的表面积比例”。因此S通过面积/质量度量（比如，cm²/100g）。总起来，PS乘积的单位是 [cm/min]•[cm²/100g] = cc/min/100g，与流量（F）的单位是相同的。

**参考材料**
    * Cuenod CA, Balvay D. `Perfusion and vascular permeability: basic concepts and measurement in DCE-CT and DCE-MRI <http://www.mri-q.com/uploads/3/2/7/4/3274160/permeability_1-s2.0-s2211568413003306-main.pdf>`_. Diagn Interv Imaging 2013; 94:1187-1204. (Good review of basic mechanisms; some terminology is slightly different than abbreviations used in Tofts models).
    * Pappenheimer JR. `Passage of molecules through capillary walls <http://www.mri-q.com/uploads/3/2/7/4/3274160/pappenheimer_387.full.pdf>`_. Physiol Rev 1953; 33;387-423.       
    * Sourbron S, Ingrisch M, Siefert A, et al. `Quantification of cerebral blood flow, cerebral blood volume, and blood-brain-barrier leakage with DCE-MRI <http://www.mri-q.com/uploads/3/2/7/4/3274160/sourbron_et_al-2009-magnetic_resonance_in_medicine.pdf>`_. Magn Reson Med 2009; 62:205-217.
    * Tofts PS. `T1-weighted DCE imaging concepts: modelling, acquisition and analysis <http://www.mri-q.com/uploads/3/2/7/4/3274160/dce-mri_siemens.pdf>`_. MAGNETOM Flash 2010; 3:30-35. 
    * Zhang N, Zhang L, Qui B, et al. `Correlation of volume transfer coefficient Ktrans with histopathologic grades of gliomas <http://www.mri-q.com/uploads/3/2/7/4/3274160/zhangnihms365626.pdf>`_. J Magn Reson Imaging 2012; 36:355-363.

**相关问题**
	* `What quantitative parameters can be extracted from the DCE data? <http://www.mri-q.com/dce-tissue-parmeters.html>`_  
	* `How do calculated DCE parameters relate to patterns of enhancement we see on clinical images? <http://www.mri-q.com/parameters-to-images.html>`_  