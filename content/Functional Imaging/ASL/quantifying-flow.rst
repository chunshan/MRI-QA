Question-血流量化 - ASL方法如何用于血流量化？
=======================================================================================

:date: 2015-11-11
:tags: Perfusion, ASL
:slug: quantifying-flow
:authors: Chunshan
:summary: ASL方法如何用于血流量化

原文链接:\ `How are ASL methods able to quantify blood flow? <http://www.mri-q.com/quantifying-flow.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5480047_orig.png?323
    :alt: summary
    :align: center
    :width: 700

像从其他MR方法获得灌注信息一样，从ASL中获取血流定量信息是梦寐以求却很难实现的目标。信号强度差分（ΔS = Scontrol - Sinversion）仅提供了灌注加权的图像，将这种原始数据转化为绝对的血流定量参数需要三个步骤：1）图像处理和滤波以去除伪影；2）获取单独的一个质子密度（PD）或者T1加权参数图用于归一化信号强度；3）根据一个数学模型拟合数据逐个像素计算血流信息。

**图像处理和滤波**

在试图获取血流的定量信息之前，需使从ASL方法得到的原始数据尽可能变得“干净”。在标记序列和控制序列之间患者一般会有一定程度的运动，因此刚体运动校正技术一般会与互配准和基于高斯平滑滤波器的“去噪”技术一起使用，也有可能会分割出灰质和白质图像，然后分别处理使得部分容积效应最小。

异常值分析可以辨认更严重和随机的误差（如右侧显示的梯度故障），当控制像和标记像之间的差值超过某一设定的阈值时可以丢弃掉。通常产生椭圆形的“mask”用于排除大脑之外的体素，也可以使用独立成分分析的统计学方法进一步减少噪声。

+--------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5269099_orig.png| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4135157_orig.png?281  |
|    :alt: Temporary gradient malfunction corrupts ASL raw data image      |    :alt: Corrected by excluding affected data during postprocessing            |
|    :width: 300                                                           |    :width: 300                                                                 |
|                                                                          |                                                                                |
|    短暂的梯度故障导致ASL原始数据被破坏                                   |    后处理过程中去除受影响数据进行校正                                          |
+--------------------------------------------------------------------------+--------------------------------------------------------------------------------+

**用于归一化的校准图像**

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3207584_orig.jpg?130
   :alt: PD calibration image
   :align: left
   :width: 200 

   质子密度校准图像

为了能够量化血流信息，任意的灌注加权图像中的ASL信号强度必须归一化到M0b，也就是动脉血的平衡磁化强度。理论上，M0b可以从一个单纯的动脉体素测定，但这是不现实的，因为血管可能非常小而且伴随部分容积效应。相反，M0b通常通过测量大脑或脑脊液的平衡磁化间接计算得到，这个过程需要单独获取大脑或脑脊液的质子密度（PD）加权像。质子密度数据转化为M0b需要校正TR，组织T1和血脑分配系数（λ）。

**数学建模与数据拟合**

最后一步是将滤波和校准后的ASL数据拟合到一个数学模型，逐个像素计算定量的血流参数。最广泛使用的Buxton的一般动力学模型，一个单室、活塞流模型，其中的参数使用线性系统方法进行估计，反卷积类似于\ `前面一个Q&A <http://chunshan.github.io/MRI-QA/dsc/quantitative-dsc.html>`_\ 中描述的DSC成像中使用的方式。

最终用于计算血流（F）的方程依赖于多个测量和估计的参数，还有精确的ASL脉冲序列。此处只是为了让读者感受一下复杂度，列出了GE系统中目前用于pCASL技术的方程，这个方程基于Alsop等的工作：

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/481951_orig.png?427
   :alt: 3D pCASL equation
   :align: center
   :width: 600 

个体参数包括：因子6000（转换单位为mL/min/100g组织）； λ为血组织分配系数（通常假设大脑为0.9）；TRPD为饱和恢复质子密度校正序列的重复时间；T1T和T1b为组织和血液的驰豫时间（通常假设3.0T下分别为1.2秒和1.6秒）；SIcont，SIinv和SIPD分别为相应的控制像，标记/反转像和质子密度加权像中像素的信号强度；PLD为标记后延迟时间，表示pCASL反转结束到图像采集之间的时间；LT为标记时间也就是pCASL反转的持续时间；α为pCASL反转的标记效率（通常假设为0.8）；σ为背景饱和脉冲的抑制效率（通常假设为0.75）；KSF为用于灌注加权序列的归一化因子；NEXPW为ASL序列的激发次数（取信号平均）。

