Question-化学位移伪影：什么是化学位移伪影（Chemical Shift Artifacts）？
================================================================================

:date: 2015-11-20
:tags: MR Artifacts, tissue related artifacts
:slug: chemical-shift-artifact
:authors: Chunshan
:summary: 什么是化学位移伪影？

.. |imagecomments1| replace:: 膝关节内的轻微化学位移伪影。频率编码方向从左到右，软骨厚度差异很明显是伪影造成的，伪影来自骨髓脂肪信号移位。肌肉与脂肪边界的化学位移伪影。

.. |imagecomments2| replace:: 脊柱上一个类似的轻微伪影，频率编码方向从S到I。椎骨的皮质厚度改变是由骨髓和椎间盘之间的化学位移伪影造成的。

.. |RST| replace:: reStructuredText

原文链接:\ `What is a chemical-shift artifact? <http://www.mri-q.com/chemical-shift-artifact.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/989884_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3915690_orig.gif
   :alt: Deshielding of the ¹H nuclei of water
   :align: left
   :width: 200

   不受屏蔽的水中\ :sup:`1`\ H原子

化学位移指的是由于原子核分子环境的不同导致的共振频率的微小变化。例如，脂肪的\ :sup:`1`\ H质子，遮蔽在长链甘油三酯中，被电子云覆盖。这些电子云部分屏蔽了外部施加磁场对脂肪中质子的影响。然而，水中的\ :sup:`1`\ H质子受到的遮蔽比较少，因为电子云被带高度负电的氧原子拉走了。

由于电子云屏蔽程度不同，脂肪中质子受到的局部磁场会比周围水分子中的质子略弱一点，其共振频率也会略低。共振频率的差异非常小，在百万分（ppm）之3.4的级别（3.4 x 10-6），1.5T时引起的绝对频率差异约215Hz，3.0T时绝对频率差异会是1.5T时的两倍，约430Hz。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5401883_orig.gif?363
   :alt: chemical shift artifacts
   :align: right
   :width: 400

常规磁共振成像中，空间位置根据共振频率不同沿频率编码方向排列。如果一个体素中既有水又有脂肪，脂肪质子发出的信号会比水中质子发出的信号频率略低。

因此，如果系统频率设置为水的共振频率，脂肪质子产生的信号看起来像梯度磁场低部区域另一个体素中的水质子产生的。当图像强度值被填到最终的图像中，脂肪质子位置将会朝着读出梯度磁场低部方向产生空间上的映射错误。

脂肪和水之间的像素映射错误导致白带或暗带伪影，伪影有一至几个像素宽，分布在解剖对象两边。这种伪影通常见于脂肪包围的含水器官（如肝脏，肾脏，视神经，硬膜囊，肌肉，神经束）。下图中暗带出现在每个肾的左边，白带出现在右边。暗带出现在哪边取决于频率编码梯度在图像上从左到右是升高还是降低。在下图肾脏，膝盖和腿的例子中，频率从左向右升高。硬膜囊的图像则不同，频率从左向右降低。因此暗的化学位移带出现在硬膜囊的左侧。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6071647_orig.jpg?562
   :alt: chemical shift artifacts of kidney
   :align: center
   :width: 700

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/9440894_orig.gif?294 | .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8931344_orig.gif?274  |
|    :alt: Chemical shift artifact between spinal fluid and epidural fat        |    :alt: Chemical shift artifact at border of muscle and fat                   |
|    :width: 350                                                                |    :width: 350                                                                 |
|                                                                               |                                                                                |
|    脊髓液与硬膜外脂肪间的化学位移伪影                                         |    肌肉与脂肪边界的化学位移伪影                                                |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

骨的边缘处髓脂肪与含水的关节囊或椎间盘毗连，也会发生轻微的化学位移伪影，看起来像皮质厚度改变了。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/729234_orig.jpg?296  | .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5041739_orig.gif?207  |
|    :alt:  Subtle chemical shift artifact in the knee.                         |    :alt: A similar subtle artifact in the spine.                               |
|    :width: 350                                                                |    :width: 300                                                                 |
|                                                                               |                                                                                |
|    |imagecomments1|                                                           |    |imagecomments2|                                                            |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+


化学位移伪影的大小可以根据两个选定的参数在成像之前很容易地预先计算出来，这两个参数是接收器带宽和频率编码矩阵的大小。比如，如果接收器总带宽为32kHz，频率编码方向有256个像素，每个像素的带宽是32000/256 = 125Hz。由于脂肪-水的共振频率在1.5T下相差约215Hz，化学位移伪影大小约 (215 Hz) ÷ (125 Hz/pixel) = 1.7个像素。

减少每个像素所占带宽会加重化学位移伪影。一般而言，在化学位移伪影会使重要交界处模糊的位置（如视神经和眼眶脂肪交界处），应尽量避免使用窄带技术。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/1181678_orig.jpg?367
   :alt: Chemical shift artifact at junction between water droplets and silicone gel 
   :align: right
   :width: 500

   一个破裂的乳房假体（“沙拉油征”）中，水和硅胶交界处的化学位移伪影。

由于化学位移伪影是基于频率的MR信号的空间映射错误，因此一般出现在频率编码方向。回波平面成像（EPI）中情况有所不同，化学位移伪影出现在相位编码方向。见下一个Q&A。

此外，在2DFT成像中，层面选择由变化的频率定义。这种采集方法中，化学位移伪影不仅发生在成像平面内，也发生在成像平面间（层面选择方向）。层面间的化学位移伪影表现为一定解剖结构周围或亮或暗的“光环”，其他形式不太明显，但会造成图像质量的轻微下降。

最后，应该注意化学位移伪影不仅发生在水和脂肪之间，而是在任何有不同化学位移的两种物质交界处。例如，硅油（用于眼科）和水之间的化学位移约4.4ppm，硅凝胶（用于乳房假体）和水之间化学位移约1.7ppm，因此化学位移伪影也会出现在乳房，头部，颈部和四肢，这些部位使用硅胶注射物或植入物比较普遍。

**参考材料**
     * Babcock EE, Brateman L, Weinreb JC et al. `Edge artifacts in MR images: chemical shift effect <http://www.mri-q.com/uploads/3/2/7/4/3274160/edge_artifacts_in_mr_images__chemical_shift_effect.4.pdf>`_. J Comput Assist Tomogr 1985; 9:252-257. (One of the first descriptions of this artifact)
     * Dwyer AJ, Knop RH, Hoult DI. `Frequency shift artifacts in MR imaging <http://www.mri-q.com/uploads/3/2/7/4/3274160/frequency_shift_artifacts_in_mr_imaging_.3.pdf>`_. J Comput Assist Tomogr 1985;9:16-18.
     * Hood MN, Ho VB, Smirniotopoulos JG, Szumowski J. `Chemical shift: the artifact and clinical tool revisited <http://www.mri-q.com/uploads/3/2/7/4/3274160/hood_chemical_shiftradiographics2e192e22eg99mr07357.pdf>`_. Radiographics 1999; 19:357-371 (Excellent review).     
     * Mathews VP, Elster AD, Barker PB, et al.  `Intraocular silicone oil: in vitro and in vivo MR and CT characteristics <http://www.mri-q.com/uploads/3/2/7/4/3274160/intraocular_silicone_article.pdf>`_. AJNR Am J Neuroradiol 1994; 15:343-7. 
     * Smith RC, Lange RC, McCarthy SM. `Chemical shift artifact: dependence on shape and orientation of the lipid-water interface <http://www.mri-q.com/uploads/3/2/7/4/3274160/chem_shift_orientationradiology2e1812e12e1887036.pdf>`_. Radiology 1991; 181:225-229.

**相关问题**
	* `水和脂肪质子的化学位移难道不会导致它们之间的相位变化么？如果如此，为什么化学位移伪影在相位编码方向没有出现？ <http://chunshan.github.io/MRI-QA/tissue-related-artifacts/chemical-shift-in-phase.html>`_