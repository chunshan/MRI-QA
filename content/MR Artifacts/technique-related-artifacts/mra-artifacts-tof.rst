Question-TOF MRA伪影：我们应该知道TOF MR哪些主要的伪影？
============================================================================================================

:date: 2015-12-31
:tags: MR Artifacts, technique related artifacts
:slug: mra-artifacts-tof
:authors: Chunshan
:summary: TOF MRA伪影

原文链接:\ `What are the major TOF MR artifacts should we know about? <http://mriquestions.com/mra-artifacts-tof.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_2744322_orig.png
    :alt: summary
    :align: center
    :width: 700

时间飞行（time-of-flight，TOF）MRA检查至少有6种不同的伪影经常被提及。下面有图示和简单说明。

**阶梯状伪影（仅2D TOF）**

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_5661541_orig.jpg
   :alt: Mild "stair-step" artifact
   :align: right
   :width: 400

   非各向同性的体素产生的温和的阶梯状伪影

这种伪影最简单的形式是在倾斜方向的血管上有微妙的像素化外观。这种伪影是因为二维层面相对与平面内的空间分辨率（0.5-1.0mm）而言比较厚（1-3mm）。可以通过重叠25%-30%的层面使阶梯状伪影最小化。这意味着覆盖相同的区域要更多的层面，伴随着扫描时间也会增加。

分别扫描二维层面时如果有轻微或重大的运动就会产生更严重的阶梯状伪影。

+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_2253338_orig.jpg| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_9446485_orig.jpg        |
|    :alt: Mild motion artifact                                                 |    :alt: Severe artifacts with jagged edges                                           |
|    :width: 400                                                                |    :width: 400                                                                        |
|                                                                               |                                                                                       |
|    轻微的运动伪影导致主动脉2D-TOF MRA上出现水平带                             |    颈动脉TOF MRA检查中比较大的运动导致锯齿状边缘的严重伪影                            |
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

**平面内饱和伪影**

TOF MRA依赖于新鲜血液（不饱和）的流入产生高血管内信号，当流动方向垂直于主成像平面时信号最强。如果血管在平面内穿行，其中的血液会像静态组织一样变得饱和，导致信号降低。在2D或3D TOF技术中都会出现。

+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_7244556_orig.jpg| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_1693649_orig.jpg        |
|    :alt: 3D-TOF MRA showing artifactual in-plane signal loss                  |    :alt: 2D-TOF MRA shows artifactual in-plane signal loss                            |
|    :width: 350                                                                |    :width: 350                                                                        |
|                                                                               |                                                                                       |
|    3D-TOF MRA显示两根大脑中动脉处都有平面内信号丢失                           |    2D-TOF MRA显示两根胫前动脉的水平部分都有平面内信号丢失                             |
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

**闪耀伪影**

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_5214666_orig.jpg
   :alt: CSF inflow phenomenon
   :align: right
   :width: 300

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_8012886_orig.jpg
   :alt: CSF inflow phenomenon
   :align: right
   :width: 300

   CSF流入现象（下面的源图像）产生MIP图像（上图）的伪影   

2D和3D TOF MRA图像都会使用最大密度投影（MIP，Maximum Intensity Projection）算法进行显示。MIP算法会选择任意最大信号强度（如背景的2倍标准差）的所有像素。

除了明亮的血管，其他任何有高信号亮度的材料都会“闪耀”或“污染”MIP图像。由于TOF MRA脉冲序列实际上是T1加权的，短T1材料（血肿，钆，脂肪）是这一现象的主因。然而，任何高信号焦点（由于运动或磁敏感效应）都会产生解释上的问题。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_5500921_orig.jpg
   :alt: 3D TOF MRA 
   :align: center
   :width: 600

   3D TOF MRA在颅底显示来自血肿(H)和脂肪(F)的高信号闪耀   

**逆流伪影**

这更多是一个陷阱而不是伪影，但同样需要注意。回忆一下，TOF技术通常会使用移动饱和脉冲消除静脉向相反方向流动的信号，但是如果由于一些异常情况下动脉逆行会发生什么呢？是的，此动脉也会被抑制，在TOF MRA中不可见。下图显示了一个例子，一个锁骨下动脉盗血综合征的患者左椎动脉被扭转。类似的现象也可以在骨盆和下肢上看到，这些部位狭窄病变周围的血管网络也可能遵循逆行的过程。

+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_9173742_orig.jpg| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_2657859_orig.jpg        |
|    :alt: 2D TOF MRA shows only right vertebral artery                         |    :alt: Contrast-enhanced MRA                                                        |
|    :width: 300                                                                |    :width: 300                                                                        |
|                                                                               |                                                                                       |
|    2D TOF MRA显示只有右椎动脉，左椎动脉无血流相关信号。                       |    对比增强MRA显示左椎动脉逆行填充（锁骨下动脉盗血现象）                              |
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

**百叶帘影（仅3D MRA）**

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_6717403_orig.jpg
   :alt: Venetian Blind Artifact 
   :align: right
   :width: 300

这是一个仅在MOSTA（Multiple Overlapping Thin Slab Acquisition，多重叠薄层采集）技术中可见的伪影。它代表了相邻层面之间的重叠，这些层面单独采集然后融合到一起。MOSTA技术在\ `另一个Q&A <http://mriquestions.com/motsa.html>`_\ 中有详细描述。  

**磁敏感伪影**

磁敏感指的是局部磁场扭曲，尤其是空气组织界面和金属物体附近。这些扭曲产生的磁场梯度会引起自旋加速失相位，信号损失和空间扭曲。在MRA中，磁敏感伪影常见于手术夹，血管内线圈和支架的周围。如果比较轻微，可能误诊为血管狭窄，如果比较严重，可能导致血流相关增强完全丢失，错误的提示为血管闭塞。

+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_2389462_orig.jpg| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_6753197_orig.jpg        |
|    :alt: Source image shows susceptibility field distortion                   |    :alt: MRA show spurious loss of flow                                               |
|    :width: 370                                                                |    :width: 370                                                                        |
|                                                                               |                                                                                       |
|    源图像显示动脉瘤夹导致磁敏感场扭曲                                         |    MRA显示由于动脉瘤夹导致的磁敏感伪影，右侧大脑中动脉供血区信号丢失                  |
+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

**参考材料**
     * Kaufman JA, McCarter D, Geller SC, Waltman AC. `Two-dimensional time-of-flight MR angiography of the lower extremities: artifacts and pitfalls <http://mriquestions.com/uploads/3/4/5/7/34572113/kaufman_artifacts_peripher_tof_ajr.pdf>`_. AJR Am J Roentgenol 1998; 171:129-135.

**相关问题**
	* `How does time-of-flight MRA work? <http://mriquestions.com/time-of-flight-tof-mra.html>`_