这儿列出此方程的目的不是为了迷惑读者，而是为了说明需要假设或估计很多参数才能从ASL数据中计算真正的血流信息。这些参数中一个小的误差或方差可以很容易地改变最终计算结果的30%或更多。归一化因子可以凭经验调整使计算后的血流信息保持在预期的生理范围内，但我建议用户仍然要对由此获得的参数的准确性保持健康的怀疑态度。像其他的MR灌注方法，ASL血流测量最有意义的在于定性，与大脑（或其他器官）另一侧比较相应的区域。

**高级讨论**

在1922年CASL最初的描述中，Williams等通过修改布洛赫方程来解释组织之间纵向磁化交换（MT）和标记血液的磁化，这奠定了ASL定量分析的基础。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3114457_orig.png?400
   :alt: foundation for quantitative analysis of ASL
   :align: center
   :width: 600 

F是血流量，T1是无血流或血液-组织之间的物质交换时组织的纵向驰豫时间，MT0是在完全松弛条件下的组织磁化，Ma和Mv分别是动脉和静脉随时间变化的纵向磁化强度。

假设血液-组织之间的相互作用发生在一个单一的、充分混合的腔室内，流出系统的静脉血磁化强度为Mv = MT/λ，其中λ为血组织分配系数，也就是标记动脉中的水穿过组织后剩余的比例。对大脑而言，λ值一般取为0.9，这是从用15O水标记的PET研究中获得的灰质和白质的平均值。

随着连续而完全的动脉自旋反转，后续的MT采样会呈现指数衰减，时间常量为T1app，由下式给出：

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/1034204_orig.png?162
   :alt: T1app
   :align: center
   :width: 300 

血流量（F）的表达式可以根据实验测量的量推导得到：

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/5703370_orig.png?194
   :alt: F
   :align: center
   :width: 300 

其中，Mcont 和Minv分别是控制状态和反转（标记）状态中组织的信号强度。尽管T1app是F的函数，但它通常可以使用一个T1映射或估计程序单独测量得到。

1998年，Buxton等提出了一个更复杂的方法称为一般动力学模型，这个模型的一些版本仍是目前ASL分析最广泛使用的模型。Buxton分析使用与DSC成像中类似的线性系统方法。在继续之前，建议读者快速回顾前面Q&A中总结的DSC线性系统分析。

Buxton方法的基本结果同时适用于连续和脉冲ASL技术，由下面的公式概括：

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/721476_orig.png?383
   :alt: Buxton
   :align: center
   :width: 600 

ΔM(t)表示控制状态和标记状态时的组织磁化强度差异，M0b 是标记前血液的平衡磁化强度，α称为标记效率（流动自旋反转的百分比，通常为80-95%，与使用的ASL方法有关）。有一个因子2是因为自旋有反转，控制状态和标记状态下磁化强度的改变为M0b − (−M0b) = 2M0b。F表示血流量，为期望测量得到的参数。

这个积分表示是一个卷积，卷积是线性系统分析的基本数学方法。积分中的第一项a(τ)是一个动脉输入函数，Buxton称为组织传递函数，表示图像读出期间在时刻t到达一个体素的标记磁化的归一化浓度。 R(τ)称为残留函数，是一个无量纲的变量，与DSC中使用的类似，表示标记水分子在时刻t仍然留在成像体素中的百分比。没有在DSC中出现但是ASL分析所必须的一个新项是m(τ)，磁化驰豫函数，表示时刻t初始反转磁化剩余的百分比。

Buxton模型中有几个隐含的假设，其中任何一个都可能受到挑战:

1. 完美的“塞”流。假设标记的磁化作为一个完美的有锋利前后边缘的矩形团进入，因此动脉输入函数，a(t)，除了血团通过时都为0。a(t)的形式为a(t) =αe-t/T1b，其中T1b是血液的驰豫时间。实际上，如此完美的矩形自旋标记轮廓很难实现，即使采用像QUIPSS技术提高血团边缘的界定。传输时间范围比较大会导致血流量被低估。
2. 单室动力学模型。假设标记的水进入体素后瞬间与组织完成交换，满足“充分混合”条件。实际上，一些标记的自旋在交换之前仍会留在血管中，一些标记的自旋则会流出成像层面而不会发生交换。两种效应都会导致灌注的低估。真正的血组织分配系数(λ)需要测量或者估计，对人的大脑，在正常血流速度下大约为0.9。Buxton模型中残留函数形式一般采用R(t) = e-Ft/λ.
3. 磁化强度衰减率反映组织的T1。作为上述假设1和2的结果，磁化驰豫函数形式为m(t) = e-t/T1t，其中T1t是组织T1。由于此假设不考虑血液流过，磁化传递效应和不完全混合，这个假设会导致灌注被高估。

