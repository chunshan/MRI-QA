Question-磁敏感性伪影：什么是磁敏感性伪影（susceptibility artifacts）？
=====================================================================================

:date: 2015-11-26
:tags: MR Artifacts, tissue related artifacts
:slug: susceptibility-artifact
:authors: Chunshan
:summary: 什么是磁敏感性伪影（susceptibility artifacts）？

原文链接:\ `What are susceptibility artifacts? <http://www.mri-q.com/susceptibility-artifact.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/5213849_orig.png?292
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/3875578_orig.gif?325
   :alt: diamagnetic，paramagnetic
   :align: left
   :width: 400

磁敏感性(χ)衡量一种物质放置到外部磁场中时被磁化的程度。使主磁场分散的材料称为抗磁性材料，使主磁场集中的材料根据影响的程度不同可分为顺磁性材料，超顺磁性材料或铁磁性材料。

钙盐（见于骨皮质）是人体中最强的抗磁性物质。几乎所有的生物组织（肌肉，脂肪，脑，肝，水）都是抗磁性的，但是比较弱。令人惊讶的是，空气不是磁敏感中性的，而是由于氧分子的存在略微显顺磁性。组织中如果存在金属离子（如Fe,Mn,Gd）会产生弱顺磁性。铁蛋白和含铁血黄素颗粒中的铁累积为微球状，产生更强的正磁敏感性效应称为超顺磁性。含Fe,Co,Ni的固体金属物体（如假体，手术夹。螺钉）有最强的磁敏感性效应，称为铁磁性材料。

磁敏感性效应导致的磁场扭曲会导致患者体内不同部位的进动频率变化，甚至单个体素内进动频率也会发生变化。进动频率的改变，反过来会导致T2*失相位和空间失配造成磁共振信号的损失。磁共振成像的特点反映了这两种物理机制：几何失真造成的焦点区域信号缺如和分配到错误区域的“打桩”信号导致部分区域非常明亮。下面是不同部位磁敏感性伪影的图片库。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/1430090_orig.jpg    | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/9604598_orig.gif     | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/3909095_orig.gif     | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/3453224_orig.gif     |
|    :alt: Susceptibility artifacts from screws in femur                        |    :alt: "Potato chip" slice position artifact due to shunt                    |    :alt: Susceptibility artifact at skull base on DW image                     |    :alt: Focal sellar suceptibility artifact that may mimic an adenoma         |
|    :width: 200                                                                |    :width: 200                                                                 |    :width: 200                                                                 |    :width: 200                                                                 |
|                                                                               |                                                                                |                                                                                |                                                                                |
|    股骨螺钉导致的磁敏感性伪影                                                 |    因分流导致的“土豆片”伪影                                                    |    颅底处DWI上的磁敏感性伪影                                                   |    焦鞍处可能一个腺瘤导致的敏感性伪影                                          |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/6164313_orig.jpg    | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/8062510_orig.gif     | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/4756973_orig.jpg     | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/558584_orig.jpg      |
|    :alt: Susceptibility-induced signal loss                                   |    :alt: Susceptibility artifact from pedicle screws                           |    :alt: Susceptibility artifact due to iron particles in mascara              |    :alt: Susceptibility artifact due to braces                                 |
|    :width: 200                                                                |    :width: 200                                                                 |    :width: 200                                                                 |    :width: 200                                                                 |
|                                                                               |                                                                                |                                                                                |                                                                                |
|    海绵状血管瘤周围含铁血黄素引起的信号损失                                   |    椎弓根螺钉引起的磁敏感性伪影                                                |    睫毛膏中的铁粒子引起的磁敏感性伪影                                          |    牙箍引起的磁敏感性伪影                                                      |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

由于铁磁性材料有最强的磁敏感性效应，磁场扭曲和磁共振伪影通常围绕金属物和植入物非常明显。比较微妙的磁敏感性扭曲可见于一些人体组织交界处（如骨小梁、鼻窦、颅底，和蝶鞍）。伪影的形状（弥散性或局灶性）和强度（高或低）依赖于局部解剖关系，磁场强度，磁敏感性差异，回波时间（TE）还有带宽（读出梯度场强度和方向）。关系用下式表示：

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/561721.jpg?440
   :alt: susceptibilities format
   :align: center
   :width: 600

由于磁敏感性伪影在高场强下更差，应尽可能避免在3.0T下扫描带金属植入物的患者。通过交换频率编码和相位编码的方向，磁敏感性伪影会有形状上的变化，但并不会消除。使用更短的TE（失相位时间更短），使用快速自旋回波代替梯度回波序列能够最小化磁敏感性伪影。给定视野（Field Of View，FOV）时增加梯度场强度，避免使用窄带技术也可以减少磁敏感性伪影。使扫描的片层更薄和使用并行成像技术对减少伪影也有帮助。更严重的金属伪影可以通过使用特定的金属伪影消除序列降低（在下一个 `Q&A <http://www.mri-q.com/metal-suppression.html>`_ 中讨论）。

**参考材料**
     * Elster AD.  `Sellar susceptibility artifacts: theory and implications <http://www.mri-q.com/uploads/3/4/5/7/34572113/sellar_suscp_ade.pdf>`_.  AJNR Am J Neuroradiol 1993; 14:129-136. (Explains the physical basis of an artifact at the skull base that can mimic a pituitary adenoma).
     * Liu H, Martin AJ, Truwit C. `Interventional MRI at high field (1.5T): needle artifacts <http://www.mri-q.com/uploads/3/4/5/7/34572113/blooming_ball_artifact.pdf>`_. J Magn Reson Imaging 1998; 8:214-9. (Explains the physical basis of the "blooming ball" artifact at the end of biopsy needles directed parallel to the Bo field).
     * Port JD, Pomper MG. `Quantification and minimization of magnetic susceptibility artifacts on GRE images <http://www.mri-q.com/uploads/3/4/5/7/34572113/quantification_and_minimization_of_magnetic.24.pdf>`_. J Comput Assist Tomogr 2000;24:958-964.
     * Schenck JF. `The role of magnetic susceptibility in magnetic resonance imaging: MRI magnetic compatibility of the first and second kinds <http://mri-q.com/uploads/3/4/5/7/34572113/schenck-suscept.pdf>`_. Med Phys 1996;23:815-850. (Slightly dated, but an excellent and enduring explanation of susceptibility from a pioneer in MRI and first inductee in GE's Genius Hall of Fame).  

**相关问题**
	* `What is magnetic susceptibility? <http://www.mri-q.com/what-is-susceptibility.html>`_
	* `What causes susceptibility? <http://www.mri-q.com/causes-of-susceptibility.html>`_
	* `我们最近为一个扫描仪买了金属伪影抑制软件。它的工作原理是什么？ <http://chunshan.github.io/MRI-QA/tissue-related-artifacts/metal-suppression.html>`_