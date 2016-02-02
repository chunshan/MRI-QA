Question-第二类化学位移伪影：什么是第二类化学位移伪影（Chemical Shift:2nd Kind）？
============================================================================================

:date: 2015-11-23
:tags: MR Artifacts, tissue related artifacts
:slug: chemical-shift-2nd-kind
:authors: Chunshan
:summary: 什么是第二类化学位移伪影？

原文链接:\ `What is a chemical shift artifact of the second kind? <http://www.mri-q.com/chemical-shift-2nd-kind.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/3582283_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/7639677_orig.jpg?277
   :alt: chemical shift artifact of the second kind
   :align: right
   :width: 400

第二类化学位移伪影有时又被称为印度墨水或黑线伪影，因为器官和肌肉束看起来像被黑笔描了边。这些黑线并不反应真正的解剖结构，而是含有水和脂肪的边界像素的信号被破坏性干扰的结果。由于这个原因，它有时被称为相位取消伪影。图示了脊柱，大腿和腹部的例子。

+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/8546841_orig.gif?273 | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/3975551_orig.jpg?332  |
|    :alt: Chemical shift artifact of the second kind                            |    :alt: Chemical shift artifact at border of muscle and fat                    |
|    :width: 350                                                                 |    :width: 350                                                                  |
|                                                                                |                                                                                 |
+--------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

这种形式的化学位移伪影只发生在梯度回波成像中（不像第一类化学位移伪影也会发生在自旋回波成像中）。此外，第二类化学位移伪影是由于相位取消效应导致的，所以不限于频率编码方向（第一类化学位移伪影仅限于此频率编码方向），会出现在沿脂肪-水交界处的所有像素。

在自旋回波成像中，水和脂肪间的信号会在每个回波的中心回到相位相干（尽管它们频率不同，空间位置不同）。梯度回波成像中，水和脂肪质子在每个回波的中心却不会回到相位相干（因为梯度回波序列缺少自旋回波序列中的180°相位重聚脉冲）。梯度回波序列中，水和脂肪质子之间的相位差是回波时间（TE）的函数。1.5T下，水和脂肪质子间从相位相同变为不相同又变为相同的周期约1/225Hz（4.4ms），因此1.5T下，在TE=2.2，6.6，11.0，15.4ms等值时，梯度回波成像中脂肪和水相位正好彼此相反。在TE接近这些“特殊值”时采集的梯度回波图像就会出现第二类的化学位移伪影。

+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/8242005_orig.gif     |
|    :alt: phase cancellation artifact                                           |
|    :width: 450                                                                 |
|                                                                                |
+--------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/206041_orig.gif      |
|    :alt: phase cancellation artifact                                           |
|    :width: 450                                                                 |
|                                                                                |
+--------------------------------------------------------------------------------+

上图显示了相位取消效应和“黑线”产生的起源。中间的边界像素包含相同数目的水和脂肪质子，而且在TE=2.2ms相位相反时成像，因为水和脂肪信号相位相反，它们彼此取消，净幅值为零，因此没有信号。纯水或纯脂肪时没有这样的相位取消，由于显示的图像都是幅值重建，因此最终的图像中都是亮的。因此纯水和纯脂肪的像素被它们之间交界处的黑色边界分开。

**参考材料**
     * Wehrli FW, Perkins TG, Shimakawa A, Roberts F. `Chemical shift-induced amplitude modulations in images obtained with gradient refocusing <http://www.mri-q.com/uploads/3/4/5/7/34572113/wehrli_chemic_shift.pdf>`_.  Magn Reson Imaging 1987; 5:157-8.

**相关问题**
	* `什么是化学位移伪影？ <http://chunshan.github.io/MRI-QA/tissue-related-artifacts/chemical-shift-artifact.html>`_