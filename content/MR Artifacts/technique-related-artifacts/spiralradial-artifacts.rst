Question-径向/螺旋伪影：径向或螺旋成像中的卷折伪影如何？看起来卷折伪影应该总是存在，因为在每个方向上都要相位编码。
================================================================================================================================

:date: 2015-12-25
:tags: MR Artifacts, technique related artifacts
:slug: spiralradial-artifacts
:authors: Chunshan
:summary: 径向或螺旋成像中的卷折伪影

原文链接:\ `What about wrap-around artifacts on radial or spiral imaging? it seems like they should always be present because phase-encode goes in every direction. <http://mri-q.com/spiralradial-artifacts.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6154853_orig.png
    :alt: summary
    :align: center
    :width: 700

径向/螺旋扫描方法确实也会产生卷折和其他形式的混叠伪影，但是它们的表现形式与直线（笛卡尔）扫描中看到的有些不同。

大多数径向和螺旋成像方法中，频率和相位轴不保持基本解剖方向中的固定关系（从左到右，从上到下等）。相反，相位和频率编码方向随着轨迹扫过或围绕k空间中心旋转时不断改变。当出现混叠时，通常以广泛分布于图像中的曲线带形式出现，虽然有时也会出现离散的径向排列的“鬼影”。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/15707_orig.gif          | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/111706_orig.gif?284      |
|    :alt: PROPELLER acquisition                                                |    :alt: Aliasing                                                              |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
|    PROPELLER采集说明频率和相位编码方向如何变化取决于每一个刀片的方向          |    源自圆形FOV外红点（左下）的混叠被复制成图像上的一个弧                       |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: hhttp://mri-q.com/uploads/3/4/5/7/34572113/6050618_orig.jpg?317   | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/2693098_orig.jpg?351     |
|    :alt: PROPELLER acquisition with less blades                               |    :alt: PROPELLER acquisition with more blades                                |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
|    如果刀片数相对较少，FOV也比较小，可见一些离散的后脑部的混叠图像            |    如果使用许多刀片，混叠伪影分散地更广泛                                      |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/9179600_orig.gif
   :alt: The "gridding" problem
   :align: right
   :width: 400

   螺旋/径向/PROPELLER成像中的“网格化”问题。采集的数据点与矩形阵列（用于离散傅里叶变换）并不匹配，因此须转换/插值，这会在最终的图像中引入振铃伪影和混叠伪影。

在PROPELLER图像的背景中通常可见一种不同形式的伪影，包含弥散的晕开的细线或条纹。这是由网格化导致的重建伪影，此过程中径向/螺旋模式采集的数据点必须转变/插值以适合等间隔的矩形阵列，然后用于图像处理。如果使用线性插值，整个图像中会有简单的阴影，但如果使用更高阶的插值机制，更复杂的振荡会混叠到图像中，偶尔会形成高信号物体边缘的明亮条纹，类似于CT中骨或金属周围看到的现象。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/4872870_orig.jpg?308    | .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/3311765_orig.jpg?323     |
|    :alt: Diffuse radial reconstruction artifact                               |    :alt: Fine streaks                                                          |
|    :width: 400                                                                |    :width: 400                                                                 |
|                                                                               |                                                                                |
|    弥散的径向重建伪影                                                         |    PROPELLER图像中右侧脸颊上高信号区域的细条纹                                 |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

**参考材料**
     * Pipe JG. `Motion correction with PROPELLER MRI: application to head motion and free-breathing cardiac imaging <http://mri-q.com/uploads/3/4/5/7/34572113/pipej_mrm_1999_42_953_959_propeller.pdf>`_. Magn Reson Med 1999; 42:963-969.
     * Patch SK. `k-Space data preprocessing for artifact reduction in MR imaging <http://mri-q.com/uploads/3/4/5/7/34572113/propeller_artifact_reduction.pdf>`_. Multidimensional Image Processing, Analysis, and Display: RSNA Categorical Course in Diagnostic Radiology
Physics 2005; pp 73–87.
     * Rasche V, Proska R, Sinkus R, et al. `Resampling of data between arbitrary grids using convolution interpolation <http://mri-q.com/uploads/3/4/5/7/34572113/rasche_et_al__3_.pdf>`_. IEEE Trans Med Imaging 1999;18:385–392.

**相关问题**
	* `螺旋桨技术如何减少运动伪影？ <http://chunshan.github.io/MRI-QA/motion-related-artifacts/propellerblade.html>`_