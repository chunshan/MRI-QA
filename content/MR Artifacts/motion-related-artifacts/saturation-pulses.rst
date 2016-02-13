Question-饱和脉冲：饱和脉冲如何起作用？
================================================================================

:date: 2015-12-04
:tags: MR Artifacts, motion related artifacts
:slug: saturation-pulses
:authors: Chunshan
:summary: 饱和脉冲如何起作用？

原文链接:\ `How do saturation pulses work? <http://mri-q.com/saturation-pulses.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/7894146_orig.png?305
    :alt: summary
    :align: center
    :width: 700

饱和脉冲使用射频能量抑制成像区域外运动组织的磁共振信号达到减少或消除运动伪影的目的。有三种类型的饱和脉冲。

**空间饱和脉冲**\ 是空间选择性的90°脉冲将磁化翻转到横向平面。与用于成像的90°激发脉冲不同，空间饱和脉冲使用不同的载波频率发射，并且被设计为跨饱和带产生最大的相位分散，不使用切片复相叶。实际中，空间饱和脉冲后会紧接着在相位编码轴和频率编码轴上施加很强的扰相梯度进一步抑制残余的横向磁化。

Siemens, Hitachi, 和Toshiba称空间饱和脉冲为“Presat pulses”，GE称之为“Sat pulses”，Philips称之为“REgional Saturation Technique (REST)”。技师在扫描图像前会将空间饱和带在scout图像中用图形标示出来。它们的角度，中心和宽度都可以调整，一般的厚度在5-10cm的范围。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/9806759_orig.gif?474    | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6003678_orig.jpg         |
|    :alt: Spatial Saturation Pulses                                            |    :alt: Spatial saturation band placed on anterior neck                       |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
|                                                                               |    空间饱和带放置在前颈部以减少吞咽伪影传到脊柱上                              |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/1486513_orig.gif?258
   :alt: Arterial saturation pulse to suppress flow artifacts in an imaged slice
   :align: right
   :width: 400

   动脉饱和脉冲抑制成像切片中的流动伪影。为了抑制静脉血流，需要选择切片相反侧的饱和带。

**流动饱和脉冲**\ 是用于抑制不需要的血管流动伪影进入成像切片的空间选择性饱和带。饱和带在平行于成像切片上游几厘米处施加（最优位置依赖于血流速度）。虽然在常规成像中多数被用于抑制动脉血流，在飞行时间（time-of-flight，TOF）磁共振血管造影中，血管饱和带被用于抑制静脉血流。

TOF MRA中，在多层图像采集过程中，静脉饱和脉冲与成像切片有固定的偏移。不同的制造商对这些移动的血管饱和脉冲有不同的名字： GE ("walking sat"), Siemens ("travel sat" 或 "tracking sat"), Philips ("travel REST), Hitachi ("sequential pre-sat"), Toshiba ("BFAST")。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/5844351_orig.jpg        | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/2543314_orig.jpg         |
|    :alt: T1-weighted abdomen image without flow saturation                    |    :alt: Application of superior flow saturation pulse                         |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
|    没有施加流动饱和脉冲的腹部T1加权像，有明显的来自主动脉的伪影。             |    上游使用流动饱和脉冲后减少了主动脉伪影，消除了血管流动伪影。                |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

**频谱饱和脉冲**\ 基于其化学位移抑制一种特殊的化学物质，通常是脂肪，也被称为脂肪饱和或化学位移选择（Chemical Shift Selective，CHESS）。这些射频脉冲的持续时间很短，而且被调谐到脂肪的共振频率，在磁共振成像序列开始之前立刻施加。化学选择脉冲使得脂肪信号消失（被饱和）然而水信号相对不受影响。由于运动的皮下脂肪是运动伪影的主要来源，整幅图像中抑制脂肪信号也就减少了运动伪影。这些脉冲的设计和使用在一个单独的\ `Q&A <http://mri-q.com/fat-sat-pulses.html>`_\ 中有更完整的讨论。

**高级讨论**

第四种重要的射频脉冲类型称为\ **空间频谱脉冲（Spatial-Spectal (SPSP) Pulse）**\ 。这可以视作空间饱和脉冲和频谱饱和脉冲的混合，在特定的位置使用特定的频谱激发磁化。

空间频谱（SPSP）脉冲比分别的两种脉冲持续时间更短，对B1场不均匀性有更好的容忍度。SPSP有许多变种，但是所有变种都含有广谱射频包络下的多个射频子脉冲，此射频包络有并发的震荡双极性层面选择梯度。SPSP脉冲越来越常用，尤其是在平面回波和螺旋采集技术中。

**参考材料**
     * Felmlee JP, Ehman RL. `Spatial presaturation: a method for suppressing flow artifacts and improving depiction of vascular anatomy in MR imaging <http://mri-q.com/uploads/3/4/5/7/34572113/spatial_presat_felmlee_radiology2e1642e22e3602402.pdf>`_. Radiology 1987;164:559 –564.
     * Rosen BR, Wedeen VJ, Brady TJ. `Selective saturation NMR imaging <http://mri-q.com/uploads/3/4/5/7/34572113/selective_saturation_nmr_imaging_.1.pdf>`_. J Comput Assist Tomogr 1984;8:813-818.

**相关问题**
	* `How do Fat-Sat pulses work? <http://mri-q.com/fat-sat-pulses.html>`_