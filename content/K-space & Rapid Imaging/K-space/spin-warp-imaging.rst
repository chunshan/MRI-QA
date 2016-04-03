Question-自旋-卷折成像：什么是自旋-卷折成像？它是不是“常规”MRI？
===========================================================================================

:date: 2014-10-08
:tags: K-space & Rapid Imaging, K-space (Basic)
:slug: spin-warp-imaging
:authors: Chunshan
:summary: 自旋-卷折成像

原文链接:\ `What is spin-warp imaging? Isn't this just "regular" MRI? <http://mriquestions.com/spin-warp-imaging.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4266023_orig.png?297
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/2466002_orig.gif?492
   :alt: conventional 2D spin-echo pulse sequence
   :align: left
   :width: 600

傅里叶变换自从二十世纪八十年代初被引入，Edelstein和其同事发明的这一基于自旋-卷折的成像技术已经成为对MR信号空间编码的主导方法。如果你认为“常规磁共振成像”是连续应用相位和频率编码梯度进行数据采集，你正在思考的就是自旋-卷折方法的一些变种。

使用自旋-卷折成像的传统2D自旋回波脉冲序列的原型如上所示。这儿，施加90°-180°射频脉冲对之后产生MR信号，选层梯度与每一个射频脉冲同时打开使得只有一个层面被激发。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4353376_orig.gif?498
   :alt: The digitized values of the MR signal
   :align: right
   :width: 500

   每一个时间点MR信号数字化的值插入k空间矩阵中水平的一行，从左到右填充

频率编码会使用90°和180°脉冲之间的失相叶和180°脉冲之后的读出叶。失相叶会对扫描轴上的质子造成相位偏移，此相位偏移是因为梯度场中空间位置不同的质子其共振频率不同导致的。这些自旋的相位会被180°脉冲反转，然后通过读出叶相位回聚为一个回波。

自旋-卷折序列独特的特征是在信号生成过程中会施加一个幅度变化的相位编码梯度，通常在90°和180°脉冲之间。此片层中其它的MR信号会在下一个TR间隔内收集，使用相同的频率编码梯度，但是不同的相位编码梯度。相位编码梯度提供了一种沿此方向根据空间位置区分信号的方法。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/2435348_orig.gif?380
   :alt: Phase enconding steps
   :align: left
   :width: 500

相位编码梯度连续应用，产生的数字化MR信号会用于填充k空间的不同行。对于常规磁共振成像，这个过程通常会按顺序重复256次。一旦所有的行都填充了数据，就可以使用傅里叶变换重建图像。

关于k空间，既然你已经看到了这儿，我建议你花一刻钟时间看一下下面的两个视频，由已故的Paul Callaghan提供。Callaghan博士仔细勾画了2DFT自旋卷折成像的原理，展示了k空间和MR信号是如何关联的(*视频来自youtube，可能不能显示*)。

.. raw:: html

    <div><div class="wsite-multicol"><div class="wsite-multicol-table-wrap" style="margin:0 -15px;">
	<table class="wsite-multicol-table">
		<tbody class="wsite-multicol-tbody">
			<tr class="wsite-multicol-tr">
				<td class="wsite-multicol-col" style="width:60%; padding:0 15px;">
					<div class="wsite-youtube" style="margin-bottom:10px;margin-top:10px;"><div class="wsite-youtube-wrapper wsite-youtube-size-auto wsite-youtube-align-center">
					<div class="wsite-youtube-container">

					<iframe src="//www.youtube.com/embed/XJvVnlMv1LQ?wmode=opaque" frameborder="0" allowfullscreen></iframe>
					</div>
					</div></div>
				</td>				

				<td class="wsite-multicol-col" style="width:60%; padding:0 15px;">
					<div class="wsite-youtube" style="margin-bottom:10px;margin-top:10px;"><div class="wsite-youtube-wrapper wsite-youtube-size-auto wsite-youtube-align-center">
					<div class="wsite-youtube-container">

					<iframe src="//www.youtube.com/embed/SrG_w5v3R8A?wmode=opaque" frameborder="0" allowfullscreen></iframe>
					</div>
					</div></div>	
				</td>			
			</tr>
		</tbody>
	</table>
	</div></div></div>

**参考材料**
     * Edelstein WA, Hutchison JMS, Johnson G, Redpath T.  `Spin warp NMR imaging and applications to human whole-body imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/edelstein_spin_warp.pdf>`_. Phys Med Biol 1980; 25:751-6.
     * Wald L. `MR image encoding <http://mriquestions.com/uploads/3/4/5/7/34572113/imageencoding_mit_courseware_wald.pdf>`_. (From MIT OpenCourseWare `http://ocw.mit.edu <http://ocw.mit.edu/>`_) 

**相关问题**
	* `从哪儿获得数据填充k空间？ <http://chunshan.github.io/MRI-QA/k-space/data-for-k-space.html>`_