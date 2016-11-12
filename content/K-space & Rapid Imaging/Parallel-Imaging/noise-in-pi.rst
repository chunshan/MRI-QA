Question-并行成像中的噪声：为什么并行成像的检查看起来噪声如此大？
=================================================================================================================

:date: 2014-11-18
:tags: K-space & Rapid Imaging, Parallel Imaging
:slug: noise-in-pi
:authors: Chunshan
:summary: 并行成像中的噪声

原文链接:\ `Why do parallel imaging studies look so noisy? <http://mriquestions.com/noise-in-pi.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9012357_orig.png?286
    :alt: summary
    :align: center
    :width: 700

并行成像（PI，Parallel Imaging）的检查有时候确实看起来噪声很大。这是并行成像技术减少成像时间带来的直接后果。这样做，采集的数据点变少，用于平均的数据点也变少，因此信噪比（SNR）相应的下降。因此，并行成像序列的SNR总是比同等的非并行成像序列低。

所有影响非并行成像序列SNR的因素也会影响并行成像序列：磁场强度，磁体硬件，线圈加感，成像组织，脉冲序列，脉冲序列时序参数，体素大小，相位编码步数，接收器带宽，信号平均次数等。除此以外，并行成像序列的SNR（SNRparallel）受另外两个因素的影响进一步降低，用如下的方程表示：

 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9194473_orig.png?163
    :alt: Parallel Imaging SNR
    :align: center
    :width: 300

其中R是并行成像加速因子，g为具有空间依赖性的项称为几何因子。

√R项表示预期的信噪比损失是由减少扫描时间（加速因子R）引起的。由于仅采样k空间中1/R条线，这一项与非并行成像中减少相位编码步数或信号平均次数有相似的影响。因此，选择R = 2可以将成像时间减为原来的1/2，但信噪比降低为原来的1/√2 ≈ 0.71。SNR的显著影响如下图所示，其中R从1增加到3，再增加到6。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/939468_orig.jpg  | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4689355_orig.jpg  | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/8408272_orig.jpg  |
|    :alt: No acceleration (R=1)                                                |    :alt: Acceleration factor R=3                                               |    :alt: Acceleration factor R=6                                               |
|    :width: 300                                                                |    :width: 300                                                                 |    :width: 200                                                                 |
|                                                                               |                                                                                |                                                                                |
|    没有加速（R=1）                                                            |    加速因子R=3                                                                 |    加速因子R=6                                                                 |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6921875_orig.jpg?288
   :alt: SENSE knee MRI with R=4
   :align: center
   :width: 800

   膝关节SENSE MRI成像R=4。注意图像中噪声分布并不均匀，与随空间变化的因子g相关。

几何因子g更加有趣，是并行成像特有的。g取决于每一个点被重复采集的个数以及对应的线圈敏感性差异。g因子不是一个常数，而是随图像位置变化而变化，对于常用的典型线圈设计，整个成像容积内g因子的范围在1.0至2.0之间。

g因子依赖于1）表面线圈的数目和位置，2）线圈加感，3）成像平面，4）扫描平面内的相位编码方向，5）成像区域中体素的位置。它与表面线圈元素的数目，尺寸和方向都相关，可以认为它是对线圈分离的一个度量，有时也被称为“噪声放大因子”。

**参考材料** 
    * Aja-Fernandez, Vegas-Sanchez-Ferrero G, Tristan-Vega A. `Noise estimation in parallel MRI: GRAPPA and SENSE <http://mriquestions.com/uploads/3/4/5/7/34572113/snr_grappa_v_sense-cdn.com_s0730725x13003810_1-s2.0-s0730725x13003810-main.pdf>`_. Magn Reson Imaging 2014; 32:281-290.
    * Breuer FA, Kannengiesser SA, Blaimer M, Seiberlich N, Jakob PM, Griswold MA. `General formulation for quantitative g-factor calculation in grappa reconstructions <http://mriquestions.com/uploads/3/4/5/7/34572113/breuer_g_factors22066_ftp.pdf>`_. Magn Reson Med 2009; 62:739–46.
    * Pruessmann KP, Weiger M, Scheidegger MB, Boesiger P. `SENSE: Sensitivity encoding for fast MRI <http://mriquestions.com/uploads/3/4/5/7/34572113/pruessmann-sense.pdf>`_. Magn Reson Med 1999; 42:952-962.
    * Robson P, Grant A, Madhuranthakam A, Lattanzi R, Sodickson D, McKenzie C. `Comprehensive quantification of signal-to-noise ratio and g-factor for image-based and k-space-based parallel imaging reconstructions <http://mriquestions.com/uploads/3/4/5/7/34572113/robson_21728_ftp.pdf>`_. Magn Reson Med 2008; 60:895.     
    * Sodickson DK, Griswold MA, Jakob PM, et al. `Signal-to-noise ratio and signal-to-noise efficiency in SMASH imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/smashsnr.pdf>`_. Magn Reson Med 1999; 41:1009-1022.

**相关问题**
  * `并行成像中有什么特别的伪影么？ <http://chunshan.github.io/MRI-QA/parallel-imaging/artifacts-in-pi.html>`_