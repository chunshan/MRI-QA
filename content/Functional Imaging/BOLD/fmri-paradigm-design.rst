Question-fMRI模式设计：如何设计一个BOLD/fMRI检查？
==========================================================================

:date: 2016-03-07
:tags: BOLD
:slug: fmri-paradigm-design
:authors: Chunshan
:summary: fMRI模式设计

.. |br| raw:: html

   <br />

原文链接:\ `How do you design a BOLD/fMRI study? <http://mriquestions.com/fmri-paradigm-design.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4971479_orig.png?319
    :alt: summary
    :align: center
    :width: 700

BOLD/fMRI检查的实验设计可以分成三种基本类型：1）组块，2）事件相关，3）混合式。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1081253_orig.png
   :alt: Three designs of BOLD/fMRI experiments
   :align: right
   :width: 400

   三种BOLD/fMRI实验的设计

**组块设计**

组块设计是最古老的功能成像模式，在fMRI发明之前就广泛用于PET检查。组块模式中任务时间（也被称为epochs）与休息时间交替进行。任务状态较高的BOLD信号“减去”休息状态时较低的BOLD信号就可以揭示大脑皮质激活的焦点区域。

组块设计是最简单最直接的fMRI实验实现模式。这种模式广泛用于临床fMRI检查中，这些检查的目的是在手术前识别功能区。在经典的“手指敲击”实验中（左图所示，在一个单独的Q&A中详细描述），患者敲击手指15秒钟，然后休息同样长度的时间。对噪声和空间畸变校正后，净BOLD信号超出一定统计阈值的区域就称为“激活”。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1727460_orig.gif?250
   :alt: Finger tapping fMRI study
   :align: left
   :width: 400

   使用简单组块设计的手指敲击fRMI检查，\ |br|\ 比较信号在活动和休息期间的差异。因为激活\ |br|\ 的“开关”模式像一列通过的火车，\ |br|\ 因此组块设计也常称为“厢式车（boxcar）”设计

与其他的fMRI模式相比，组块设计具有最高的信噪比，最高的统计功率和最大的时间效率。除了上面描述的简单“开关（on-off）”式组块设计，也有更复杂的组块设计，比如，在每个休息阶段之后两种或更多种活动交替进行。

尽管有这些优点，组块设计在更复杂的神经生理学中实用性有限，特别是涉及非二进制的任务。使用简单的任务，被试可以预测简单组块（任务/休息）的顺序或持续时间，从而引入干扰变量。最后，由于组块设计需要在相对长的时间（10-20秒）中测量，血流动力学响应和fMRI信号出现时机的信息很难衡量。

**事件相关设计**

事件相关设计会在短而可变的时间间隔中进行一个或多个任务/刺激。这种模式提供了复杂的神经生理学实验所需的高度灵活性。事件可以是随机的，也可以混合使用不同类型的事件。被试不能预测何时将发生什么，可能会有惊喜/惊讶。事件相关设计有更好的时间分辨率，可以更好地估计血流动力学响应函数（HRF）的时间过程，使得在实验中评估“学习曲线”和实践效果，包括评估刺激时间间隔的影响成为可能。

事件相关设计的缺点有较低的信噪比，较低的统计效能，对每个被试需更长的成像时间和更多的试验。数据分析更加复杂，也更依赖于对HRF的准确建模。同时，事后分析可以在检查后对事件重新排序和重新分类，比如，可以将正确和不正确的响应分开独立进行分析。

**混合设计**

混合模式兼具组块设计和事件相关设计的特征，这种模式中，休息块与组块设计中的休息块相同，但任务块时事件是半随机的。混合模式倾向于保留组块设计中良好的信噪比特征，兼有事件相关设计中的灵活性。

**参考材料**
     * Amaro E Jr, Barker GJ. `Study design in fMRI: basic principles <http://mriquestions.com/uploads/3/4/5/7/34572113/amaro_study_design_542057.pdf>`_. Brain Cognition 2006; 60:220-232.
     * Blamire AM, Ogawa S, Ugurbil K, et al. `Dynamic mapping of the human visual cortex by high-speed magnetic resonance imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/pnas-1992-blamire-11069-73.pdf>`_. Proc Natl Acad Sci USA 1992; 89:11069–11073. (first demonstration of difference between long-duration/block and short-duration/event-related brain responses)
     * Buckner RL. `Event-related fMRI and the hemodynamic response <http://mriquestions.com/uploads/3/4/5/7/34572113/bruckner_1998_10.1.1.481.2946.pdf>`_. Human Brain Mapping. 1998; 6:373–377. (shows linear response to multiple short-term stimuli)
     * Dale AM. `Optimal experimental design for event-related fMRI <http://mriquestions.com/uploads/3/4/5/7/34572113/dale-event.pdf>`_. Human Brain Mapping 1999; 8:109-114.
     * Huettel SA. `Event-related fMRI in cognition <http://mriquestions.com/uploads/3/4/5/7/34572113/event_v_blocked_huttell_nihms333191.pdf>`_. NeuroImage 2012; 62:1152–1156. (good review)
     * Liu TT, Frank LR, Wong EC, Buxton RB. `Detection power, estimation efficiency, and predicability in event-related fMRI <http://mriquestions.com/uploads/3/4/5/7/34572113/liu-event.pdf>`_. NeuroImage 2001; 13:759-773.
     * Maus B, Van Breukelen GJP, Goebel R, Berger MPF. `Optimization of blocked designs in fMRI studies <http://mriquestions.com/uploads/3/4/5/7/34572113/maus_blocked_design_art_3a10.1007_2fs11336-010-9159-3.pdf>`_. Psychometrika 2010; 75:373-390.
     * Price CJ, Veltman DJ, Ashburner J, Josephs O, Friston KJ. `The critical relationship between the timing of stimulus presentation and data acquisition in blocked designs with fMRI <http://mriquestions.com/uploads/3/4/5/7/34572113/pricewk7price99.pdf>`_. NeuroImage 1999; 10:36-44.

**相关问题**
  * `使用fMRI识别运动皮层的最佳方法是什么？ <http://chunshan.github.io/MRI-QA/bold/motor-paradigms.html>`_
  * `为什么要做“开关”BOLD信号的比较？为什么不能直接测量BOLD信号绝对值？ <http://chunshan.github.io/MRI-QA/bold/why-on-off-comparison.html>`_