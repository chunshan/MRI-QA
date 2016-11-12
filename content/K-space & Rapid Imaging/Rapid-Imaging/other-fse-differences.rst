Question-CSE图像 vs FSE图像：除了明亮的脂肪信号，传统自旋回波和快速自旋回波之间图像属性上还有什么不同么？
=========================================================================================================================

:date: 2014-10-28
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: other-fse-differences
:authors: Chunshan
:summary: 除了明亮的脂肪信号，传统自旋回波和快速自旋回波之间图像属性上的不同

原文链接:\ `Besides bright fat, are there other differences in image properties between conventional spin echo and fast spin echo imaging? <http://www.mri-q.com/other-fse-differences.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/4457934_orig.png
    :alt: summary
    :align: center
    :width: 700

FSE/TSE图像上除了明显明亮一些的脂肪信号，与传统自旋回波成像相比，对比度上还有其他一些微小的差别。这些差别包括：1）对磁敏感的敏感性降低；2）磁化转移效应增强；3）边缘和对比度效应。

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/5745693_orig.jpg?241
   :alt: Conventional spin-echo image and fast spin-echo image
   :align: right
   :width: 400

   传统自旋回波（上）和快速自旋回波（下），TR/TE(eff)均为3000/80. 由红核处铁导致的磁敏感效应（箭头处）在CSE图像上更显著。

**对磁敏感的敏感性降低**

说明这种现象的一个例子是常规T2加权的大脑图像（右）。场强为1.0T或更高时，通常在基底节，黑质，红核可见低信号，因为这些结构的细胞内都有铁沉积。微观的铁沉积导致局部磁场扭曲，称为磁化率梯度。当水分子扩散通过这些梯度时，自旋失相位加速并且T2*缩短，降低了磁共振信号。

信号损失的程度取决于扩散的水在不均匀磁场中被180°脉冲重聚焦之前花费的时间。在CSE中，再回聚的时间由回波时间（TE）决定，一般50ms或更长；然而在FSE中，180°回聚脉冲间隔时间很短，由ESP（回波时间间隔，通常5-10ms）决定，由磁敏感性导致的失相位时间更短。

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/8820678_orig.jpg
   :alt: Conventional spin-echo image and fast spin-echo image
   :align: left
   :width: 450

   与CSE图像（左）相比，FSE图像（右）上暗出血灶能见度降低（来自Reimer等，经过许可）

磁敏感性降低使得FSE成为外科手术硬件或金属异物存在时首选序列，可以显著降低伪影。然而，当需要检测组织中磁敏感性的变化进行诊断时，这个优势有时也会变为劣势，如钙化或出血的检测。

|
|
|

**磁化转移效应增强**

如在 `前面一个Q&A中 <http://www.mri-q.com/magnetization-transfer1.html>`_ 所描述的，磁化转移是自由水的自旋与结合水和生物大分子的自旋交换能量的过程。FSE中的多个180°回聚脉冲使得大分子偏共振饱和，其饱和过程是渐进的。在脑组织的大分子中，有T2非常短的髓磷脂和膜磷脂，它们不直接成像。随着脉冲数目的增加，磁化转移效应变得更加显著，特别是白质明显变暗，灰质也有小的信号损失。相反，脑脊液和脂肪的信号不会被抑制，这些物质看起来比大脑组织更亮。

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/1304832_orig.gif?610
   :alt: Magnetization transfer effects
   :align: center
   :width: 800

   磁化转移效应体现在随着ETL的增加，白质信号不断降低

**边缘和对比度效应（k空间滤波）**

如上面的例子说明的，FSE和CSE相似但脉冲序列的结构并不相同，即使使用相同的TR，而且TE=TEeff，不同组织的相对信号强度也会不一样。我们已经描述了几种物理现象（J偶联的瓦解，对磁敏感性的灵敏度降低和磁化转移），能够解释其中的一些差异。

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/2886353_orig.gif?423
   :alt: k-space filtering
   :align: right
   :width: 450

   k空间滤波。k空间中的每一条线在T2衰减曲线的不同点山采集，意味着图像对比度在采集期间不断变化

