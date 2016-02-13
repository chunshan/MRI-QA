Question-门控/触发简介：怎么做心跳和呼吸门控？
================================================================================

:date: 2015-12-05
:tags: MR Artifacts, motion related artifacts
:slug: gating-methods
:authors: Chunshan
:summary: 怎么做心跳和呼吸门控？

原文链接:\ `How are cardiac and respiratory gating performed? <http://mri-q.com/gating-methods.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6102624_orig.png
    :alt: summary
    :align: center
    :width: 700

减少心跳和呼吸伪影最古老最直接的方式是将磁共振数据采集与心跳或呼吸周期同步。这个过程称为门控或触发。这两个术语通常交替使用。

然而，最严格意义上讲，触发是一种前瞻性门控，只有当检测到所需的生理事件（如一个R波，脉搏，或呼吸的特定阶段）后才开始磁共振数据的的采集。门控则是一个比触发更宽泛的术语，既可以是前瞻性的，也可以是回顾性的。在回顾性门控中，磁共振数据被连续采集（不需要特定的心跳或呼吸“触发”事件），心电图，脉搏或呼吸水平也与磁共振数据同时记录。之后对磁共振数据进行重新排序，分组或与心肺周期的不同阶段相关联。回顾性门控通常用于心脏电影运动的研究方法。

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/_7126104_orig.gif
   :alt: Prospective cardiac gating 
   :align: center
   :width: 1000

   前瞻性心脏门控（触发）在两个R波之间特定的采集窗口内采集数据。回顾性门控持续地采集数据，然后根据心跳周期的不同阶段分组并且填充k空间。

**心跳门控**

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/7319891_orig.jpg
   :alt: Peripheral pulse transducer 
   :align: right
   :width: 250

   外周脉搏传感器（光电）（来自www.biopac.com）

心脏收缩可以通过心电图或脉搏传感器检测。对于心脏成像（通常也包括下胸部成像），必须要基于一些心电图类型的触发。由于从心脏收缩到脉搏波到达手指时间比较长而且延迟不可预测，脉搏门控不能用于心脏成像。脉搏门控通常用于外周磁共振血管造影或者用于脑脊液流动电影的研究。

心跳和脉搏门控特别可靠，除了室性心律失常的情况，被广泛使用。这些方法需要专门的硬件和软件，通常在每次扫描前还需要额外几分钟时间设置这些硬件和软件。另外的限制是重复时间（TR）不能自由选择，必须是心跳间隔的倍数。

**呼吸门控**

下胸和上腹部的影像学检查需要一些方法能够冻结膈肌的运动。对配合的患者，可以使用简单的屏气配合快速成像技术如HASTE或SS-EPI。对不配合的患者或者超过20-30秒的检查（患者的平均屏气极限），必须使用某种类型的呼吸门控技术。

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/8819780_orig.jpg?310
   :alt: Pneumatic respiratory belt and transducer 
   :align: left
   :width: 310

   气动呼吸带和传感器（来自www.biopac.com）

可以通过使用胸带，波纹管或坐垫等检测呼吸扩张。对胸式呼吸，胸带应环绕下胸部放置，对腹式呼吸，胸带应环绕中腹部放置。也有测量呼吸过程中绕胸电阻抗变化的装置，但是不常用。

简单的呼吸门控需要仅在呼吸周期的有限部分采集图像，有显著的时间损失（高达非门控检查的3倍时间）。因此很少使用纯粹的前瞻性呼吸门控，但是仍然使用回顾性补偿方法，根据呼吸时相对图像数据进行收集或重排。近年来使用导航回波跟踪膈肌运动已经成为进行呼吸触发最流行的方法。

下面的图片说明了简单的前瞻性心跳和呼吸门控在提高胸部和上腹部磁共振图像质量中的作用，单独使用和联合使用心跳和呼吸门控。


+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/5721998_orig.jpg        | .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/7654221_orig.jpg      |
|    :alt: Ungated                                                              |    :alt: Cardiac gating only                                                   |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
|    没有门控                                                                   |    只有心跳门控                                                                |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/7403086_orig.jpg     | .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6431947_orig.jpg      |
|    :alt: Respiratory gating only                                              |    :alt: Both cardiac and respiratory gating                                   |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
|    只有呼吸门控                                                               |    既有心跳门控又有呼吸门控                                                    |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

**参考材料**
     * Chia JM, Fischer SE, Wickline SA, Lorenz CH. `Performance of QRS detection for cardiac MRI with a novel vectorcardiographic triggering method <http://mri-q.com/uploads/3/4/5/7/34572113/chia_jmri_vector_cardiogram.pdf>`_. J Magn Reson Imaging 2000; 12:678-688.
     * Ehman RL, McNamara MT, Pallack M, et al. `Magnetic resonance imaging with respiratory gating: techniques and advantages <http://mri-q.com/uploads/3/4/5/7/34572113/ehman_respiratory_gating_1984_ajr.pdf>`_. AJR Am J Roentgenol 1984; 143:1175-1182.     
     * Lanzer P, Barta C, Botvinick EH, et al. `ECG-synchronized cardiac MR imaging: method and evaluation <http://mri-q.com/uploads/3/4/5/7/34572113/lanzer_radiology_1984_cardiac_gating.pdf>`_. Radiology 1985;155:681–686.
     * Santelli C, Nezafat R, Goddu B, et al. `Respiratory bellows revisited for motion compensation: preliminary experience for cardiovascular MR <http://mri-q.com/uploads/3/4/5/7/34572113/resp_bellows_revisited.pdf>`_. Magn Reson Med 2011; 65:1097-1102.

**相关问题**
	* `How do you set the various parameters for a cardiac gated study, such as repetition time (TR), trigger delay, and trigger window? <http://mri-q.com/gating-parameters.html>`_ 
	* `Is cardiac gating the same as triggering? <http://mri-q.com/gating-v-triggering.html>`_ 
	* `什么是呼吸补偿？与呼吸门控有何不同？ <http://chunshan.github.io/MRI-QA/motion-related-artifacts/respiratory-comp.html>`_  
