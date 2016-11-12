Question-强回波：什么是“强回波”？与普通回波有什么不同？
======================================================================================================================

:date: 2014-11-01
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: hyperechoes
:summary: 强回波

原文链接:\ `What are "hyper-echoes" and how do they differ from regular echoes? <http://mriquestions.com/hyperechoes.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4771630_orig.png
    :alt: summary
    :align: center
    :width: 700

强回波是高幅值的受激回波，当射频脉冲以特定的一种对称次序排列时就会产生。这个概念是由弗莱堡大学医院的Juergen Hennig提出的，在一些Siemens机器中作为快速自旋回波的一种选择。

快速自旋回波序列中RF脉冲特定的排列如下图所示。脉冲链的中心是180°脉冲，两侧的脉冲呈镜像排列，极性和相位相反。180°脉冲后的反对称脉冲完全撤销了180°脉冲前的脉冲造成的复杂的旋转，使得强回波在期望的回波时间处出现。强回波有与常规自旋回波几乎相同的幅值，没有任何干扰脉冲。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/8768047_orig.gif?568
   :alt: reduced flip angle FSE imaging
   :align: center
   :width: 800

令人惊讶的是，只要对称关系保持，不管单个脉冲的翻转角和相位偏移，强回波都会出现。强回波在快速自旋回波链中可以重复出现几次，通常会使强回波的出现与最低阶的相位编码步骤相匹配，使信噪比最大。虽然目前强回波主要与快速自旋回波序列结合使用，但也有用于弥散加权成像，梯度回波成像和磁共振波谱的潜力。

**参考材料** 
    * Frank LR, Wong EC, Liu TT, Buxton RB. `Increased diffusion sensitivity with hyperechos <http://mriquestions.com/uploads/3/4/5/7/34572113/diffusion-hyperechoes_frank03_hyper.pdf>`_. Magn Reson Med 2003; 49:1098-1105.
    * Hennig J, Weigel M, Scheffler K. `Multiecho sequences with variable refocusing flip angles: optimization of signal behavior using smooth transitions between pseudo steady states (TRAPS) <http://mriquestions.com/uploads/3/4/5/7/34572113/traps_abstract.pdf>`_. Magn Reson Med 2003;49:527–535. 
    * Hennig J, Scheffler K. `Hyperechoes <http://mriquestions.com/uploads/3/4/5/7/34572113/hyperechoes_hennig_2001.pdf>`_. Magn Reson Med 2001;46:6–12.
    * Mugler JP III. `Optimized three-dimensional fast spin echo MRI <http://mri-q.com/uploads/3/4/5/7/34572113/optimized_3dfse_jmri24542.pdf>`_. J Magn Reson Imaging 2014;39:745-767. (Excellent up-to-date review).
    * Weigel M., Hennig J. `Contrast behavior and relaxation effects of conventional and hyperecho-turbo spin echo sequences at 1.5 and 3T <http://mriquestions.com/uploads/3/4/5/7/34572113/hyperechoes_weigel.pdf>`_. Magn Reson Med 2006;55:826-35.

**相关问题**
	* `为什么想要在FSE中减小翻转角？小翻转角难道不会使MR信号消失么？ <http://chunshan.github.io/MRI-QA/rapid-imaging/reduced-flip-angle-fse.html>`_