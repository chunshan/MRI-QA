Question-灌注方法：灌注（Perfusion）如何定义和测量？
=====================================================

:date: 2015-10-09
:tags: Perfusion, DSC
:slug: measuring_perfusion
:authors: Chunshan
:summary: 灌注（Perfusion）如何定义和测量

.. _measuring_perfusion:

原文链接:\ `How is perfusion defined and measured? <http://www.mri-q.com/measuring-perfusion.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4131569_orig.png?323
    :alt: summary
    :align: center
    :width: 700

灌注是指通过一个器官或组织的毛细血管循环的血流量。考虑到器官的大小不同，灌注的量化通常需要归一化，血流量（mL/min）除以器官质量（每100g），所以灌注的单位一般被表示为mL/min/100g。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/__9552085_orig.jpg
   :alt: maps from ASL
   :align: right
   :width: 300

   脑的动脉自旋标记的灌注参数图，有血管性脑胶质瘤 

不同的器官灌注情况不同，而且对同一器官，灌注也会随着其病理改变或代谢需要而改变。例如，脑灰质和白质灌注分别约60和20mL/min/100g。心肌灌注则大得多，休息时约100mL/min/100g，最大运动时可达400mL/min/100g。

灌注的测量需要使用示踪剂（分子，分子聚集体或小颗粒），示踪剂与血流充分混合，分布在组织中并且可以被检测。一些示踪剂会留在血管内，其他的示踪剂则分布更加广泛。示踪剂可分为：

1. 血管内示踪剂，限制在血管中。用于MR的血管内示踪剂包括钆膦维司（Ablavar，与血清白蛋白结合）和超小超顺磁性铁氧化合物分子（USPIO）。
2. 细胞外示踪剂，不进入细胞，但可自由地通过血管壁，分布在组织的细胞外空间。大多数钆基造影剂属于此类。
3. 可扩散示踪剂，分布在组织所有部位，包括细胞内。通常用于MRI的可扩散示踪剂是磁标记的水分子，用于动脉自旋标记（ASL，arterial spin labelling ）。

**高级讨论**

* 血管内示踪剂

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6278820_orig.jpeg?287
   :alt: 15 μm diameter injectable microspheres
   :align: right
   :width: 400

   实验室灌注测量使用的约15微米直径的可注射微球体

虽然没有完美的方法，传统测量组织灌注的实验室“金标准”是动脉内注射约15微米直径的微球体，这些颗粒会被困毛细血管床处，困住的比例与局部血流量呈正比，然后采集解剖标本，使用光学或电子学显微镜对颗粒计数，也可以对微球体进行放射性或者荧光标记从而能够使用半自动计数方法。

由于上述方法需要插入动脉导管收集组织进行测量，实验室微球体对于常规临床灌注是不可行的。然而有几种能够被无创影像学方法检测的微球体已经被开发出来用于临床，最常见的有放射性同位素标记的血细胞，大颗粒聚合白蛋白（核医学）和包膜微泡（超声），但还没有真正市售的微球体用于MR灌注成像。钆膦维司（ablavar）与血清白蛋白结合并且在注射后几小时都会局限于血管内空间，与上述微球体性质相仿。超小超顺磁性铁氧化合物（USPIO）粒子也在MR成像中被尝试使用以达到类似目的。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/__7081247_orig.gif
   :alt: Cine images from 1st pass myocardial perfusion study
   :align: right
   :width: 400

   首过法心肌灌注检查的电影图像，使用饱和恢复的扰相GRE序列

* 细胞外示踪剂

CT灌注成像和MR灌注成像中分别广泛使用碘基和钆基造影剂作为示踪剂，这些低分子量（500-1000Da）化合物注射后最初分布在血浆中，随即很快扩散到大多数组织的细胞外空间。唯一的例外是在中枢神经系统中，沿血脑屏障紧密的内皮细胞连接会阻断细胞外通道，阻止造影剂进入正常的大脑和脊髓。虽然一些新的专门的MR造影剂（如gadoxetate/eovist）有肝摄取，大部分造影剂不能进入正常细胞，局限在细胞外空间中。

*  可扩散示踪剂

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6118682_orig.jpg
   :alt: measuring blood flow noninvasively.
   :align: right
   :width: 300

   基于\ :sup:`15`\ O水的PET是无创测量血流量最准确的方法

自由扩散的示踪剂是放射性或磁性标记的离子或能在细胞内外轻松穿梭的小分子。在核医学（PET）中众所周知的有\ :sup:`15`\ O标记的O\ :sub:`2`，H\ :sub:`2`\ O，CO\ :sub:`2`; \ :sup:`13`\ NH\ :sub:`2`; \ :sup:`82`\ Rb; \ :sup:`201`\ TI. 另一种扩散性示踪剂，吸入性疝气，用于CT灌注成像，曾经在20世纪90年代获得一定的关注，现在已经基本被抛弃了。MRI中磁标记的水分子被广泛用作扩散性示踪剂，这也是动脉自旋标记（ASL）技术的基础。

使用\ :sup:`15`\ O的PET通常被认为是无创测量大多数器官灌注的金标准。但这是一项繁琐的技术，需要在线产生示踪剂，然后通过连续动脉采血输送给病人。这不是一个完美的解决方案，受部分容积效应的影响尤其在小且复杂的大脑结构周围。相比于微球体，基于\ :sup:`15`\ O水的PET往往会低估高流量时的灌注而高估低流量时的灌注。

使用\ :sup:`15`\ O水的PET和使用DSC或ASL的MR灌注的详细比较几乎没有。已经进行的研究表明，MR灌注方法具有可重复性，能够获得血流量可靠的定性信息，准确的定量测量是可能的但是具有挑战性，依赖于MR成像方法（DSC或ASL）和使用的复杂数学模型。   

**参考材料**
     * Cuenod CA, Balvay D. `Perfusion and vascular permeability: basic concepts and measurement in DCE-CT and DCE-MRI <http://www.mri-q.com/uploads/3/2/7/4/3274160/permeability_1-s2.0-s2211568413003306-main.pdf>`_. Diagn Interven Imaging 2013; 94:1187-1204. (Good review of basic mechanisms; some terminology is slightly different than abbreviations used in Tofts models).          
     * Frackowiak RSJ, Lenzi G-L, Jones T, Heather JD. `Quantitative measurement of regional cerebral blood flow and oxygen metabolism in man using 15O and positron emission tomography: theory, procedure, and normal values <http://www.mri-q.com/uploads/3/2/7/4/3274160/quantitative_measurement_of_regional_cerebral.1.pdf>`_. J Comput Assist Tomogr 1980; 4:727-736.  
     * Ito H, Inoue K, Goto R, et al. `Database of normal human cerebral blood flow measured by SPECT: I. Comparison between I-123-IMP, Tc-99m-HMPAO, and Tc-99m-ECD as referred with O-15 labeled water PET and voxel-based morphometry <http://www.mri-q.com/uploads/3/2/7/4/3274160/brain_tracers_nuc_med.pdf>`_. Ann Nucl Med 2006; 20:131-138. 
     * Prinzen FW, Bassingthwaighte JB. `Blood flow distributions by microsphere deposition methods <http://www.mri-q.com/uploads/3/2/7/4/3274160/microspheres.pdf>`_. Cardiovasc Res 2000; 45:13-21. 
     * Salerno M, Beller GA. `Noninvasive assessment of myocardial perfusion <http://www.mri-q.com/uploads/3/2/7/4/3274160/circ_cardiovasc_imaging-2009-salerno-412-24.pdf>`_. Circ Cardiovasc Imaigng 2009; 2:412-424. (comparison of different imaging methods for myocardial perfusion measurement) 
     * Zhang K, Herzog H, Mauler J, et al. `Comparison of cerebral blood flow acquired by simultaneous [15O]water positron emission tomography and arterial spin labeling magnetic resonance imaging <http://www.mri-q.com/uploads/3/2/7/4/3274160/jcbfm201492a.pdf>`_. J Cerebr Blood Flow Metab 2014; 34:1373-1380.

**相关问题**
	* `Can myocardial perfusion be accurately quantified?  <http://www.mri-q.com/quantifying-perfusion.html>`_
	* `What are the differences between DSC, DCE and ASL perfusion methods used in MRI?  <http://www.mri-q.com/dsc-v-dce-v-asl.html>`_