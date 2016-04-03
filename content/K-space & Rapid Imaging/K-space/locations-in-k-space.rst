Question-空间频率的位置：k空间中空间频率具体在什么位置？
========================================================================================

:date: 2014-10-05
:tags: K-space & Rapid Imaging, K-space (Basic)
:slug: locations-in-k-space
:authors: Chunshan
:summary: k空间中空间频率的位置

原文链接:\ `Exactly where are the spatial frequencies are located in k-space? <http://mriquestions.com/locations-in-k-space.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/8885696_orig.png?304
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/670889_orig.gif?438
   :alt: locations-in-k-space
   :align: left
   :width: 600

概括地说，k空间的中心包含低空间频率信息，决定图像整体的对比度，亮度和基本形状；k空间的周边包含高空间频率信息（边缘，细节，尖锐的过渡）。

k空间的数据单元通常在以kx和ky为主轴的矩形网格中显示，k空间中的kx和ky轴与图像中的水平轴(x-)和垂直轴(y-)对应，但是kx和ky轴表示x-和y-方向的空间频率而不是位置，k空间中每个数据点(kx,ky)也并不与图像中每个像素点(x,y)一一对应。k空间中每个点含有最终图像中所有像素的空间频率和相位信息，反过来，图像中的每个像素也映射到k空间中所有的点。

kx轴上的点表示沿图像x方向的频率部分，ky轴上点反应图像沿y方向的频率部分。一个方块的图像，方块的边与图像的x轴和y轴对齐，此图像的k空间图像如右上图所示。

如果方块旋转45°，对应于方块边缘的主要空间频率也将与kx轴和ky轴成45°。平面图像波的角度和k空间位置之间的关系如下所示。

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/696427_orig.gif  | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1493423_orig.gif  |
|    :alt: Image of a block                                                     |    :alt: Correseponding k-space representation                                 |
|    :width: 300                                                                |    :width: 300                                                                 |
|                                                                               |                                                                                |
|    一个方块的图像                                                             |    对应的k空间表示                                                             |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1401047958.jpg   | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9765219_orig.gif  |
|    :alt: Image of rotated block                                               |    :alt: Corresponding rotation of k-space frequencies                         |
|    :width: 300                                                                |    :width: 300                                                                 |
|                                                                               |                                                                                |
|    旋转方块的图像                                                             |    k空间频率相应旋转                                                           |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1834219_orig.gif
   :alt: locations-in-k-space
   :align: center
   :width: 800

当然，真实的图像在所有方向上都有频率分量，造成k空间具有“银河”状的外观。k空间中特定位置的一颗明亮的“星”暗示此点表示的空间频率对最终图像有积极的贡献。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/8582198_orig.gif?585
   :alt: locations-in-k-space
   :align: center
   :width: 800

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/2216332_orig.gif?295
   :alt: Inverse relation between size of object (left) and extent of k-space representation (right)
   :align: right
   :width: 400

   物体尺寸（左）与k空间表示频率范围（右）之间的反比关系

最后一点，成像物体的物理尺寸和k空间中频率的宽广程度成反比。换句话说，小物体（像右图中的小白圆圈）有涟漪到k空间的边缘，而较大的物体的频谱能量更多聚焦于k空间的中心。

随着物体的增大，仅需要各个方向少量的低空间频率来表示。极限情况下（物体填充整个FOV），仅需要一个常数傅里叶项。对非常大的物体，其k空间表示收缩为(kx, ky) = (0, 0)处的一个数据点，它的值反应图像的平均亮度。

|
|
|
|
|
|
|
|
|
|
|
|

**参考材料**
     * Mezrich R. `A perspective on k-space <http://mriquestions.com/uploads/3/4/5/7/34572113/fourier.kspace.mezrich.1995.pdf>`_. Radiology 1995; 195: 297-315. [review].
     * Miller K. `MRI image formation (ppt) <http://mriquestions.com/uploads/3/4/5/7/34572113/miler-image_formation.ppt>`_. On-line lecture notes available at `users.fmrib.ox.ac.uk/~karla/teaching/image_formation.ppt <http://users.fmrib.ox.ac.uk/~karla/teaching/image_formation.ppt>`_
     * `"Spatial frequency" <https://en.wikipedia.org/wiki/Spatial_frequency>`_. Wikipedia, The Free Encyclopedia.

**相关问题**
	* `k空间是什么？ <http://chunshan.github.io/MRI-QA/k-space/what-is-k-space.html>`_
	* `k空间中点与图像中的点并不对应，它们的意义是什么？ <http://chunshan.github.io/MRI-QA/k-space/parts-of-k-space.html>`_
	* `What are 2D- and 3D-Fourier transforms? I don't see how FT works in higher dimensions. <http://mriquestions.com/what-are-2d---3d-fts.html>`_	 		    