Question-动脉输入函数（AIF）：动脉输入函数是什么，为什么需要测量动脉输入函数？
==================================================================================

:date: 2015-10-22
:tags: Perfusion, DSC，AIF
:slug: arterial-input-aif
:authors: Chunshan
:summary: 动脉输入函数的意义及必要性

原文链接:\ `What is the arterial input function (AIF) and why do you need to measure it? <http://www.mri-q.com/arterial-input-aif.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/9274759_orig.png
    :alt: summary
    :align: center
    :width: 700

理想的DSC实验中，我们希望钆能够以短而紧凑的静脉推注递送到组织，然而实际上，血液要经过心脏和肺，最初的静脉推注变得延迟并且分散，DSC实验中测得的组织浓度曲线形状依赖于到达的动脉输入函数（AIF, Arterial Input Function， a(t)）的形状。如果没有AIF，组织灌注动力学中内在有价值的信息就可能会丢失。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8550739_orig.png?322
   :alt: tissue contrast concentration curve
   :align: right
   :width: 500

   组织对比剂浓度曲线c\ :sub:`tissue`\ (t) 的形状高度依赖于动脉输入函数的形状

获取AIF的最简单方法是使感兴趣区域能够覆盖一条容易识别的动脉，在腹部影像学检查中，可能是主动脉或肾动脉，在头部，往往主要是脑动脉（ACA, MCA）或其近侧分支。如果以这种方式得到的AIF应用于一个片层内的所有体素，称之为全局AIF(Global AIF)。但是测得的AIF位置与感兴趣体素的位置距离可能比较远，对比剂团注的延迟和分散在计算血流量时会产生明显的错误。潜在更好的方法是从与每一个成像的组织体素很近的小动脉中识别局部AIF（Local AIF），这也是过去十年众多研究的主题。

现在的灌注软件包提供了自动或半自动的方法来识别最优的局部AIF，下图所示的例子中，从大脑一个小区域可能的AIF数组中可以选出最佳的候选者。被选为AIF的体素理想上有比较平坦的基线，陡峭的峰，和紧凑的形状。下图的例子中，第二（或第三）列的体素可能是最佳选择。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/217349_orig.gif?387
   :alt: choose AIF from Voxel-by-voxel interrogation
   :align: center
   :width: 600

   逐个体素查询来确定大脑中动脉附近1cm\ :sup:`2`\ 区域的最优AIF。最优AIF一般有平坦的基线和陡峭的峰

一旦选择了合适的AIF，软件就可以产生每个像素的重要灌注参数，形成参数图，包括血容量，血流量和平均通过时间。这是如何完成的是下一个Q&A的主题。

**参考材料**
    * Bleeker EJW, van Buchem MA, van Osch MJP. `Optimal location for arterial input function measurements near the middle cerebral artery in first-pass perfusion MRI <http://www.mri-q.com/uploads/3/2/7/4/3274160/bleeker_2009.pdf>`_. J Cereb Blood Flow Metab 2009; 29:840-852. (Best location for the AIF may be just outside the MCA, not within it).
    * Calamante F, Mørup M, Hansen LK. `Defining a local arterial input function for perfusion MRI using independent component analysis <http://www.mri-q.com/uploads/3/2/7/4/3274160/calamante_et_al-2004-magnetic_resonance_in_medicine.pdf>`_. Magn Reson Med 2004; 52:789-797.
    * Carroll TJ, Rowley HA, Haughton VM. `Automatic calculation of the arterial input function for cerebral perfusion imaging with MR imaging <http://www.mri-q.com/uploads/3/2/7/4/3274160/automated_aif_radiol2e2272020092.pdf>`_. Radiology 2003; 227:593-600.
    * Mlynash M, Eyngorn I, Bammer R, et al. `Automated method for generating the arterial input function on perfusion-weighted MR imaging: validation in patients with stroke <http://www.mri-q.com/uploads/3/2/7/4/3274160/automated_aif_ajnr1479.full.pdf>`_. AJNR Am J Neuroradiol 2005; 26:1479-1486. (Computers generally due a more consistent/reliable job of finding the best AIF than people!)

**相关问题**
	* `Question-DSC高级处理：如何使用动脉输入函数从DSC数据中提取更多量化的血流信息？ <http://chunshan.github.io/MRI-QA/dsc/quantitative-dsc.html>`_ 