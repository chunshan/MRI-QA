Question-DSC：如何做一个DSC灌注研究？
=============================================================

:date: 2015-10-16
:tags: Perfusion, DSC
:slug: how-to-perform-dsc
:authors: Chunshan
:summary: 如何做一个DSC灌注研究

.. |Ktrans| replace:: K\ :sup:`trans`

原文链接:\ `How do you perform a DSC perfusion study? <http://www.mri-q.com/how-to-perform-dsc.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8428067_orig.png
    :alt: summary
    :align: center
    :width: 700

动态磁敏感对比（DSC）灌注成像在1.5T或更高场强的设备上效果更好。将18或20号静脉导管插入右肘窝，使用高压注射器注射钆螯合物。虽然所有钆基对比剂都可以使用，但是我们更喜欢标准剂量（0.1mmol/kg）的钆贝酸盐（莫迪司，MultiHance®），它安全性好，T2弛豫率高。

对脑灌注成像，在动态研究之前，我们使用大约¼到⅓的总剂量作为预负荷。预负荷可以减少对比剂渗漏引起的T1效应，特别是采用大翻转角度序列时（并不是所有中心都使用预负荷，但我们认为它是有帮助的，尤其是肿瘤中对比剂渗漏到组织可能比较明显）。5分钟过后，剩余的钆注射速率不少于3-5mL/s，然后是20mL生理盐水“驱逐舰”。

注射对比剂后需要马上以类似放电影的形式获取大脑（或其他感兴趣器官）的快速T2*或T2加权像，目前大多数中心采用单次激发的平面回波成像（EPI）技术，用约20片层覆盖全脑，时间分辨率为1至1.5s。1.5T设备下，我们使用T2*加权的GRE EPI序列，参数TR/TE/α = 2000/50/35°或者T2加权的SE EPI序列， 参数TR/TE/α = 1500/30/90°。

当钆螯合物团首次通过局部循环区域时，大部分或全部仍留在血管内空间，血管壁造成钆螯合物在血管内外浓度不同，从而导致血管周围局部磁场不均匀（磁敏感效应），T2（T2*）失相位，信号强度降低。值得注意的是，这种效应与在CT灌注成像中看到的现象相反，CT灌注成像中碘造影剂穿过时组织吸收率升高。

MR信号强度可以基于像素逐个绘制出来，如下面的图像所示。定性和半定量灌注参数都可以从时间强度曲线中获得，包括到达时间（AT），达峰时间（TTP），和曲线下面积（AUC），也被称为负性增强积分（NEI）。这些参数和其他参数在后续Q&A中有更详细的描述。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/2930394_orig.jpg?463
   :alt: TIC of DSC
   :width: 700

   钆造影剂通过时脑内的时间信号强度曲线图

**高级讨论**

为了不浪费预负荷和全剂量造影剂注射之间约5分钟左右的等待时间，通常在此期间我们会扫常规的T2加权成像序列或者采集T1加权像用于这个阶段的DCE研究。


**参考材料**
     * Essig M, Shiroishi MS, Nguyen TB, et al. `Perfusion MRI: the five most frequently asked technical questions <http://www.mri-q.com/uploads/3/2/7/4/3274160/essig_5_questions_ajr2e122e9543.pdf>`_. AJR Am J Roentgenol 2013; 200:24-34.
     * Jahng G-H, Li K-L, Ostergaard l, Calamante F. `Perfusion magnetic resonance imaging: a comprehensive update on principles and techniques <http://www.mri-q.com/uploads/3/2/7/4/3274160/perfusion_review_article_kjr-15-554.pdf>`_. Korean J Radiol 2014; 15:554-577.
     * McGehee BE, Pollock JM, Maldjian JA. `Brain perfusion imaging: how does it work and what should I use <http://www.mri-q.com/uploads/3/2/7/4/3274160/mcgehee_whitlow_review.pdf>`_? J Magn Reson Imaging 2012; 36:1257-1272.
     * Welker K, Boxerman J, Kalnin A, et al. `ASFNR recommendations for clinical performance of MR dynamic susceptibility contrast perfusion imaging of the brain <http://www.mri-q.com/uploads/3/2/7/4/3274160/white_paper_asfnr_on_dsc_ajnr.a4341.full.pdf>`_. AJNR Am J Neuroradiol 2015; 36: E41-E51.

**相关问题**
	* `If gadolinium contrast is used to increase signal intensity on routine MR images, why does it decrease signal on DSC perfusion images?  <http://www.mri-q.com/bolus-gd-effect.html>`_
	* `Question-MR灌注概述：MRI中的DSC，DCE和ASL灌注方法有何不同?  <http://chunshan.github.io/MRI-QA/dsc/dsc-v-dce-v-asl.html>`_