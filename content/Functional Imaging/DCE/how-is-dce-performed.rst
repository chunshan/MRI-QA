Question-DCE脉冲序列：使用什么脉冲序列进行DCE检查？
======================================================================================

:date: 2015-10-25
:tags: Perfusion, DCE
:slug: how-is-dce-performed
:authors: Chunshan
:summary: 进行DCE检查的序列

原文链接:\ `What pulse sequences are used to perform a DCE study? <http://www.mri-q.com/how-is-dce-performed.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6242819_orig.png
    :alt: summary
    :align: center
    :width: 700

任何器官都可以做DCE成像，但是通常会用于脑，心脏，乳腺，肝脏，前列腺和肾脏。DCE一般使用表现为T1加权的3D扰相梯度回波技术，但不同应用使用的序列结构和脉冲时序参数也有稍微的不同。心脏灌注序列有一些独特的特性，在前面的Q&A中已经有描述。

用于脑，乳腺或前列腺DCE的典型脉冲序列可能规定使用如下参数：3D SPGR或FLASH序列，TR = 4-6毫秒，TE = 1-3毫秒，flip angle = 10°-15°，并行加速系数 = 2。

扫描的视场（FOV， Field of View），层厚，层数，成像矩阵大小取决于不同的应用。乳腺和前列腺的DCE检查通常是为了发现小病灶，这些检查一般要求层厚≤ 3 毫米，平面内像素尺寸≤ 1平方毫米。大脑DCE成像可能对空间分辨率要求不这么苛刻，层厚可以大至5毫米，像素尺寸也可以大50%。

不同的器官系统，不同的图像分析类型，要求的时间分辨率（不同时相的间隔时间）和总成像时间有明显不同。空间分辨率和时间分辨率之间的权衡总是存在的。

乳腺MRI一般只会进行半定量的DCE分析，通常每1½−2分钟采集一次，共持续5-7分钟。前列腺肿瘤通常比乳腺肿瘤对对比剂吸收和冲洗（流出）更快，前列腺DCE的时间分辨率要求更高，图像在注射造影剂后必须至少每10s采集一次，持续约5分钟。

脑DCE成像往往是为了获得基于药代动力学模型的组织灌注参数，这样一个完整的定量分析通常需要打造影剂前扫描额外的T1映射协议。T1映射协议可以是一个Look-Locker类型序列（见相关的Q&A）或者是一系列使用不同翻转角度和回波时间采集的容积数据。T1映射协议完成后，与上面类似的3D扰相梯度回波序列就开始运行，时间分辨率约为5s，数据采集至少5分钟。

**参考材料**
    * Buckley DL, Roberts C, Parker GJM, et al. `Prostate cancer: evaluation of vascular characteristics with dynamic contrast-enhanced T1-weighted MR imaging — initial experience <http://www.mri-q.com/uploads/3/2/7/4/3274160/prostate_dce.pdf>`_. Radiology 2004; 233:709-715.
    * Choi YJ, Kim JK, Kim N, et al. `Functional imaging of prostate cancer <http://www.mri-q.com/uploads/3/2/7/4/3274160/prostate_functional_radiographics_review_g2e271065078.pdf>`_. RadioGraphics 2007; 27:63-77.  
    * Jahng G-H, Li K-L, Ostergaard l, Calamante F. `Perfusion magnetic resonance imaging: a comprehensive update on principles and techniques <http://www.mri-q.com/uploads/3/2/7/4/3274160/perfusion_review_article_kjr-15-554.pdf>`_. Korean J Radiol 2014; 15:554-577. (good recent review).
    * Larsson HB, Hansen AE, Berg HK, et al. `Dynamic contrast-enhanced quantitative perfusion measurement of the brain using T1-weighted MRI at 3T <http://www.mri-q.com/uploads/3/2/7/4/3274160/larsson_et_al-2008-journal_of_magnetic_resonance_imaging.pdf>`_. J Magn Resona Imaging 2008; 27:754-762
    * Sourbron S, Ingrisch M, Siefert A, et al. `Quantification of cerebral blood flow, cerebral blood volume, and blood-brain-barrier leakage with DCE-MRI <http://www.mri-q.com/uploads/3/2/7/4/3274160/sourbron_et_al-2009-magnetic_resonance_in_medicine.pdf>`_. Magn Reson Med 2009; 62:205-217.
    * Tofts PS. `T1-weighted DCE imaging concepts: modelling, acquisition and analysis <http://www.mri-q.com/uploads/3/2/7/4/3274160/dce-mri_siemens.pdf>`_. MAGNETOM Flash 2010; 3:30-35.
    * Verma S, Turkbey B, Muradyan N, et al. `Overview of dynamic contrast-enhanced MRI in prostate cancer diagnosis and management <http://www.mri-q.com/uploads/3/2/7/4/3274160/prostate_ajr2e122e8510.pdf>`_. AJR Am J Roentgenol 2012; 198:1277-1288. (Prostate DCE requires high temporal resolution, with images acquired every 5-10 sec for several minutes).

**相关问题**
	* `Question-乳腺DCE：乳腺DCE需要一些特殊的技术么？ <http://chunshan.github.io/MRI-QA/dce/breast-dce.html>`_  
	* `How is cardiac T1 mapping performed? When is it useful? <http://www.mri-q.com/t1-mapping.html>`_  