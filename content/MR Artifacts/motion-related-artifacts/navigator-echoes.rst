Question-导航回波：什么是导航回波？导航回波如何减少运动伪影？
======================================================================================================

:date: 2015-12-07
:tags: MR Artifacts, motion related artifacts
:slug: navigator-echoes
:authors: Chunshan
:summary: 什么是导航回波？导航回波如何减少运动伪影？

原文链接:\ `What are navigator echoes and how do they reduce motion artifacts? <http://mri-q.com/navigator-echoes.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/7808149_orig.png
    :alt: summary
    :align: center
    :width: 700

导航器是动态跟踪解剖运动的额外的射频脉冲，特别是跟踪膈肌上下运动的位置。导航脉冲可以是自旋回波（SE），也可以是梯度回波（GRE）。

导航器最简单的形式是在scout图像上在肝脏的圆顶部用图形标出。导航器可以在单一平面上标示（左图），也可以使用两个感兴趣带（右图）形成更准确的“铅笔束”或柱形束。导航带通常1-2cm宽，沿束方向的空间分辨率则是1mm左右。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/7361766_orig.jpg        | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6850125_orig.jpg         |
|    :alt: Navigator prescribed from single coronal scout image.                |    :alt: Navigator prescribed by two intersecting bands on axial scout image.  |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
|    冠状位scout图像上标示的单一导航                                            |    在横断位图像上两个感兴趣带标示的导航                                        |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/1788300_orig.jpg
   :alt: M-mode display of navigator data showing motion of liver (lower gray bands) with respiration. Dark area is lung. 
   :align: left
   :width: 400

   肝（下部灰色带）随呼吸运动的导航数据的M型显示。暗色区域是肺

导航器返回的回波信号在读出（运动）方向重建，显示为沿束方向的线状数据。这种技术是线扫描成像的一种形式，也被成为M型显示，因为相当于M型超声心动图中观察心脏瓣膜运动的方式。

软件自动检测膈肌运动的波峰和波谷。磁共振技师可以进一步定义哪些位置采集的数据允许排除在外，通常还可以设置一定的容忍度，一般3-6mm。

根据导航回波得到的信息可以在呼吸周期的特定阶段触发数据采集，也可以用于根据呼吸导致的器官位移调整一组片层的位置。使用呼吸管时的触发和相位重排算法也同样可以用于导航扫描中。

虽然导航器主要用于追踪膈肌运动，但是也可以放置在任何移动的物体上，比如心脏。导航回波经常被集成到多次激发的弥散加权脉冲序列中，用于图像采集时运动的自我校正。导航回波通常在功能磁共振检查中用来监测和校正头部的轻微运动。整个头颅可以使用球形导航器在三维空间中进行追踪。

**高级讨论**

关于导航器的补充：

一个并行成像线圈可以用于监测导航器，或者也可以使用整个体线圈。

导航器可以在数据采集之前，之后或者都使用。跟踪导航器可以用于确定膈肌在数据采集前后是否已经恢复到相同的位置。如果前导导航器和跟踪导航器的位置差异超过了预设的阈值，相应的数据就会被废弃并重新采集。

切片跟踪技术会在扫描体移动到患者几乎相同的解剖位置时进行每次采集。如果成像堆栈的跟踪位置根据感兴趣解剖器官的实际位置而动态调整，就需要使用前导导航器，门控和跟踪可以同时进行。

导航门控的水平位置在采集过程中可能会漂移。在多数扫描器中可以在扫描中使用自动检测机制连续检测并更新呼气水平来校正这种漂移。

一些扫描仪中还可以使用多个导航束。

二维导航方法（如Siemens的2D PACE和Philips的MotionTrak）有一些比线扫描方法更具优势的地方。二维方法使用螺旋轨迹填充k空间，因此激发是圆柱形。这样的饱和伪影不太广泛，特别是小翻转角度时。

2D螺旋射频导航器可以通过改变翻转角和周期数进行修改。更少的周期导致更短的脉冲持续时间和更少的偏共振问题，但是会导致射线束附近出现更严重的混叠环状伪影。二维射频脉冲的形状通常是块状或jinc状，后者的激发轮廓更好。

**参考材料**
     * Ehman RL, Felmlee JP. `Adaptive technique for high-definition MR imaging of moving structures <http://mri-q.com/uploads/3/4/5/7/34572113/ehman_felmlee_navigators_radiology_1989.pdf>`_. Radiology 1989; 173:255-263.
     * Welch EB, Manduc A, Grimm RC et al. `Spherical navigator echoes for full 3D rigid body motion measurements in MRI <http://mri-q.com/uploads/3/4/5/7/34572113/3d_navigators.pdf>`_. Magn Reson Med 2002; 47:32-41.

**相关问题**
	* `How can navigators track heart position if placed on the diaphragm? <http://mri-q.com/heart-navigators.html>`_