为了克服Buxton模型的限制，更复杂的分析已经开发出来，包括：1）使用圆而且光滑的前后边缘描述动脉输入函数；2）使用有血管和组织的双室模型类似与DCE成像中的Tofts模型；3）分割灰质和白质并分别使用不用的组织T1和λ值；4）改变磁化衰减函数来反映组织水与血管水交换之前的初始阶段。多TI ASL采集方法也有望能够更好估计血团到达时间及血液和组织的驰豫属性。

**参考材料**
    * Alsop DC, Detre JA, Gola X, et al. `Recommended implementation of arterial spin-labeled perfusion MRI for clinical applications: A consensus of the ISMRM perfusion study group and the European consortium for ASL in dementia <http://mriquestions.com/uploads/3/2/7/4/3274160/recommended_implementation_of_asl.pdf>`_. Magn Reson Med 2015; 73:102-116.
    * Buxton RB, Frank LR, Wong EC, et al. `A general kinetic model for quantitative perfusion imaging with arterial spin labeling <http://www.mri-q.com/uploads/3/2/7/4/3274160/buxton_general_kinetic_model.pdf>`_. Magn Reson Med 1998; 40:383-396.
    * Herscovitch P, Raichle ME. `What is the correct value for the brain-blood partition coefficient for water <http://www.mri-q.com/uploads/3/2/7/4/3274160/partition_coefficient_water_in_brain_jcbfm19859a.pdf>`_? J Cereb Blood Flow Metab 1985; 5:65-69. (Answer: probably about 0.90 ml/g) 
    * Mutsaerts HJMM, Steketee RME, Heijtel DFR, et al. `Inter-vendor reproducibility of pseudo-continuous arterial spin labeling at 3 Tesla <http://www.mri-q.com/uploads/3/2/7/4/3274160/intervendor_asljournal.pone.0104108.pdf>`_. PLOS One 2014; 9(8):e104108.     
    * Petersen ET, Lim T, Golay X. `Model-free arterial spin labeling quantification: approach for perfusion MRI <http://mriquestions.com/uploads/3/2/7/4/3274160/quasar_petersen06.pdf>`_. Magn Reson Med 2006; 55:219-232. (QUASAR method) 
    * Petersen ET, Zimine I, Ho Y-C L, Golay X. `Non-invasive measurement of perfusion: a critical review of arterial spin labelling techniques <http://mriquestions.com/uploads/3/2/7/4/3274160/bjr_67705974.pdf>`_. Br J Radiol 2006; 79:688-701. 
    * Wang Z. `Arterial spin labeling perfusion MRI signal processing toolbox (ASLtbx) <http://www.mri-q.com/uploads/3/2/7/4/3274160/asltbx_manual.pdf>`_. Version 1, May 2012. (manual for a freely available MATLAB-based toolbox for processing ASL data).
    * Williams DS, Detre JA, Leigh JS, Koretsky AP. `Magnetic resonance imaging of perfusion using spin inversion of arterial water <http://mriquestions.com/uploads/3/2/7/4/3274160/pnas-1992-williams-212-6.pdf>`_. Proc Natl Acad Sci USA 1992; 89:212-216. (derives modified Bloch equations to account for inflow of inverted spins)
    * Wong EC. `Quantifying CBF with pulsed ASL: technical and pulse sequence factors <http://www.mri-q.com/uploads/3/2/7/4/3274160/wong-2005-journal_of_magnetic_resonance_imaging.pdf>`_. J Magn Reson Imaging 2005; 22:727-731.

**相关问题**
	* `如何使用动脉输入函数从DSC数据中提取更多量化的血流信息？ <http://chunshan.github.io/MRI-QA/dsc/quantitative-dsc.html>`_
	* `如何选择成像参数来优化ASL的采集？ <http://chunshan.github.io/MRI-QA/asl/asl-parameters.html>`_