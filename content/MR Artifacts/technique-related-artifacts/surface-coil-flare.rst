Question-表面线圈耀斑：表面线圈耀斑是什么？可以对它做什么？
============================================================================================================

:date: 2015-12-30
:tags: MR Artifacts, technique related artifacts
:slug: surface-coil-flare
:authors: Chunshan
:summary: 表面线圈耀斑

原文链接:\ `What is surface coil flare? What can be done about it? <http://mriquestions.com/surface-coil-flare.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/3046393_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_5277660_orig.gif
   :alt: Signal to noise ratio for coils of various sizes
   :align: right
   :width: 350

   不同尺寸的线圈的信噪比。表面线圈的灵敏度随着距离表面越远下降越厉害.

磁共振成像越来越多的使用放置在身体附近或身体上的小表面线圈阵列，并与并行成像结合使用。使用小表面线圈比使用大的，距离身体更远的线圈的优势是会有更高的信噪比（SNR），缺点是会造成信号的不均匀性。线圈的穿透深度与其直径成反比，患者表面产生的信号增强而患者体内深处产生的信号衰减，由此产生的明亮的表面信号有时被称为表面线圈“耀斑”。

+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/7352962_orig.jpg | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5740339_orig.jpg         |
|    :alt: Surface coil spine image showing surface coil flare                  |    :alt: Same image as left, post-processed with SCIC                                 |
|    :width: 400                                                                |    :width: 400                                                                        |
|                                                                               |                                                                                       |
|    表面线圈脊柱图像的表面线圈“耀斑”表现为过多明亮的皮下脂肪。                 |    与左边相同的图像，用SCIC算法（表面线圈强度校正，Surface Coil Intensity             |
|    深层组织的信号相对较低，看起来就差。                                       |    Correction）处理后的结果。注意整幅图像对比度更加均匀。                             |
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

表面线圈耀斑最简单的解决方案是对重建后的图像应用一个后处理滤波器。这样的滤波器可以校正低空间频率的强度调制，增强图像对比度，减少噪声，它们被统称为SCIC（表面线圈强度校正）。一些版本的SCIC是每个厂商都提供的，并作为一项常规使用的规则，特别是对脊柱，四肢和身体成像。但是，当需要得到定量数据时不要使用强度校正滤波器，如质量保证/SNR测量，T2软骨映射，功能磁共振成像等。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6421885_orig.jpg
   :alt: PURE large FOV, low spatial resolution calibration scan 
   :align: right
   :width: 350

   PURE - 使用体线圈映射线圈灵敏度的大FOV，低空间分辨率校准扫描

对于多通道并行成像，可以在成像之前对非均匀的接收器线圈配置进行校正。不同的供应商对这些方法有不同的名称：GE（PURE- "Phased array Uniformity Enhancement"相控阵均匀性增强），Siemens（Prescan Normalize，预扫描均一化），Philips（CLEAR - "Constant LEvel AppeaRance"恒定外观水平），Hitachi（(NATURAL - "NATural Uniformity Realization Algorithm"自然的一致性算法实现）。与SCIC不同，这些预扫描校正方法需要在成像前进行短暂的表面线圈灵敏度校准扫描。

对于大多数应用而言，可以同时使用线圈均匀性校正预处理和后处理。

**高级讨论**

如上所述，除了定量成像时应限制使用滤波器，当成像视野中包含大的金属植入物时也应当避免使用像PURE/CLEAR等预扫描方法。此时线圈校准很可能会失败或不充分，校准后的图像甚至比不校准的图像更差。

由于PURE/CLEAR方法需要在成像前进行校准扫描，患者在两次扫描间的任何运动都可能导致校准失败或产生伪影。

**参考材料**
     * Belaroussi B, Milles J, Carme S, et al. `Intensity non-uniformity correction in MRI: existing methods and their validation <http://mriquestions.com/uploads/3/4/5/7/34572113/belaroussi_.com_s1361841505000976_1-s2.0-s1361841505000976-main.pdf>`_. Med Image Anal 2006; 10:234-246. (This review shows that there are many new and interesting methods for solving the image intensity problem than are available on current clinical scanners).    
     * GE Healthcare. `MR Field Notes: RF Coils...They've come a long, long way <http://mriquestions.com/uploads/3/4/5/7/34572113/ge_fieldnotes_volume1-2_coils.pdf>`_. 2005.        
     * Hayes CE, Axel L. `Noise performance of surface coils for magnetic resonance imaging at 1.5T <http://mriquestions.com/uploads/3/4/5/7/34572113/surface_coil_snrhayes85.pdf>`_. Med Phys 1985; 12:604-7.
     * McVeigh ER, Bronskill MJ, Henkelman RM. `Phase and sensitivity of receiver coils in magnetic resonance imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/mcveigh_med_phys_1986.pdf>`_. Med Phys 1986; 13:806-814.
     * Wallner Bk, Edelman RR, Bajakian RL, et al. `Signal normalization in surface-coil MR imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/wallner_ajnr.pdf>`_. Am J Neuroradiol 1990; 11:1271-2.

**相关问题**
	* `How do receive-only coils work? <http://mriquestions.com/receive-only-coils.html>`_