Question-拉链及相关伪影：我们断断续续在我们图像看到拉链样伪影，它们是怎么产生的？
=====================================================================================================================

:date: 2015-12-28
:tags: MR Artifacts, technique related artifacts
:slug: zipper-artifact
:authors: Chunshan
:summary: 拉链及相关伪影

原文链接:\ `We intermittently see zipper-like artifacts in our images. What causes them? <http://mriquestions.com/zipper-artifact.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9777154_orig.png?293
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5445937_orig.gif?316
   :alt: Zipper artifact due to RF-feedthrough
   :align: right
   :width: 300

   由于射频直通产生的链条伪影

穿过图像的拉链样条带假信号有许多原因，所以没有单一的策略可以纠正所有的此类伪影。拉链伪影最常见的形式是穿过图像的中心并且在相位编码方向出现。这种形式的拉链伪影是由于接收系统接收不同的发射器射频信号泄露（“直通”）导致的，最常见的这种RF噪声源或许是一个外部的信号源，由于射频屏蔽室的门没有完全封闭或它的密闭有缺陷。其次常见的原因是扫描室内麻醉检测设备（如脉搏血氧仪）的射频发射。

在频率编码方向的链条伪影通常是因为不完美的层面选择梯度轮廓或不合适的射频发射器调整产生的刺激回波。增加层面间的间隙可以减少这种伪影，但通常需要给服务工程师打电话。   

Annefact伪影（Annefact(cusp) artifact）是一种像羽毛的明亮信号，在相位编码方向上穿过图像的中心，这一点上很像拉链伪影。它的产生是因为FOV外的刺激回波被远处没有正确停用的阵列线圈接收，这种伪影是一种卷折伪影，由于梯度与磁体孔末端空间上变化的主磁场非线性地耦合产生。Annefact伪影在脊柱或骨盆矢状位或冠状位的FSE图像图像上最常见，偶尔，这种伪影也会退化为图像中间的一些集群点，成为星状伪影(star artifac)。

+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9359301_orig.jpg | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/7796144_orig.jpg?265     |
|    :alt: Annefact (cusp) artifact                                             |    :alt: Star artifact (arrow)                                                        |
|    :width: 300                                                                |    :width: 300                                                                        |
|                                                                               |                                                                                       |
|    由于FOV外的刺激回波产生的Annefact伪影                                      |    星状伪影（箭头处）                                                                 |
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

**参考材料**
     * Artasona LM. `Annefact artifact in MRI <http://mriquestions.com/uploads/3/4/5/7/34572113/annefact_artifact.pdf>`_. Blog at El Baul Radiologicó 16 Mar 2015, accessble at this link in Spanish.
     * Graves MJ, Mitchell DG. `Body MRI artifacts in clinical practice: a physicist's and radiologist's perspective <http://mriquestions.com/uploads/3/4/5/7/34572113/graves_et_al-2013-journal_of_magnetic_resonance_imaging.pdf>`_. J Magn Reson Imaging 2013; 38:269-287.     
     * Heiland S. `From A as in aliasing to Z as in zipper: artifacts in MRI <http://mriquestions.com/uploads/3/4/5/7/34572113/artifacts_a_to_z.pdf>`_. Clin Neuroradiol 2008; 1:25-36. 
     * Larkman DJ, Herlihy AH, Coutts GA, Hajnal JV. Elimination of magnetic field foldover artifacts in MR images. J Magn Reson Imaging 2000; 12:795-797.​_ 
     * Rangawala N, Zhou XJ. `Reduction of fast spin echo cusp artifact using a slice-tilting gradient <http://mriquestions.com/uploads/3/4/5/7/34572113/rangwala_et_al-2010-magnetic_resonance_in_medicine.pdf>`_. Magn Reson Med 2010;64:220-228.   
     * Zhuo J, Gullapalli RP. `AAPM/RSNA physics tutorial for residents <http://mriquestions.com/uploads/3/4/5/7/34572113/zhuo_aritfacts_radiographics.pdf>`_. MR artifacts, safety, and quality control. Radiographics 2006;26:275-297.

**相关问题**
	* `我们还应该注意哪些其他数据相关的伪影？ <http://chunshan.github.io/MRI-QA/technique-related-artifacts/data-artifacts.html>`_