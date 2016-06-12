Question-开关模式：为什么要做“开关”BOLD信号的比较？为什么不能直接测量BOLD信号绝对值？
=======================================================================================================================

:date: 2016-03-08
:tags: BOLD
:slug: why-on-off-comparison
:authors: Chunshan
:summary: BOLD信号开关模式

.. |br| raw:: html

   <br />

原文链接:\ `Why do you have to do an "on-off" comparison? Why not just measure the absolute BOLD signal instead? <http://mriquestions.com/why-on-off-comparison.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6489585_orig.png
    :alt: summary
    :align: center
    :width: 700

原始MR BOLD信号不是绝对的，受很多具体的技术和患者因素的影响。技术因素包含场强，放大器增益，头线圈接收单元的数目和位置，脉冲序列（SE或GRE），层的采集顺序，序列时间参数（TR/TE/α），体素大小等。患者相关的因素包括红细胞容积比，呼吸速率，头的大小，年龄，性别，激素状态和药物治疗（含咖啡因）。

BOLD信号通常用任意单位（A.U.s，Arbitrary Units）或者与基线相比变化的百分比表示。虽然一些研究实验室对BOLD信号校准取得一些有限的成果（见高级讨论），绝大多数情况下BOLD信号不能简单地转换为绝对单位，如每分钟的血流量或每秒去极化的峰值数量。

因此大多数BOLD/fMRI检查中，必须基于“任务”态和“非任务”态信号的变化使用统计技术区分“激活”脑区和“非激活”脑区的信号。

**高级讨论**

虽然有这些限制，BOLD信号的校准方面仍取得一些有限的成果。现有的方法包括使用呼吸挑战引起血液中碳酸浓度升高（↑CO2）和氧气浓度升高（↑O2），同时结合动脉自旋标记（ASL）技术观察BOLD信号的变化。脑血容量可以使用外源性对比剂（如钆）或内源性对比方法如血管空间占用（VASO，Vascular Space Occupancy）进行测量。结合复杂的数学模型，就可以估计氧摄取分数（OEF，Oxygen Extraction Fraction）。

**参考材料**
     * Blockley NP, Griffeth VEM, Simon AB, Buxton RB. `A review of calibrated blood oxygenation level-dependent (BOLD) methods for the measurement of task-induced changes in brain oxygen metabolism <http://mriquestions.com/uploads/3/4/5/7/34572113/blockley_et_al-2013-nmr_in_biomedicine.pdf>`_. NMR Biomed 2013; 26:987-1003.
     * Hoge RD. `Calibrated fMRI <http://mriquestions.com/uploads/3/4/5/7/34572113/1-s2.0-s1053811912001991-main.pdf>`_. Neuroimage 2012; 62:930-937. (review)
     * Lu H, Golay X, Pekar JJ, van Zijl PCM. `Functional magnetic resonance imaging based on changes in vascular space occupancy <http://mriquestions.com/uploads/3/4/5/7/34572113/lu_et_al-2003_vaso-magnetic_resonance_in_medicine.pdf>`_. Magn. Reson. Med. 2003; 50: 263–274.

**相关问题**
  * `如何设计一个BOLD/fMRI检查？ <http://chunshan.github.io/MRI-QA/bold/fmri-paradigm-design.html>`_