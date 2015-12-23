Question-DCE参数：从DCE数据中能够提取哪些量化参数？
======================================================================================

:date: 2015-10-29
:tags: Perfusion, DCE
:slug: dce-tissue-parmeters
:authors: Chunshan
:summary: 从DCE数据中能够提取哪些量化参数

原文链接:\ `What quantitative parameters can be extracted from the DCE data? <http://www.mri-q.com/dce-tissue-parmeters.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/7776115_orig.png
    :alt: summary
    :align: center
    :width: 700

DCE原始数据被转换为钆造影剂浓度后，下一步是确定一个用于数据拟合的组织模型。比较简单而且广泛使用的模型是由Paul Tofts和他的同事们提出的，说明如下。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5463119_orig.gif
   :alt: Tofts Model
   :align: left
   :width: 500

   Tofts模型。图中细胞外空间相对于不含钆的细胞内空间（深蓝色）有些夸大。此外，血浆体积分数（vp，米色）一般比细胞外血管外空间的体积分数（Ve，浅蓝色）小得多。

在Tofts模型中，每个体素包含三种成分：组织实质细胞（深蓝色），血管（含红细胞和血浆），组织的细胞外血管外空间（EES）。钆造影剂在刚刚注射后是在血浆中的，由于浓度梯度的存在，会通过血管内皮细胞被动扩散到细胞外血管外空间（EES）。钆的容积转移常数（Ktrans）依赖于血流，血管表面积，和血管通透性。与Ktrans相关的速率常数 kep表示从细胞外血管外空间返流回血浆的速率。钆造影剂不进入细胞，所以它的浓度取决于血浆体积分数（vp）和EES的体积分数 (ve) ，这两个体积分数都是无量纲的，在图中有标示。

Tofts 模型有两个基本的数学公式（见下面高级讨论）。第一个公式假设血浆体积分数（Vp）比较小，对总组织的磁共振信号贡献比较小。Tofts模型的第二个公式包含了血浆的贡献，这增加了复杂性，但是可能更适合表示严重血管病变的情况，如恶性肿瘤。Tofts模型中DCE参数的意义和实际使用将在后续几个Q&A中进行探索。

**高级讨论**

**使用Tofts模型进行药代动力学分析**

最初的Tofts-Kermode模型（1991年）假设组织中钆造影剂的平衡浓度Ct仅由血浆中造影剂浓度（Cp）与细胞外血管外组织中造影剂浓度（Ce）差异导致的简单被动扩散驱动。由于钆造影剂不进入细胞，Ce比Ct高了1/Ve，Ve（0<Ve<1）是细胞外血管外空间（EES）组织的无量纲体积分数。Tofts-Kermode方程定义如下：

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/1551089.png?330
   :alt: Tofts-Kermode equation 
   :align: center
   :width: 500

其中Ktrans 是容积转移常数，单位是min−1。该方程的右边可以重写为：

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8400810_orig.png?481
   :alt: Tofts-Kermode equation 
   :align: center
   :width: 500

其中， kep 定义为Ktrans/ve，表示造影剂从EES返流回血浆的速率。Ktrans, ve, 和 kep互相联系，并不是完全互相独立的参数。如果已知其中两者，可以算出第三者。
在DCE检查中，我们可以控制血浆中随时间变化的钆造影剂浓度（Cp），使用动脉输入函数（AIF）表示，或者使用双指数衰减估计的AIF表示，双指数衰减的的初始值从肾脏清除率和整个身体的细胞外空间分布得到。另外，通过测量组织的信号强度，我们可以确定组织中钆造影剂浓度，Ct。Ktrans和ve是未知的，但是这些事潜在的重要生理学参数，可以通过将测量数据拟合到Tofts模型上进行估计。

最初的Tofts-Kermode模型假设组织中钆的总浓度可以忽略血管内钆的贡献。换句话说，血浆体积分数Vp非常小，在分析中可忽略。因此简单的TK模型只有两个自有参数，这个微分方程可以通过积分解决，

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8960309_orig.png?305
   :alt: Tofts-Kermode equation 
   :align: center
   :width: 500

对逐个像素使用非线性最小二乘估计，可以加计算出Ktrans和ve。

上述公式假定组织中钆的总浓度可以忽略血管内钆的贡献，Ct仅仅由EES中的钆得到。尽管这对某些病变是成立的，如多发性硬化斑块和低级别肿瘤，但对许多恶性肿瘤和其他严重血管病变并不成立。

对原始Tofts模型的修改通常就是将血管的贡献考虑在内，引入一个新的参数Vp，含血浆组织的体积分数。与Ve一样，Vp是无量纲的，因为它表示组织每单位体积中的血浆容量。扩展后的Tofts模型现在有两部分，含3个参数，用下面这个引入了新术语（VpCp）的方程表示。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/2151624_orig.png?372
   :alt: Tofts-Kermode equation 
   :align: center
   :width: 500

应当指出的是模型中增加更多的自由参数并不一定能够改进此模型，它需要更多的数据点来估计多出来的变量。非线性最小二乘拟合算法已经有些不稳定和病态，可能受到更多噪声的干扰从而收敛到不切实际的值。

**其他用于DCE成像的组织模型**

在Tofts和Kermode（英国）研究药代动力学模型的同时，Brix和他的同事（德国）也研究出了一个药代动力学模型。最初的Brix公式（现在已扩展）是一个中央（血管/血浆）和外周（组织细胞外空间）的开放-交换模型。钆在两者之间正向和反向的交换速率分别表示K12和K21，与Tofts模型中的Ktrans和Kep大致对应。然而，Brix模型明确将血流从渗透效应中分离出来（在Ktrans概念中二者是混在一起的）。最初的Brix模型根据信号改变的比例计算钆浓度，这是一个相对不太准确的方法，但是也有优点，这种方法不需要扫打造影剂之前的T1 Mapping序列，也不需要测量动脉输入函数。

分布参数模型，也被成为组织同质化模型，摒弃了Tofts模型和Brix模型中使用的钆造影剂在组织中“充分混合”的概念，而是假设沿每根毛细血管存在钆浓度梯度，这需要将传输时间纳入模型，但此模型有直接从分析中提取血流信息的潜力。

**参考材料**
    * Brix G, Semmler W, Port R, et al. `Pharmacokinetic parameters in CNS Gd-DTPA enhanced MR imaging <http://www.mri-q.com/uploads/3/2/7/4/3274160/brix_pharmacokinetic_parameters_in_cns_gd_dtpa_enhanced.18.pdf>`_. J Comput Assist Tomogr 1991; 15:621-628.
    * Tofts PS. `Modeling tracer kinetics in dynamic Gd-DTPA MR imaging <http://www.mri-q.com/uploads/3/2/7/4/3274160/b103_tofts-modeling-jmri1997.pdf>`_. J Magn Reson Imaging 1997; 7:91-101.      
    * Tofts PS, Brix, G, Buckley DL, et al. `Estimating kinetic parameters from dynamic contrast-enhanced T1-weighted MRI of a diffusable tracer: standardized quantities and symbols <http://www.mri-q.com/uploads/3/2/7/4/3274160/tofts_et_al-1999-journal_of_magnetic_resonance_imaging.pdf>`_. J Magn Reson Imaging 1999; 10:223-232. 
    * Tofts PS, Kermode AG. `Measurement of the blood-brain barrier permeability and leakage space using dynamic MR imaging. 1. Fundamental concepts <http://www.mri-q.com/uploads/3/2/7/4/3274160/b48_toftsandkermode-mrm1991.pdf>`_. Magn Reson Med 1991; 17:357-367
    * Zaharchuk G. `Theoretical basis of hemodynamic MR imaging techniques to measure cerebral blood volume, cerebral blood flow, and permeability <http://www.mri-q.com/uploads/3/2/7/4/3274160/ajnr_zharchuk_perfusion_review.pdf>`_. AJNR Am J Neuroradiol 2007; 28:1850-8.

**相关问题**
	* `Is Ktrans the same as permeability？ <http://www.mri-q.com/parameters-to-images.html>`_  
	* `How do calculated DCE parameters relate to patterns of enhancement we see on clinical images? <http://www.mri-q.com/parameters-to-images.html>`_  