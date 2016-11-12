Question-两种类型的并行成像（PI）：我们的扫描仪中并行成像有两种不同的选择SENSE和GRAPPA。它们的原理是什么？应该选择哪一个？
==============================================================================================================================

:date: 2014-11-14
:tags: K-space & Rapid Imaging, Parallel Imaging
:slug: two-types-of-pi
:authors: Chunshan
:summary: 两种类型的并行成像（PI）SENSE和GRAPPA

原文链接:\ `Our scanner has two different options for parallel imaging (SENSE and GRAPPA). What are they and which should I use? <http://mriquestions.com/two-types-of-pi.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/2882704_orig.png
    :alt: summary
    :align: center
    :width: 700

并行成像技术一般分为两类：1）在图像域进行重建的技术，这类技术需要展开或反转的过程；2）在k空间进行的技术，这类技术需要在重建之前计算缺失的谐波数据。结合这两种技术的混合技术正变得越来越受欢迎。

**图像域并行成像**\ 是目前最广泛使用的方法，或许也是最容易理解的方法。我们将这一技术称为SENSE，这是此技术最初广泛使用的缩写（SENSitivity Encoding）。每一个主要的MR制造商对此技术有不同的商品名：Siemens（mSENSE），GE（ASSET），Philips（SENSE），Hitachi（RAPID），Toshiba（SPEEDER）。

**K空间并行成像**\ 技术操作的是复频率域信号，在这些信号转换为图像之前。这些方法都归在GRAPPA这一类下，GRAPPA最初是GeneRalized Autocalibrating Partial Parallel Acquisition的缩写，GRAPPA没有SENSE用得广泛，某种程度上更难理解。Siemens使用术语GRAPPA，而GE称为ARC（Autocalibrating Reconstruction for Cartesian imaging）。据我所知，其他的主要厂商尚未将K空间中的并行成像方法发布为一个产品。

每个技术的相对优点和缺点

在目前技术不断发展的状态下，哪种技术更优越尚没有达成共识。使用图像域的方法（SENSE/ASSET）还是使用k空间的方法（GRAPPA/ARC）与厂商有关，也与具体的情况有关。然而，以下的一般规则仍然是适用的。

1. 总成像时间。GRAPPA/ARC序列的时间一般比SENSE/ASSET长，因为它需要额外的时间用于k空间线数据的自校正。这个时间消耗对低分辨率的图像而言更加严重，这种情况下校正时间在总采集时间中所占的比例更高。随着成像矩阵尺寸的增加，GRAPPA/ARC序列此相对缺点降低。
2. 信噪比。SENSE/ASSET随着加速因子增加有稍高的SNR和更好的图像质量。R=2的情况下，这种差异几乎可以忽略。
3. 身体部位。SENSE/ASSET在异质的身体部位（如肺）上表现很差，这些部位上很难获得准确的线圈敏感映射图，此时GRAPPA/ARC更有优势。
4. 运动。如果在校准扫描和采集扫描之间有运动，SENSE/ASSET可能效果很差，导致重建伪影。一个明显的例子是患者在序列之间发生运动，即使此患者在每一个单独的序列扫描时保持完美的静止。第二个更微妙的例子适用于屏住呼吸的肝脏成像。这种情况下，在SENSE/ASSET的校正和成像时，患者可能很难暂停呼吸在完全相同的程度。此时，带自校正技术的GRAPPA/ARC会更受欢迎（假如全部序列可以在一次屏住呼吸的时间内完成）。应该指出的是，一些SENSE更新的变种（mSENSE，RAPID）也使用了自校正，因此这种区别就没有了。
5. 视野（FOV）。GRAPPA/ARC更能容忍小视野。当整个FOV比成像物体还小时，SENSE/ASSET可能在相位编码方向上产生伪影/卷折。相反，GRAPPA/ARC允许选择更小的FOV，但没有明显的伪影。
6. 在单次激发的平面回波成像（EPI）中的使用。GRAPPA/ARC在磁敏感引起场扭曲的情况下不太会影响重建过程，这比SENSE/ARC有显著的优势。

尽管这些细微的区别，SENSE和GRAPPA对几乎所有的应用中都可互换使用。在高级讨论和参考文献中有更多额外的细节。

**高级讨论**

下面列出的是一些更高阶的后续问题和解释。

**为什么在高度不均匀的区域如肺和腹部GRAPPA比SENSE表现好？** 答案在于SENSE需要对每个线圈产生准确的敏感性映射，这可能是很难获取的。GRAPPA中，估计缺失的k空间线数据更多是一个全局的过程，涉及三个线圈的数据，同时还有自动校准区域。它不受局部不均匀性的影响。在k空间中心额外采集的线数据还会增加信噪比和估计的准确性。

**为什么GRAPPA对单次激发的平面回波成像（EPI）效果更好？** 这儿也是线圈敏感性映射的问题。EPI方法本身的图像扭曲就比较严重，主要是由磁敏感效应引起的局部共振频率差异导致的。使用SENSE方法，由磁敏感效应引起的图像扭曲和由线圈敏感性映射导致的图像扭曲可能是不同的。由于上面描述的原因，GRAPPA方法中，这些图像扭曲对估计缺失的k空间线影响相对较小。

**为什么GRAPPA对小FOV的场景效果更好？** 对一些并行成像应用（如心脏磁共振）而言，需要相对小的FOV来观察感兴趣的解剖结构。减小FOV势必会带来混叠伪影，这并不是并行成像才特有的。在SENSE/ASSET中，这种混叠不能使用常规的并行成像展开算法进行校正，因而通常在图像的中心会观察到“SENSE Ghost”伪影。相反，GRAPPA/ARC可以不对重建算法进行任何修改就能产生部分混叠的全FOV图像。回忆一下，小FOV需要比通常的k空间线间距要大。简单增加线间距不会显著影响GRAPPA/ARC对缺失线数据的估计。因此小FOV应用中GRAPPA/ARC更受欢迎。 

**参考材料** 
    * Blaimer M, Breuer F, Mueller M, Heidemann RM, Griswold MA, Jakob PM. `SMASH, SENSE, PILS, GRAPPA. How to choose the optimal method <http://mriquestions.com/uploads/3/4/5/7/34572113/blaimer_parallelreview.pdf>`_. Top Magn Reson Imaging 2004;15:223-236 [review].     
    * Brau A. `New parallel imaging method enhances imaging speed and accuracy <http://mriquestions.com/uploads/3/4/5/7/34572113/arc_ge.pdf>`_. GE Signa Pulse, 2007; 36-38. (Promotional piece describing GE's ARC method). 
    * Griswold MA, Jakob PM, Heidemann RM, et al. `Generalized autocalibrating partially parallel acquisitions (GRAPPA) <http://mriquestions.com/uploads/3/4/5/7/34572113/griswold-grappa.pdf>`_. Magn Reson Med 2002; 47:1202-1210
    * Pruessmann KP, Weiger M, Scheidegger MB, Boesiger P. `SENSE: Sensitivity encoding for fast MRI <http://mriquestions.com/uploads/3/4/5/7/34572113/pruessmann-sense.pdf>`_. Magn Reson Med 1999; 42:952-962.

**相关问题**
  * `什么是并行成像？与常规成像有什么不同？ <http://chunshan.github.io/MRI-QA/parallel-imaging/what-is-pi.html>`_
  * `GRAPPA/ARC的原理是什么？ <http://chunshan.github.io/MRI-QA/parallel-imaging/grappaarc.html>`_