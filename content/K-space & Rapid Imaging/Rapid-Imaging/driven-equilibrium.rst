Question-驱动平衡：驱动平衡（快速恢复）脉冲是什么？
======================================================================================================================

:date: 2014-10-30
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: driven-equilibrium
:authors: Chunshan
:summary: 驱动平衡（快速恢复）脉冲序列

原文链接:\ `What is a driven equilibrium (fast recovery) pulse? <http://mriquestions.com/driven-equilibrium.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1998045_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9078766_orig.gif?550
   :alt: Driven equilibrium technique
   :align: right
   :width: 400

   驱动平衡技术使胆汁在FSE的MRCP图像（短TR，1200ms）上显示高信号。

驱动平衡（DE，Driven Equilibrium）也称为快速恢复，是一种使用-90°“翻转回来”的脉冲在MR序列结束时帮助恢复纵向磁化的技术。快速成像中，长T1和长T2的物质（如脑脊液，尿液和胆汁）在一个TR间隔的后期其纵向磁化（Mz）可能仍然没有完全恢复。经过几个周期就会发生饱和，这些液体正常的高T2信号会降低，驱动平衡技术恢复这些信号特别有用，广泛用于脊柱成像，磁共振尿路造影术和胰胆管造影术（MRCP，Magnetic Resonance Cholangiopancreatography）。

如左图中所示，长T1和长T2的液体在一个周期结束时仍有明显的横向磁化，通过使用-90°脉冲，此横向磁化翻转回纵向平面，辅助T1恢复，增强MR信号。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/8270313_orig.gif
   :alt: Driven equilibrium technique
   :align: left
   :width: 500

驱动平衡脉冲实际上可与任何成像或波谱序列结合使用，但最常用于快速自旋回波成像中。所有主要的MR厂商都提供了此种序列，但有不同的商品名：Siemens称为RESTORE，GE称为FRFSE（快速恢复的快速自旋回波，Fast Recovery Fast Spin Echo），Philips称为DRIVE，Hitachi称为驱动平衡FSE，Toshiba称为T2 Plus FSE。偶尔也会使用通用的简写DEFT（Driven Equilibrium Fourier Transform），一个典型的2D快速自旋回波如下所示。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6756418_orig.gif?565
   :alt: Driven equilibrium technique
   :align: center
   :width: 700

   FSE序列结束时使用-90°的驱动平衡脉冲

DE模式的一簇三个非选择性脉冲（+90°/180°/-90°）可用作波谱，EPI和GRE序列（如MP-RAGE）的准备模块。因为在这些脉冲之间会发生T2衰减，使用此模块可以得知T2敏感性，因此常被称为T2准备脉冲（T2-pre pulse）。

**高级讨论**

因为DE脉冲的翻转角可能与理想值略有不同，会使用围绕180°脉冲的破碎梯度（crusher gradients）和“翻转回来”90°脉冲之后的扰相梯度（spoiler gradients）干扰残留的横向磁化。

**参考材料** 
    * Becker ED, Ferretti JA, Farrar TC. `Driven equilibrium Fourier transform spectroscopy. A new method of nuclear magnetic resonance signal enhancement <http://mriquestions.com/uploads/3/4/5/7/34572113/becker_1969_ja50001a068.pdf>`_. J Am Chem Soc 1969;91:7784-5. (This was the first use of a DE pulse — to improve the signal in NMR spectroscopy)
    * Melhem ER, Itoh R, Folkers PJM. `Cervical spine: three-dimensional fast spin-echo MR imaging − improved recovery of longitudinal magnetization with driven equilibrium pulse <http://mriquestions.com/uploads/3/4/5/7/34572113/melhem_deft_spine_radiology2e2182e12er01ja38283.pdf>`_. Radiology 2001; 218:283-288. (Good description of how DE pulses can be used to augment CSF signal in 3D FSE imaging).
    * van Uijen CM, den Boef JH. `Driven-equilibrium radiofrequency pulses in NMR imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/van_uijen_539237.pdf>`_. Magn Reson Med 1984;1:502-7. (One of the earliest implementation of DE pulses for imaging).


**相关问题**
	* `什么是快速自旋回波成像？ <http://chunshan.github.io/MRI-QA/rapid-imaging/what-is-fsetse.html>`_