另外一个重要的现象（适用于FSE和所有的快速/平面回波技术）称为k空间滤波。基本思想是T2衰减发生在每个TR间隙k空间的线被填充时，每一个回波在T2衰减曲线不同的时间点上被采集。因此，k空间中线的加权并不一致，图像对比度在采集期间不断变化。

图像的整体对比度由k空间中心（TEeff）附近采集的数据决定，k空间外围早期或后期的回波反应高空间频率信息。这些外围的线在不同的TE值时采集得到，其信号强度受T2衰减的调制，会导致图像的模糊。采集的回波越多（ETL越长），模糊效应越明显。

当TEeff比较短时空间模糊效应最明显，因为提供边缘细节的高阶相位编码步骤使用回波链后期的回波进行填充。因此，T1和质子密度加权像的模糊效应最明显。一个好的临床引例是FSE的质子密度加权像上轻微的膝盖半月板撕裂可能会被模糊掉，从而影响临床诊断。

流体（如CSF）的T2弛豫时间比较长，因此早期和后期回波的信号强度变化相对比较小，T2长的物质在T2加权的FSE成像中由k空间导致的模糊几乎不是问题。但是对多数固体组织，T2比较短，早期和后期回波的信号强度差异比较大，T2加权的FSE图像上固体短T2组织的空间模糊更显著。这样的模糊可能会导致不能检测T2值与周围背景接近的小物体或者小病变。

当长T2和短T2组织共存时，就会发生一种称为伪边缘增强的反常现象。伪边缘增强通常见于腰椎轴状位T2加权的FSE图像，表现为围绕神经根的白色“光环”。

下面说明其机制，并且展示神经根和脑脊液（CSF）被模糊（改变了图像的点扩散函数）的结果。CSF固有的T2比较长，没有显示多少模糊，而神经根（T2比较短）的模糊比较明显。神经根模糊的信号溢出到相邻高信号的CSF，增加了附近的亮度。即使没有可见的光环，伪边缘增强解释了FSE图像上硬膜囊的神经根为什么如此锐利。

+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/3516459_orig.gif?280    | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/978683_orig.gif          |
|    :alt: pseudo-edge enhancement                                                  |    :alt: pseudo-edge enhancement                                                   |
|    :width: 400                                                                    |    :width: 400                                                                     |
|                                                                                   |                                                                                    |
|                                                                                   |    伪边缘增强导致腰椎神经根周围出现白色光环（箭头处）。                            |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

**参考材料** 
     * Garyun BB, Major NM, Helms CA. `Comparison of fast spin-echo versus conventional spin-echo MRI for evaluating meniscal tears <http://www.mri-q.com/uploads/3/4/5/7/34572113/fse_meniscus_ajr.pdf>`_. Am J Roentgenol 2005; 184:1740-1743.
     * Jones KM, Mulkern RV, Mantello MT, et al. `Brain hemorrhage: evaluation with fast spin-echo and conventional dual spin-echo images <http://www.mri-q.com/uploads/3/4/5/7/34572113/jones_hemorrhage_radiology2e1822e12e1727309.pdf>`_. Radiology 1992;182:53-58.
     * Reimer P, Allkemper T, Schuierer G, Peters PE. `Brain imaging: reduced sensitivity of RARE-derived techniques to susceptibility effects <http://www.mri-q.com/uploads/3/4/5/7/34572113/brain_imaging__reduced_sensitivity_of_rare-derived_technique...pdf>`_. J Comput Assist Tomogr 1996;20:201-205.  
     * Tartaglino LM, Flanders AE, Vinitski S, et al: `Metallic artifacts on MR images of the postoperative spine: Reduction with fast spin-echo techniques <http://www.mri-q.com/uploads/3/4/5/7/34572113/metal_artifact_reduction_radiology2e1902e22e8284417.pdf>`_. Radiology 1994;190:565-569.
     * Thomas DL, De Vita E, Roberts S, et al. `High-resolution fast spin-echo imaging of he human brain at 4.7T: implementation and sequence characteristics <http://www.mri-q.com/uploads/3/4/5/7/34572113/fse_4.7t_nihms-118.pdf>`_. Magn Reson Med 2004;51:1254-1264.

**相关问题**
	* `What is magnetization transfer? <http://www.mri-q.com/magnetization-transfer1.html>`_