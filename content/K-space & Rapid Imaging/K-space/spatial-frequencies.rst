Question-空间频率：空间频率是什么意思？
========================================================================================

:date: 2014-10-04
:tags: K-space & Rapid Imaging, K-space (Basic)
:slug: spatial-frequencies
:authors: Chunshan
:summary: 空间频率是什么意思

原文链接:\ `What do you mean by spatial frequency? <http://mriquestions.com/spatial-frequencies.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9413903_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4991572_orig.jpg?139
   :alt: Line-pair resolution test pattern
   :align: right
   :width: 250

   测试分辨率的线对图案.你的显示器有多好？

空间频率的概念对所有类型的成像都是很基础的，包括摄影，电视，普通放射成像，和磁共振成像。你可能见过右图所示的测试图案，用于评估打印机或者电脑监视器的保真度。

图像分辨率通常用“每mm中线的对数”描述，能够分辨的黑条和白条的最近间距。由于一对线就像相邻波的波峰和波谷，每mm中线的对数可以用来测量空间频率。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/8499974_orig.jpg
   :alt: spatial frequencies
   :align: left
   :width: 400

正如一个一维信号可以分解为简单的正弦和余弦波的和，二维图像可以分解为一组相位，频率，幅度和方向不同的平面波。

平面波必须从所有可能的方向考虑，沿图像x轴(0º)，沿图像y轴(90º)和其他的方向（145º, −126º等）。

+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9670405_orig.gif?326 | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/3538852_orig.png?327  |
|    :alt: Egg-crate" pattern                                                       |    :alt: planar waves from more directions                                         |
|    :width: 400                                                                    |    :width: 400                                                                     |
|                                                                                   |                                                                                    |
|    由两个偏移90º的平面波形成的“蛋箱”图案                                          |    更多方向的平面波相加时，图像逐渐显现                                            |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9140299_orig.jpg
   :alt: All images can be represented as a sum of spatial frequencies oriented in different directions.
   :align: right
   :width: 400

   所有图像都可以表示为不同方向空间频率的和。

所有图像都可以使用傅里叶分析分解为不同频率，相位，振幅和方向的平面波。这在斑马图像上很容易看到，但是对即使没有清晰边界的图像其实也适用。实际上，人的视觉皮层包含对不同方向上正弦空间频率响应的细胞。MR图像的k空间表示仅仅是反应图像空间谐波内容的空间频率的有机集合。

|
|
|

**参考材料**
     * `Sharpness: What is it and how is it measured? <http://mriquestions.com/uploads/3/4/5/7/34572113/imatest_-_sharpness__what_is_it_and_how_is_it_measured_.pdf>`_ (White paper from `Imatest.com <http://www.imatest.com/>`_, a company that makes image-testing software).
     * `"Spatial frequency" <https://en.wikipedia.org/wiki/Spatial_frequency>`_. Wikipedia, The Free Encyclopedia.

**相关问题**
	* `k空间是什么？ <http://chunshan.github.io/MRI-QA/k-space/what-is-k-space.html>`_
	* `k空间中点与图像中的点并不对应，它们的意义是什么？ <http://chunshan.github.io/MRI-QA/k-space/parts-of-k-space.html>`_
	* `What are 2D- and 3D-Fourier transforms? I don't see how FT works in higher dimensions. <http://mriquestions.com/what-are-2d---3d-fts.html>`_	 		    