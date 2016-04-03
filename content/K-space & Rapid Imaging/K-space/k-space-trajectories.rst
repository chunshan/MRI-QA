Question-填充k空间的方法：你提到的用不同轨迹填充K空间。它们是什么？
========================================================================================

:date: 2014-10-10
:tags: K-space & Rapid Imaging, K-space (Basic)
:slug: k-space-trajectories
:authors: Chunshan
:summary: 从哪儿获得数据填充k空间？

原文链接:\ `You alluded to different trajectories for filling k-space. What are they? <http://mriquestions.com/k-space-trajectories.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/8006302_orig.png?282
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6999003_orig.jpg
   :alt: k-space for pigeons
   :align: left
   :width: 200

   鸽子的k空间

在产生MR信号之前，k空间是等待数据到来的一系列空格子。打个比方，想象k空间为有很多空“鸽子洞”的箱子，等待接收鸽子，目标是一个洞中放一个鸽子。只要箱子被填满，顺序并不重要。

下边是现代MR成像中4种常见的k空间填充轨迹。传统上，笛卡尔方法（一行接一行）占主导地位，但是现在所有这些模式都被广泛使用。

+-------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9551885_orig.gif |
|    :alt: k-space for pigeons                                                  |
|    :width: 800                                                                |
|                                                                               |
+-------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4421712_orig.gif |
|    :alt: k-space for pigeons                                                  |
|    :width: 800                                                                |
|                                                                               |
+-------------------------------------------------------------------------------+

.. raw:: html

    <div class="wsite-flash">
    	<div style="padding-top: 20px; padding-bottom: 20px; text-align: center;">
				<object type="application/x-shockwave-flash" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" align="middle"	height="256px" width="512px" >
					<param name="movie" value="http://mriquestions.com/uploads/3/4/5/7/34572113/kspace-centric.swf"> 
					<param name="quality" value="high"> 
					<param name="play" value="true"> 
					<param name="loop" value="true"> 
					<param name="wmode" value="transparent"> 
					<param name="allowFullScreen" value="true"> 
					<param name="flashvars" value=""> 
					<embed src="http://mriquestions.com/uploads/3/4/5/7/34572113/kspace-centric.swf" quality="high" pluginspage="//www.macromedia.com/go/getflashplayer" play="true" loop="true" wmode="transparent" allowfullscreen="true" flashvars="" type="application/x-shockwave-flash" align="middle"  height="256px" width="512px"></embed>
				</object>
		</div>
	</div>

上图：k空间的笛卡尔填充方法，频率编码从左到右

下图：k空间的螺旋填充方法，从中心向外围

.. raw:: html

    <div class="wsite-flash"><div style="padding-top: 20px; padding-bottom: 20px; text-align: center;">
				<object type="application/x-shockwave-flash" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" align="middle" height="256px" width="512px" >
					<param name="movie" value="http://mriquestions.com/uploads/3/4/5/7/34572113/kspace-outward.swf"> 
					<param name="quality" value="high"> 
					<param name="play" value="true"> 
					<param name="loop" value="true"> 
					<param name="wmode" value="transparent"> 
					<param name="allowFullScreen" value="true"> 
					<param name="flashvars" value=""> 
					<embed src="http://mriquestions.com/uploads/3/4/5/7/34572113/kspace-outward.swf" quality="high" pluginspage="//www.macromedia.com/go/getflashplayer" play="true" loop="true" wmode="transparent" allowfullscreen="true" flashvars="" type="application/x-shockwave-flash" align="middle"  height="256px" width="512px"></embed>
				</object>
			</div></div>

**高级讨论**

选择何种k空间填充策略取决于不同的应用，这种选择也许对平面回波成像（EPI）最为关键，EPI中很长的读出链使得序列对磁敏感伪影和快速切换产生的多余涡电流效应非常敏感。理解这些效应的一般分析方法是沿三个标准的成像轴（相位编码，频率编码，层面选择）进行分解。

沿频率编码方向的梯度导致图像错切和模糊，这种效应与读出链长度成正比。沿相位编码方向的梯度会缩放图像并改变有效TE。由于沿相位编码轴的带宽通常远低于其他方向的带宽，偏离共振的自旋（如脂肪质子）将明显错位。因此EPI序列通常使用脂肪饱和技术减少相位编码方向的化学位移伪影。最后，沿层面选择轴上的梯度会使得信号相散，产生信号缺如。

遍历k空间的笛卡尔方法最容易实现，很长时间都是大多数MR成像序列(含EPI或其他序列)的标准方法。现在，径向和螺旋读出方法逐渐成为常态，因为它们对运动天生不太敏感，而且允许更短的TE值。螺旋方法可以是“螺旋进”，“螺旋出”或二者联合。由于在径向和螺旋技术中频率和相位编码方向没有分开，伪影有些不同（包括环形带和环形模糊）。螺旋扫描受不正确的梯度时间和伴随产生的梯度场影响更大。图像重建也更加复杂，需要”网格化“或其他方法将测量的k空间数据点移至矩形矩阵中，然后应用快速傅里叶变换的数值处理。

**参考材料**
     * Mezrich R. `A perspective on k-space <http://mriquestions.com/uploads/3/4/5/7/34572113/fourier.kspace.mezrich.1995.pdf>`_. Radiology 1995; 195: 297-315. [review].
     * Miller K. `MRI image formation (ppt) <http://mriquestions.com/uploads/3/4/5/7/34572113/miler-image_formation.ppt>`_. On-line lecture notes available at `users.fmrib.ox.ac.uk/~karla/teaching/image_formation.ppt <http://users.fmrib.ox.ac.uk/~karla/teaching/image_formation.ppt>`_

**相关问题**
	* `从哪儿获得数据填充k空间？ <http://chunshan.github.io/MRI-QA/k-space/data-for-k-space.html>`_