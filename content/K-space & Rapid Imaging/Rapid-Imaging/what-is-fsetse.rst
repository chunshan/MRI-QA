Question-快速自旋回波：什么是快速自旋回波成像？
======================================================================================================================

:date: 2014-10-25
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: what-is-fsetse
:authors: Chunshan
:summary: 什么是快速自旋回波成像

原文链接:\ `What is Fast (Turbo) Spin Echo imaging? <http://mriquestions.com/what-is-fsetse.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/954024_orig.png
    :alt: summary
    :align: center
    :width: 700

快速自旋回波（Fast Spin Echo， FSE）成像也称为TSE（Turbo Spin Echo），是RARE（Rapid Acquisition with Refocused Echoes）技术的商业化实现，最早是Hennig等在1986年提出的。从那时起，FSE/TSE就成为现代磁共振成像中的一个“主力”脉冲序列。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9078766_orig.gif?550
   :alt: conventional spin-echo V.S. Fast spin echo
   :align: center
   :width: 700

FSE/TSE脉冲序列（如上所示）表面上类似于传统自旋回波（conventional spin-echo，CSE）序列，在一个90°脉冲后使用一系列180°聚焦脉冲产生一连串回波。可简单记为：
* CSE: 90º−180º−echo………………………………………………………90º−180º−echo
* FSE: 90º−180º−echo−180º−echo−180º−echo−180º−echo……………90º−180º−echo

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/7162303_orig.gif?476
   :alt: conventional spin-echo
   :align: right
   :width: 500

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5013564_orig.gif?474
   :alt: Fast spin echo
   :align: right
   :width: 500

然而，FSE/TSE技术会对每一个回波改变相位编码梯度（传统的多回波序列使用相同的相位编码采集所有的回波）。回波之间改变相位编码梯度的结果是给定的重复时间（TR）内可以采集k空间中的多条线（如相位编码步骤）。

由于每个TR间隔内可以采集多条相位编码线，FSE/TSE技术可以显著减少成像时间。

给定TR间隔内采集的回波数目称为回波链长度（Echo Train Length，ETL）或者涡轮因子。ETL在常规扫描中的典型范围是4到32，但是在快速成像/平面回波技术中，可能会超过200。

如果层数不是限制因素，成像时间反比于ETL，即使用相同的TR，ETL=8的FSE/TSE序列所需时间仅是传统SE序列的八分之一。

除了速度之外，FSE技术还有其它的优势。首先，k空间扫描多条线节省的大量时间可用于延长TR，使得纵向磁化的恢复时间更长，从而提高信噪比。其次，可以使用更多的相位编码步骤，提高空间分辨率。最后，磁敏感导致的信号损失减少，使得FSE在对颅底和金属周围物体成像时优于CSE。

然而，FSE能够降低磁敏感伪影也可能是其缺点，使得FSE图像不太可能检测小面积的钙化或出血。FSE的其他局限性包括T2加权像上脂肪信号过于明亮，质子密度加权像上CSF信号过于明亮。多个180°脉冲会导致组织发热增加，也会限制FSE在婴儿及小孩儿中的使用。

**高级讨论**

*关于FSE/TSE序列的附加说明*

虽然上面的脉冲图与后面的讨论都集中在笛卡尔/直线轨迹上，其实FSE/TSE可以用于几乎所有的k空间采样策略，包括螺旋（Spiral），径向（Radial），圆形（Circular）和螺旋桨（PROPELLER）方法。

FSE/TSE可用于2D或3D模式中。2D采集中，多个层面几乎都采用隔行扫描的方式，因为TR一般比序列长度要长。FSE/TSE技术节省的时间首次使得3D采集称为可能。

在上面的FSE/TSE脉冲序列图中，你可能已经注意到每一个正相位编码梯度总是与回波后一个立刻施加的负相位编码梯度成对出现，这会将每个步骤的相位回退，使得k空间中的每一行都从相同的方向开始遍历。

回聚脉冲不需要是准确的180°，为了减少组织中的能量沉积（特定吸收率-Specific Absorption Rate/SAR），会产生一些有趣的现象称为“强回波（hyperechoes）”，在后面的一个Q&A中会讲到。

不管使用何种翻转角度的回聚脉冲，FSE/TSE序列的信号包含来自最近的一对RF脉冲的主要的自旋回波信号，也包含来自前面多个RF脉冲组合作用的受激回波。回波链中特定相位编码值的分布决定了图像的对比度，影响图像的伪影。通常最好是以阶梯模式缓慢改变回波之间的相位，从而减少由于k空间不连续导致的伪影。不同的厂商做法并不相同，可以看一下下面参考文献中Hitachi的“Prime FSE”策略。


**参考材料** 
     * Hennig J, Nauerth A, Friedburg H. `RARE imaging - a fast imaging method for clinical MR <http://mriquestions.com/uploads/3/4/5/7/34572113/hennig-rare.pdf>`_. Magn Reson Med 1986; 3: 823-833. 
     * Hitata Y, Sasaki M, Esashika K, Gakumazawa H. `Hitachi's Prime Fast Spin Echo technology: efficacies in improving image quality and usability <http://mriquestions.com/uploads/3/4/5/7/34572113/fse_hitachi_prime.pdf>`_. (Sales brochure for Hitachi's version of FSE, giving some insight into how various manufacturers have different approaches to echo ordering and data collection in what is essentially the same basic sequence).
     * Walker MT, Partovi S, Karis JP, Fram EK. `Fast, versatile, and cost-effective FSE MR imaging: technical considerations and clinical applications <http://www.thebarrow.org/Education_And_Resources/Barrow_Quarterly/205117>`_. Barrow Quarterly 2000;16:1-5.


**相关问题**
	* `你如何选择快速自选回波的成像参数？有几个新参数需要设置。 <http://chunshan.github.io/MRI-QA/rapid-imaging/fse-parameters.html>`_