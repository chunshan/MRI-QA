Question-CAIPIRINHA：CAIPIRINHA是什么？难道不是一种饮料么？
=================================================================================================================

:date: 2014-11-17
:tags: K-space & Rapid Imaging, Parallel Imaging
:slug: caipirinha
:authors: Chunshan
:summary: CAIPIRINHA

原文链接:\ `What is CAIPIRINHA? Isn't it some sort of a drink? <http://mriquestions.com/caipirinha.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6923388_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6909326_orig.jpg
   :alt: CAIPIRINHA
   :align: left
   :width: 300

Caipirinha是巴西的一种鸡尾酒，由甘蔗酒（cachaça），糖，冰和酸橙制成。2014FIFA世界杯上有这种鸡尾酒的大量新闻，使得它在世界范围内的知名度又获得了提升。

但是在MRI中，CAIPIRINHA是一种由Siemens提供的一种并行成像方法，主要用于三维的屏气腹部图像，CAIPIRINHA是Controlled Aliasing in Parallel Imaging Results in Higher Acceleration的缩写。

SENSE和GRAPPA都可以用于3D采集模式，在两个相位编码方向同时加速。然而由于线圈的几何形状和敏感性不同，当选择比较大的R值时可能会出现严重的残余混叠伪影和放大的噪声。

CAIPIRINHA使用一组独特的k空间采样模式减少像素混叠和重建图像上的重叠。由于在相位编码梯度表中施加了额外的偏移，k空间中采集的数据点也被平移了。

以下是GRAPPA类并行成像序列三种可能的k空间填充方式，其中R=4。注意读出方向（kx）是进入页面的。红圈表示采集的数据点，白圈表示缺失的数据点，必须在重建过程中从已知数据（红点）估计出来。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5788819_orig.gif | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/8640751_orig.gif  | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/3985147_orig.gif  |
|    :alt: R=4                                                                  |    :alt: R = 2 x 2 = 4                                                         |    :alt: no phase wrap-around                                                  |
|    :width: 300                                                                |    :width: 300                                                                 |    :width: 200                                                                 |
|                                                                               |                                                                                |                                                                                |
|    在一个方向上加速（R=4）                                                    |    在两个方向上加速（R = 2x2 = 4）                                             |    CAIPIRINHA的加速模式，在两个方向加速加交替行的相移                          |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

第一个图中，加速仅沿一个方向（kz），每4行采集一行。这种策略通常会增加噪声和残余的混叠伪影。

第二个图中，使用了一个稍微好点的策略，加速在ky和kz方向均分，因此，在两个相位编码方向都会出现每隔一条线会缺失，总的加速仍然保持为4（R = 2 x 2）。

第三个图中，使用了CAIPIRINHA模式的采样，每一个相位编码方向的R = 2但是中间列数据采样有相移（每4列）。此相位偏移提高了重建的准确性，减少了噪声和混叠。混叠伪影仍然存在但是被平移到图像空间的角落上，不再集中于几个位置。

目前CAIPIRINHA通常用于3D肝脏检查，在对比剂通过时可以得到质量非常优秀的图像，而且加速比很高。下面显示了一个临床的例子，CAIPIRINHA也被建议用于弥散加权成像和MRA。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5678495_orig.jpg?650
   :alt: 3D T1-VIBE
   :align: center
   :width: 800

   使用CAIPIRINHA的3D T1-VIBE，加速因子R = 4。在对比剂通过过程中保持屏气，每隔2秒重复采集覆盖整个肝脏的72层图像（3mm厚）。

**高级讨论**

**CAIPIRINHA的附加笔记**

虽然上面的例子使用的是GRAPPA，但CAIPIRINHA既可以与SENSE算法一起使用也可以与GRAPPA算法一起使用，甚至可以与非笛卡尔方法一起使用。

除了第三个图中被称为Δ=2的交替相位方法，许多不同的CAIPIRIINHA采样模式也是可行的。可能的采样模式数量随加速因子R的增加指数增加。

**参考材料** 
    * `Caipirinha <https://en.wikipedia.org/wiki/Caipirinha>`_. Wikipedia, the Free Encyclopedia. 
    * Breuer F, Blaimer M, Griswold M, Jakob P. `Controlled aliasing in parallel imaging results in higher acceleration (CAIPIRINHA) <http://mriquestions.com/uploads/3/4/5/7/34572113/caipirinha_flash_article-00570122.pdf>`_. MAGNETOM Flash 2012;1:2-7. (Siemens promotional brochure).
    * Breuer FA, Blaimer M, Mueller MF, et al. `Controlled aliasing in volumetric parallel imaging (2D CAIPIRINHA) <http://mriquestions.com/uploads/3/4/5/7/34572113/breuerf_mrm_2006_55_549_556caiprinah.pdf>`_. Magn Reson Med 2006; 55:549-556.
    * Yutzy SR, Seiberlich N, Duerk JL, Griswold MA. `Improvements in multislice parallel imaging using radial CAIPIRINHA <http://mriquestions.com/uploads/3/4/5/7/34572113/caiprinha_-yutsy_nihms-253625.pdf>`_. Magn Reson Med 2011; 65:1630-1637.

**相关问题**
  * `什么是并行成像？与常规成像有什么不同？ <http://chunshan.github.io/MRI-QA/parallel-imaging/what-is-pi.html>`_