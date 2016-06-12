Question-BOLD脉冲序列：用于BOLD fMRI的最佳脉冲序列是什么？
==========================================================================

:date: 2016-03-06
:tags: BOLD
:slug: bold-pulse-sequences
:authors: Chunshan
:summary: BOLD脉冲序列

.. |br| raw:: html

   <br />

原文链接:\ `What is the best pulse sequence to use for BOLD fMRI? <http://mriquestions.com/bold-pulse-sequences.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/3783571_orig.png?323
    :alt: summary
    :align: center
    :width: 700

神经元活动产生的血流动力学反应会改变大脑局部氧合血红蛋白和去氧血红蛋白的浓度。这个过程反过来会产生T2和T2*弛豫时间随时间的变化，这是产生BOLD信号的基础。因此，BOLD脉冲序列需要有如下的特征：1）对T2和/或T2*变化敏感；2）BOLD信号本身比较微弱，通常与基线相比只有百分之几的差异，具有检测此微弱信号的能力；3）具有足够的空间分辨率和时间分辨率，能够在多个紧密间隔的时间点上覆盖全脑。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9575165_orig.jpg?359
   :alt: fMRI axial images
   :align: right
   :width: 400

   一个短暂的刺激之后BOLD的血流动力学响应函数（HRF）

场强小于等于3.0T时，T2*加权的梯度回波（GRE）序列是最常用的BOLD序列。场强大于等于7.0T时，一般首选T2加权的自旋回波（SE）。下面讨论的参数主要适用于3.0T成像，大多数选择更多是经验性的，基于信噪比，空间分辨率，时间分辨率和运动伪影之间的权衡（其他适用于7.0T成像的方法和适用于所有场强的新技术可以参考高级讨论）。

**成像平面**  通常选择斜轴，平行于前连合-后连合（AC-PC）连线，能够覆盖全脑。如果用于评估一些解剖结构，如海马，可能会使用垂直于此结构或垂直于AC-PC连线的斜冠状成像。

**回波时间（TE）**  使用GRE序列，当TE ≈ 组织T2*时，BOLD效应最大，然而，更长的TE会导致更多GRE-EPI图像上的磁敏感伪影和信号丢失，可能需要在后处理中进行场映射校正。3.0T时，一个合理的折中值是TE ≈ 30−35 ms。

**重复时间（TR）**  应当与血流动力学响应函数峰值信号的时间差不多，典型值为1-4秒。较短的TR（≤ 1.5秒）会更适合于统计，但是必须要改变其他参数如翻转角避免饱和效应和血流流入的信号。

**层厚**  这是低信噪比（太薄）和部分容积效应（太厚）之间的折中，典型值为2-3mm。

**层的采集顺序**  一般使用交替采集（1,3,5...2,4,6...）以降低层与层之间的串扰伪影。

**平面分辨率**  更高的平面空间分辨率意味着更大的成像矩阵，需要增加成像时间（因此影响其时间分辨率），也需要延长读出时间（产生更多伪影），而且降低信噪比。也存在权衡，典型选择是基础分辨率矩阵为64x64 − 128x128（平面内分辨率为2x2 − 3x3 mm）。

**总成像时间**  为了被试有最大的服从性，总的成像时间不应该超过45-60分钟，每个单独的实验不超过10-12分钟。

**并行成像**  一般建议使用并行成像减少采集时间和磁敏感伪影，但仅建议使用小加速因子（R ≈ 2）从而不影响信噪比太多。

**高级讨论**

*高级技术和选择*

**畸变校正** 一直以来都采用预采集的场映射以最小化磁敏感引起的fMRI在空间上的扭曲，但这会显著增加采集的时间。使用一个快速的匀场过程提高磁场均匀性被更广泛地使用，尤其是在不以研究为主的中心。
 
**3D方法**  fMRI的3D采集具有减少低质图像，连续采集没有间隙，不需要进行切片-时间校正的潜在优势。但TR和读出时间会延长，实现这样的采集变得困难，许多应用无法接受。分段的3D方法，辅以两个方向的并行成像，能够缓解这些问题。也可以使用一种称为z-匀场的技术，这种技术会沿层编码方向（z轴）施加一个补偿梯度，确保k空间轨迹在TE时刻回到原点。

**多路采集** 现在可以使用“多带”技术同时激发几层，即使这样的代价是会延长EPI读出链。

**PRESTO (Principle of Echo Shifting with a Train of Observations)**  PRESTO技术采用一种巧妙的特定选层梯度模式（有相同的相重聚区域）使第一个RF脉冲产生的信号出现延迟，直到第二个RF脉冲施加时才出现。这种方法是一个单独Q&A的主题，已经被Philips开发为商用产品用于ASL和fMRI。

**其他非GRE脉冲序列**  使用自旋回波的技术也曾经用于fMRI的研究，因为它们能提供高信噪比，减少几何畸变。然而，FSE/TSE序列产生T2加权的图像，必须做出一些变化（如引入回波平移延迟或回波校验修正）增强对T2*的敏感性，这是fMRI在3T或更低场强时所需要的。混合的GRASE方法（交替使用梯度和自旋回波）可能会是一个解决方案，但是目前还没有广泛使用。磁场强度7T或以上时，T2*加权的需求变得不那么强烈，因为fMRI中单纯的T2变化可以更好地反映神经元活动位置。因此在超高场，可以使用自旋回波和SSFP方法，并且有一定优势。

**参考材料**
     * Chen JE, Glover GH. `Functional magnetic imaging methods <http://mriquestions.com/uploads/3/4/5/7/34572113/chen_glover_fmri_review_2015art3a10.10072fs11065-015-9294-9.pdf>`_. Neuropsychol Rev 2015; 25:289-313.
     * Feinberg DA, Setsompop K. `Ultra-fast MRI of the human brain with simultaneous multi-slice imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/feinberg_1-s2.0-s1090780713000311-main.pdf>`_. J Magn Reson 2013; 229:90-100. ("Multi-band" technique applied to fMRI)
     * Glover GH. `3D z-shim method for reduction of susceptibility effects in BOLD fMRI <http://mriquestions.com/uploads/3/4/5/7/34572113/3dzshim.pdf>`_. Magn Reson Med 1999; 42:290-299.
     * Preibisch C, Wallenhorst T, Heidemann R, et al. `Comparison of parallel acquisition techniques Generalized Autocalibrating Partially Parallel Acquisitions (GRAPPA) and Modified Sensitivity Encoding (mSENSE) in functional MRI (fMRI) at 3T <http://mriquestions.com/uploads/3/4/5/7/34572113/preibisch_et_al-2008-journal_of_magnetic_resonance_imaging.pdf>`_. J Magn Reson Imaging 2008; 27:590-598.
     * van Gelderen P, Duyn JH, Ramsey NF, Liu G, Moonen CTW. `The PRESTO technique for fMRI <http://mriquestions.com/uploads/3/4/5/7/34572113/1-s2.0-s1053811912000341-main.pdf>`_. NeuroImage 2012; 62:676-681.
     * Weiskopf N, Hutton C, Josephs O, Deichmann R. `Optimal EPI parameters for reduction of susceptibility-induced BOLD senstiivty losses: a whole-brain analysis at 3 T and 1.5 T <http://mriquestions.com/uploads/3/4/5/7/34572113/weiskopf_suscpt_losses_1-s2.0-s1053811906007841-main.pdf>`_. NeuroImage 2006; 33:493-504.

**相关问题**
  * `BOLD fMRI的图像对比度是如何产生的？ <http://chunshan.github.io/MRI-QA/bold/bold-contrast.html>`_