Question-钆的T1效应：钆的T1效应出现情况下，对比增强区域有何表现？
===================================================================

:date: 2015-10-18
:tags: Perfusion, DSC
:slug: t1-effects-on-dsc
:authors: Chunshan
:summary: 钆外渗会造成T1效应

原文链接:\ `What about areas of contrast enhancement? Surely some T1 effects of gadolinium are present there... <http://www.mri-q.com/t1-effects-on-dsc.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4612212_orig.png
    :alt: summary
    :align: center
    :width: 700

由于血脑屏障（BBB，Blood Brain Barrier）的阻隔，含钆造影剂正常情况下不能进入大脑和脊髓的血管外空间。血脑屏障的内皮细胞之间紧密连接，只让离子和小分子（如O2）穿过血管壁。如果血脑屏障由于疾病（如恶性肿瘤和感染）被破坏，造影剂漏入脑实质，使T1缩短，T1信号增强。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8677845_orig.jpg
   :alt: Blood-brain Barrier
   :align: right
   :width: 500

   血脑屏障紧密连接的内皮细胞阻止血管内的钆造影剂进入大脑的细胞外空间（此图来自维基百科）

有渗漏的血脑屏障会使造影剂在组织中累积，这违反了简单示踪剂动力学模型的基本假设，也就是违反了DSC成像的基础，没有池或造影剂滞留。血脑屏障破坏时，血流量/血容量的估计会出现明显的错误。

钆造影剂累积造成T1缩短使DSC灌注成像出现两种效应：
1，迟钝的T2*信号损失。DSC方法依赖于钆造影剂团通过时T2*失相位导致的信号下降。血管外钆造影剂的T1效应使得信号升高，延迟了希望的T2*缩短，造成一些情况下反常的灌注后信号过冲。    2，稳态信号效应。DSC图像采集通常使用相对较短的TR（一般为1000-2000ms），由于钆累积导致T1缩短的区域在射频脉冲之间恢复更快，因此有更强的稳态信号。翻转角（α）大时，这种现象更加明显。

有几种措施补偿钆外渗造成的T1效应。一种常用方法是使用钆“预负荷”，在常规注射和DSC序列采集前约5-10分钟注射造影剂总剂量的 ¼ 到 ⅓。钆预负荷会升高对比度增强区域的基准信号，在DSC团注期间获得更好的T2*改变。
第二种减少钆外渗造成的T1效应的方法是减小DSC采集序列的射频脉冲翻转角，然而翻转角减小也会导致信噪比下降。其他补偿组织中钆累积效应的方法是基于软件的泄露校正算法。

**参考材料**
     * `"Blood-brain Barrier" <https://en.wikipedia.org/wiki/Blood-brain_barrier>`_, Wikipedia, The Free Encyclopedia.     
     * Boxerman JL, Prah DE, Paulson ES, et al. `Gadolinium-based cerebral blood volume estimation determined by comparison with MION as a criterion standard <http://www.mri-q.com/uploads/3/2/7/4/3274160/preload_asnr.pdf>`_. AJNR Am J Neuroradiol 2012; 33:1081-87.
     * Boxerman JL, Schmainda KM, Weisskoff RM. `Relative cerebral blood volume maps corrected for contrast agent extravasation significantly correlate with glioma tumor grade, whereas uncorrected maps do not <http://www.mri-q.com/uploads/3/2/7/4/3274160/boxerman_ajnr_uncorrected_maps.pdf>`_. AJNR Am J Neuroradiol 2006; 27:859-67.
     * Welker K, Boxerman J, Kalnin A, et al. `ASFNR recommendations for clinical performance of MR dynamic susceptibility contrast perfusion imaging of the brain <http://www.mri-q.com/uploads/3/2/7/4/3274160/white_paper_asfnr_on_dsc_ajnr.a4341.full.pdf>`_. AJNR Am J Neuroradiol 2015; 36: E41-E51.

**相关问题**
	* `Question-DSC：如何做一个DSC灌注研究？ <http://chunshan.github.io/MRI-QA/dsc/how-to-perform-dsc.html>`_