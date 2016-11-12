Question-HASTE/SS-FSE：什么是HASTE？
======================================================================================================================

:date: 2014-11-04
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: hastess-fse
:authors: Chunshan
:summary: HASTE

原文链接:\ `What is HASTE? <http://mriquestions.com/hastess-fse.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4118556_orig.png
    :alt: summary
    :align: center
    :width: 700

HASTE是Siemens对平面回波的快速自旋回波序列的商标名。其扩展的缩写相当完整地描述了其内涵：Half-Fourier Acquisition Single-shot Turbo spin Echo imaging。

其他厂商也有相似的序列，但是名字略有不同：GE（Single-shot fast spin echo, SS-FSE），Philips（Single-shot turbo spin echo, SSH-TSE; ultra-fast spin echo, UFSE)， Hitachi (Single-shot fast SE)，Toshiba (Fast Advanced Spin Echo, FASE, SuperFASE)。

HASTE/SS-FSE是一种单次激发技术。这意味着k空间所有的数据都是来自一个90°激发脉冲，要求有很长的回波链，对现代扫描仪而言，可能达到128，256甚至更高。

相比之下，常规的FSE/TSE是一种多次激发技术，这意味着虽然k空间的填充比传统SE快很多，但仍然需要多次RF激发才能采集所有的数据。例如，如果需要在k空间中采样128行，ETL（Turbo factor）为16的FSE/TSE序列需要128/16 = 8次激发才能完整地收集数据。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/7975618_orig.jpg
   :alt: Single Shot v.s. Multi Shot
   :align: center
   :width: 700

为了最小化k空间中采样的行数，HASTE/SS-FSE利用k空间的相位共轭对称性（一种部分傅里叶方法），仅直接采集比k空间的一半儿多一点儿的数据，其余行的数据可以利用k空间的“镜像”性质估计出来。一个典型的HASTE/SS-FSE脉冲序列时序图如下所示。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/3443842_orig.gif?576
   :alt: Representative HASTE/SS-FSE pulse sequence
   :align: center
   :width: 800

   代表性的HASTE/SS-FSE脉冲序列。注意到相位编码方向非对称采样，k空间一侧外围的行没有采集而是使用共轭对称性进行估计。

HASTE/SS-FSE技术的应用已经遍及全身，包括常规的定位像，儿童或不配合患者的头或身体的图像，胎儿成像，非屏气的腹部成像，磁共振胆胰管成像，磁共振脊髓造影，非增强的磁共振血管造影。不可避免的，回波时间相对长，HASTE图像通常是T2加权的，然而，与预备的反转脉冲相结合，也可以生成某种程度上T1加权或质子密度加权的对比度。下面是几个代表性的例子。

+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/2440505_orig.jpg?175 | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9806732_orig.jpg?71  |
|    :alt: HASTE                                                                    |    :alt: HASTE                                                                    |
|    :height: 350                                                                   |    :height: 350                                                                   |
|                                                                                   |                                                                                   |
+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4934130_orig.jpg?116 | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9347174_orig.jpg?177 |
|    :alt: HASTE                                                                    |    :alt: Gibbs (truncation) artifacts                                             |
|    :height: 350                                                                   |    :height: 350                                                                   |
|                                                                                   |                                                                                   |
+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+

**参考材料** 
    * Patel MR. Klufas RA, Alberico RA, Edelman RR. `Half-Fourier acquisition single-shot turbo spin-echo (HASTE) MR: Comparison with fast spin-echo MR in diseases of the brain <http://mriquestions.com/uploads/3/4/5/7/34572113/patel_haste_v_fse_in_brain.pdf>`_. AJNR Am J Neuroradiol 1997; 18:1635-1640.

**相关问题**
  * `How does phase-conjugate symmetry work? Why is it used? <http://mriquestions.com/phase-symmetry.html>`_