Question-电介质伪影：什么是介电效应？它如何产生磁共振成像中的伪影？
======================================================================================================

:date: 2015-11-28
:tags: MR Artifacts, tissue related artifacts
:slug: dielectric-effect
:authors: Chunshan
:summary: 电介质伪影

原文链接:\ `What is the dielectric effect and how does it produce artifacts in MRI? <http://www.mri-q.com/dielectric-effect.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/4847218_orig.png
    :alt: summary
    :align: center
    :width: 700

在MRI中，我们通常关注B0场和B1场，而常常忘记与磁场共生的一直存在的电场（E）。如在Maxwell方程中描述的，磁场（B场）和电场（E场）振荡的方向互相垂直，而且都垂直于波传播的方向。当电磁波遇到人体，会发生几个现象：1）波长变短，2）产生电流，3）在组织交界处产生反射波或折射。介电效应是指物体与电磁场中的电场（E）之间的相互作用。

由B1场不均匀性导致的异常明亮或黑暗区域在超高场（3.0T及以上）时经常出现，虽然这些伪影的本质还不是完全清楚，它们通常被称为电介质伪影。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/7833466_orig.jpg    | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/5430497_orig.jpg?310 |
|    :alt: "Dielectric" artifact at 7.0T                                        |    :alt: "Dielectric" artifact at 3.0T                                         |
|    :width: 300                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
|    7.0T下的电介质伪影，脑部中心区域异常明亮                                   |    3.0T下的电介质伪影。腹部（有腹水）中心区域异常昏暗                          |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/2610674_orig.jpg?282
   :alt: RF wavelengths in tissue as a function of field strength.
   :align: left
   :width: 400

   组织中的射频波长是磁场强度的函数

介电共振能够导致的亮区和暗区的程度仍然是有争议的。有相对高电导率的组织会引入一个“趋肤深度”的术语，产生阻尼驻波现象。中央明亮的现象已经在高电导率的水模中（其中的介电共振最小）得到验证。总之，介电效应及与之关联的伪影随着磁场强度的升高越发显著，虽然简单的介电诱导的驻波模型可能仅能解释一小部分现象。

**高级讨论**

物质与电磁场交互的程度可以通过三个参数描述：磁导率（μ），介电常数（ε），电导率（σ）。在一般情况下，这些参数随温度，电磁频率，和物质的物理状态而变化。而且因为它们还可能随位置和方向有关，因此一般更准确得表示为向量（张量）而不是标量。尽管如此，为了简单的解释，我只用希腊符号来表示，而不涉及它们更复杂的性质。


磁导率（μ）反映物质集中或分散外加磁场的程度。它与磁化率（χ）这个我们已经熟悉的概念几乎同义，通过关系μ = 1 + χ相联系。

介电常数（ε）是一种电气特性，与磁导率（μ）同源。它反映物质集中或分散外加电场的程度。高介电常数意味着当放置在电场中时，材料会变得更加极化。Permittivity（介电常数）与dielectric constant（介电常数）往往是同义词，后者是更古老的术语，已经逐渐不被使用了。

电导率（σ）反映材料携带电流的能力。电导率与电阻成反比。

弱导电介质材料（如人体）内部的射频磁场受传导电流通量（JC）和位移电流通量（JD）扰动，可以通过Maxwell校正后的Ampère定律描述：

ΧB = μJC + μJD = μσE + iωεE

其中，i2 = -1是复数单元，引入了传导电流和位移电流之间90°的相位偏移。传导电流和位移电流幅值之间的比例为：

JC /JD = σ / ω ε

人体组织中，在MRI中使用的射频频率，JC和JD的幅值在相同的量级。随着频率的升高，JD变得越来越重要，但即使在7.0T下（3000MHz），传导电流/位移电流的比例对脂肪，灰质，肌肉和脑脊液分别约为0.4，0.6，0.7和1.7。高介电材料（如在绝缘垫中使用的材料）传导电流/位移电流的比例仅为约0.01，意味着传导电流可以被忽略。

**参考材料**
     * Collins CM, Liu W, Schreiber, et al. `Central brightening due to constructive interference with, without, and despite dielectric resonance <http://www.mri-q.com/uploads/3/4/5/7/34572113/collins_central_brightening.pdf>`_. J Magn Reson Imaging 2005; 21:192-6.
     * Gabriel C, Gabriel S, Corhout E. `The dielectric properties of biological tissues: I. Literature survey <http://www.mri-q.com/uploads/3/4/5/7/34572113/the_dielectric_properties_of_biological_tissues_.1._literature_survey.pdf>`_. Phys Med Biol 1996;41:2231-2249.    
     * Webb AG, Collins CM. `Parallel transmit and receive technology in high-field magnetic resonance neuroimaging (pdf) <http://www.mri-q.com/uploads/3/4/5/7/34572113/201003_parallel_transmit_and_receive_technology_in_high-field_magnetic_resonance_neuroimaging.pdf>`_. Int J Imaging Syst Technol 2010; 20:2–13.

**相关问题**
	* `如何减少电介质伪影？绝缘垫用于解决这个问题的效果如何? <http://chunshan.github.io/MRI-QA/tissue-related-artifacts/dielectric-pads.html>`_