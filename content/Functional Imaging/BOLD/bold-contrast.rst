Question-BOLD对比机制：BOLD fMRI的图像对比度是如何产生的？
==========================================================================

:date: 2016-03-03
:tags: BOLD
:slug: bold-contrast
:authors: Chunshan
:summary: BOLD对比机制

.. |br| raw:: html

   <br />

原文链接:\ `How is image contrast produced by BOLD fMRI? <http://mriquestions.com/bold-contrast.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4114370_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/980703_orig.gif?295
   :alt: Deoxyhemoglobin is strongly paramagnetic
   :align: right
   :width: 400

   由于以每个铁原子为中心有4个未成对电子，去氧血红蛋白呈强顺磁性

BOLD（Blood Oxygen Level Dependent）对比度产生于局部氧合血红蛋白和去氧血红蛋白浓度的改变。如在前一个Q&A中描述的，氧合血红蛋白没有未成对的电子，呈弱抗磁性，当氧气释放形成去氧血红蛋白时，4个未成对电子暴露在每个铁原子中心，使分子成为强顺磁性。BOLD效应与去氧血红蛋白的浓度直接相关，其浓度在动脉血中少于2%而在静脉血中高于40%。

大脑的局部T2和T2*弛豫时间随着去氧血红蛋白比例增加而降低。这种效应对MR信号的影响取决于场强（Bo），脉冲序列（SE或者GRE）和回波时间（TE）。无论上述何种技术，含更多氧合血红蛋白的大脑区域会比含更多去氧血红蛋白的区域信号强度更高（看起来更明亮）。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5991244_orig.png
   :alt: Paramagnetic deoxyhemoglobin
   :align: left
   :width: 300

   红细胞中顺磁性的去氧血红蛋白（D）\ |br|\ 导致血管内外局部磁场畸变

红细胞内顺磁性去氧血红蛋白的出现使得血管内外局部磁场畸变（磁敏感梯度）。这些局部磁场扭曲会导致附近静止和缓慢移动的质子有不同的共振频率和相位偏移。由此产生的像素内失相位是一种经典的T2*缩短效应，在大静脉附近最为显著，使用回波时间（TE）接近T2*的GRE序列会加剧这种效应。此效应与场强（B0）成线性关系，是1.5T下BOLD对比度的主要形成机制。

血管内去氧血红蛋白导致的局部磁场畸变也会影响在血管内外弥散的水分子中的质子。这些质子会受到随机改变的频率偏移的影响，其失相位是不可恢复的。这种弥散相关的T2信号损失在临近毛细血管的地方比稍微大一些的血管处更加显著，最好使用自旋回波技术（可以翻转由静磁场不均匀性导致的失相位）抑制此效应。真正的T2弥散效应与磁场强度的平方（Bo²）成正比，是4.0T或更高场强下BOLD对比度的主要机制（大多数临床fMRI检查使用3.0T，这种情况下T2和T2*效应对BOLD对比度的贡献相当）。

**高级讨论**

至少四种不同的机制会产生BOLD fMRI中的T2和T2*弛豫，下面的参考文献中可以找到对此更完整的描述。这可以分为血管内和血管外两部分，这两部分可以分开考虑因为两部分之间的交换速率比起成像时间（TE）而言非常慢。弥散效应非常重要，因为一个典型的fMRI实验过程中，在其成像间隔（TE ≈ 50 ms），水分子扩散的距离约为毛细血管直径的4倍。血管相对于B0的方向也必须考虑到。

稍低磁场（≤ 3.0T）和更高磁场（≥ 7.0T）中BOLD图像对比度的一个主要不同的机制在于血液和大脑由磁场强度不同导致的弛豫时间改变。1.5T下，动脉血和静脉血的T2分别为250ms和180ms，而白质和灰质的T2在70-100ms之间；7.0T下，相对的弛豫时间发生了逆转，血液的T2（T2*）与大脑相比变得非常短。

**参考材料**
     * Pauling L, Coryell CD. `The magnetic properties and structure of hemoglobin, oxyhemoglobin and carbonmonoxyhemoglobin. <http://mriquestions.com/uploads/3/4/5/7/34572113/pnas-1936-pauling-210-6.pdf>`_ Proc Natl Acad Sci 1936; 22:210-216. (first paper describing and explaining the diagmagnetic and paramagnetic properties of oxy- and deoxy-hemoglobin respectively)   
     * Silvennoinen MJ, Clingman CS, Golay X, et al.  `Comparison of the dependence of blood R2 and R2* on oxygen saturation at 1.5 and 4.7 Tesla <http://mriquestions.com/uploads/3/4/5/7/34572113/silvennoinen_et_al-2003-magnetic_resonance_in_medicine.pdf>`_. Magn Reson Med 2003; 49:47–60.​
     * Thulborn KR, Waterton JC, Matthews PM, Radda GK. `Oxygenation dependence of the transverse relaxation time of water protons in whole blood at high field <http://mriquestions.com/uploads/3/4/5/7/34572113/thulborn_hb_541151.pdf>`_. Biochem Biophys Acta 1982; 714:265–270. (describes T2 changes due to diffusion and their quadratic dependence on field strength)
     * Uludağ K, Muller-Bierl B, Uğurbil K. `An integrative model for neuronal activity-induced signal changes for gradient and spin echo functional imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/uludag_1-s2.0-s1053811909005576-main__1_.pdf>`_. Neuroimage 2009; 48:150-165.
     * Weisskoff RM, Zuo CS, Boxerman JL, Rosen BR. `Microscopic susceptibility variation and transverse relaxation: theory and experiment <http://mriquestions.com/uploads/3/4/5/7/34572113/weisskoff_541128.pdf>`_. Magn Reson Med 1994; 31:601-610.

**相关问题**
  * `What are the different forms of hemoglobin and why do they have different magnetic properties? <http://mriquestions.com/types-of-hemoglobin.html>`_
  * `Why does acute hemorrhage become dark on T2-weighted images? <http://mriquestions.com/acutedeoxy-hb.html>`_
  * `为什么BOLD信号在激活时反而增强？消耗了更多的氧气信号似乎应该降低。 <http://chunshan.github.io/MRI-QA/bold/why-does-bold-uarr-signal.html>`_