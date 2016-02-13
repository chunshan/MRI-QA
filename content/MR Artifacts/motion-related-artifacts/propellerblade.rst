Question-螺旋桨/刀锋：螺旋桨技术如何减少运动伪影？
======================================================================================================

:date: 2015-12-08
:tags: MR Artifacts, motion related artifacts
:slug: propellerblade
:authors: Chunshan
:summary: 螺旋桨技术如何减少运动伪影？

原文链接:\ `How does PROPELLER reduce motion artifacts? <http://mri-q.com/propellerblade.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/267662_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6154900_orig.gif
   :alt: PROPELLER sequence sampling strips of data
   :align: right
   :width: 400

   PROPELLER序列的数据采样带采用围绕k空间中心旋转的方式

螺旋桨（Periodically Rotated Overlapping ParallEL Lines with Enhanced Reconstruction， PROPELLER）技术是20世纪90年代末期由Pipe发明的减少运动伪影的方法。基本思想是以旋转的方式使用一组组径向直线条（或称为“刀片”）对k空间进行采样。

每一个刀片由多个平行的相位编码扫描线组成，这些扫描线可以使用快速自旋回波或梯度回波。实践中，通常一次激发采集8-32个刀片线，刀片以很小的角度（10°-20°）旋转，然后采集第二组数据。这个过程一直持续到整个k空间的成像数据都已收集。

PROPELLER填充k空间的轨迹有一些独特的优势。k空间的中心（信号幅度最高，对图像对比度贡献最大）过采样，意味着信号噪声比和对比度噪声比比较高。这个区域的过采样还提供了冗余信息，意味着新刀片的数据可以与来自前一个刀片的数据比较一致性。如果患者在两个刀片之间有运动，第二个刀片的数据可以基于其中心信息不一致的程度进行校正（甚至被全部丢弃）。

PROPELLER重建算法包括以下几个步骤：1）对每一个刀片进行相位校正保证其旋转的支点恰好位于k空间的中心；2）物体平面内旋转和平面内平移的修正；3）相关加权用于最小化刀片数据中包含的运动和位移误差。现在PROPELLER的2D版本仅能校正平面内运动，3D版本未来可能会克服此限制。复杂的重建过程在扫描结束后还需要额外的一些时间，用我们目前的计算机硬件，对一个大数据集需额外延迟大约15+秒才能开始下一个序列。

PROPELLER作为最受欢迎的磁共振序列，所有主要厂商都有自己的小变化，而且有自己好听的名字：GE（PROPELLER），SIEMENS（BLADE），Philips（MulitVane），Hitachi（RADAR）和Toshiba（JET）。

PROPELLER技术对运动校正的程度可能是实质性地，通常用于DWI，FLAIR和T2加权图像，任何患者都可以使用，我们期待此技术可以使得患者在扫描过程中不用静止不动。由于对k空间的过采样，磁敏感伪影也有轻微减少。一个例子如下所示。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/4885686_orig.jpg?268    | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/5419247_orig.jpg?270     |
|    :alt: Without PROPELLER: Patient motion artifacts on routine FSE image     |    :alt: With PROPELLER: Motion artifacts substantially reduced                |
|    :width: 330                                                                |    :width: 330                                                                 |
|                                                                               |                                                                                |
|    没有PROPELLER，常规FSE图像中出现患者运动伪影                               |    使用PROPELLER，运动伪影显著减少                                             |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

**高级讨论**

关于PROPELLER成像的进一步评论：

虽然k空间中心高度过采样，k空间的“角落”完全没有采样到。然而，这些位置仅仅对最终图像中倾斜角度上的高空间频率信息有贡献，所以通常被认为是k空间中最不重要的区域。如果每个刀片有L条线，共N个刀片，成像矩阵的等价直径M可表达为LN = πM/2

使用PROPELLER方法，k空间圆的完全覆盖（刀片之间没有空隙）需要比笛卡尔（矩形）k空间填充方法长约π/2 ≈ 1.57倍。刀片重叠的程度（两个相邻刀片之间的角度）通常是操作者可选的百分比形式的参数，制造商对此参数也有不同的名字，"blade coverage factor" (Siemens), "MultiVane percentage" (Philips), "k-space filling factor" (Toshiba)。覆盖因数为157%是无缝覆盖，覆盖因数为100%与笛卡尔方法相比不会有时间上的损失但是两个刀片末端将会有间隙。如果使用低于100%的覆盖因数进行扫描将会有更明显的条状伪影。覆盖因数更高的扫描伪影更少，信噪比更高，代价是扫描时间更长。通常在临床实践中选择100%到157%之间的某个值。

**参考材料**
     * Hirokawa Y, Isoda H, Maetani YS, et al. `MRI artifact reduction and quality improvement in the upper abdomen with PROPELLER and Prospective Acquisition Correction (PACE) technique <http://mri-q.com/uploads/3/4/5/7/34572113/hirokawa_blade_ajr_2010.pdf>`_. AJR Am J Roengenol 2008;191:1154-1158.     
     * Pipe JG. `Motion correction with PROPELLER MRI: application to head motion and free-breathing cardiac imaging <http://mri-q.com/uploads/3/4/5/7/34572113/pipej_mrm_1999_42_953_959_propeller.pdf>`_. Magn Reson Med 1999; 42:963-969.
     * van Loon L. `Tips for robust motion correction in liver imaging using MultiVane <http://mri-q.com/uploads/3/4/5/7/34572113/tips_for_robust_motion_correction_in_liver_imaging_using_multivane.pdf>`_. Philips NetForum Community, 30 Jan 2014.

**相关问题**
	* `What about wrap-around artifacts on radial or spiral imaging? it seems like they should always be present because phase-encode goes in every direction. <http://mri-q.com/spiralradial-artifacts.html>`_