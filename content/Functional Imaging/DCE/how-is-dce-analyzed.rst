Question-DCE成像：如何评估从DCE检查中获得的信息？
======================================================================================

:date: 2015-10-26
:tags: Perfusion, DCE
:slug: how-is-dce-analyzed
:authors: Chunshan
:summary: 如何评估从DCE检查中获得的信息

原文链接:\ `How do you evaluate the information obtained from a DCE imaging study? <http://www.mri-q.com/how-is-dce-analyzed.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/225402_orig.png?310
    :alt: summary
    :align: center
    :width: 700

DCE成像数据可以使用三种方法评估：简单的视觉评估，半定量的描述性指标分析或基于模型的定量分析。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3947751_orig.gif?476
   :alt: Contributions to total contrast enhancement as a function of time
   :align: right
   :width: 500

   随时间变化不同生理现象对总对比增强的贡献

对不同时间点的对比增强图像的简单视觉评估是临床放射医生最常用的方法，首先寻找动态序列中造影剂首先出现的区域，病变区域对造影剂摄取的模式和流入/流出率，可以对病变性质提供线索。

动态对比增强曲线的不同部分反映了不同的解剖和生理特征。该曲线初始陡峭的上坡与组织血流量相关，曲线的峰值高度反映的总血流量和血容量。曲线的下一部分由于造影剂渗透到组织间隙，反映的是毛细血管面积和渗透功能。曲线的最后部分反映组织总的细胞外空间和血浆间质容积。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3872153_orig.png?407
   :alt: Semi-quantitative descriptive indices
   :align: left
   :width: 400

与DSC类似，也可以从原始DCE图像的强度数据中计算半定量描述性指标，包括到达时间（AT， Arrival Time），达峰时间（TTP， Time to Peak），流入率（WIR， Wash-in Rate），流出率（WOR，Wash-out Rate）曲线下面积（AUC，Area Under Curve），与基线相比的最大增强（ME， Maximum Enhancement）和最大增强百分比（%ME）。尽管这些指标的绝对值没有意义，但是与其他病变的信号强度改变比较，或与正常的背景组织比较还是有用的。

DCE数据的全定量分析需要三步：1，将信号强度转换为钆造影剂浓度；2，选择一个合适的组织模型；3，从拟合的数据中估计模型参数。能够获取的重要的量化量化组织参数包括血管渗透性，造影剂交换比率，血流量和组织的细胞外空间体积。如何计算这些参数的细节和他们的生理意义是后续几个Q&A的主题。

**参考材料**
    * Choi YJ, Kim JK, Kim N, et al. `Functional MR imaging of prostate cancer <http://www.mri-q.com/uploads/3/2/7/4/3274160/prostate_functional_radiographics_review_g2e271065078.pdf>`_. RadioGraphics 2007; 27:65-77. (use of semi-quantitive DCE parameters to detect prostate cancer.)   
    * Kuhl CK, Mielcareck P, Klaschik S, et al. `Dynamic breast MR imaging: Are signal intensity time course data useful for differential diagnosis of enhancing lesions <http://www.mri-q.com/uploads/3/2/7/4/3274160/kuhl_types_i_ii_iii_breast_ce_radiology2e2112e12er99ap38101.pdf>`_? Radiology 1999; 211:101-110. (original paper describing Type I, II, and III kinetic patterns of contrast uptake in breast tumors).
    * Schnall MD, Blume J, Bluemke DA, et al. `Diagnostic architectural and dynamic features at breast MR imaging: multicenter study <http://www.mri-q.com/uploads/3/2/7/4/3274160/mammo_radiol2e2381042117.pdf>`_. Radiology 2006; 238:42-53. (showed Kuhl classification not so accurate as thought).
    * Verma S, Turkbey B, Muradyan N, et al. `Overview of dynamic contrast-enhanced MRI in prostate cancer diagnosis and management <http://www.mri-q.com/uploads/3/2/7/4/3274160/prostate_ajr2e122e8510.pdf>`_. AJR Am J Roentgenol 2012; 198:1277-1288.

**相关问题**
	* `Question-DCE脉冲序列：使用什么脉冲序列进行DCE检查？ <http://chunshan.github.io/MRI-QA/dce/how-is-dce-performed.html>`_  
	* `Can myocardial perfusion be accurately quantified? <http://www.mri-q.com/quantifying-perfusion.html>`_  
	* `How do calculated DCE parameters relate to patterns of enhancement we see on clinical images? <http://chunshan.github.io/MRI-QA/dsc/dsc-v-dce-v-asl.html>`_  