Question-矩形FOV：如何获得矩形FOV？我们为什么要使用这样的FOV？
========================================================================================

:date: 2014-10-18
:tags: K-space & Rapid Imaging, K-space (Advanced)
:slug: rectangular-fov
:authors: Chunshan
:summary: 矩形FOV

原文链接:\ `How does one obtain a rectangular field of view? Why would you want to use it? <http://mri-q.com/rectangular-fov.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/6819383_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/8388995_orig.gif?393
   :alt: Rectangular (1:2) FOV obtained by sampling every other line
   :align: right
   :width: 500

   在相位编码方向隔行采样得到的矩形FOV（1:2）

在\ `前一个Q&A <http://chunshan.github.io/MRI-QA/k-space/field-of-view-fov.html>`_\ 中，我们说明了FOV与k空间中采样之间的间隔（Δk）成反比。为了简化说明，我们考虑正方形的像素，而且在每一个方向上有相同的FOV。然而，通过改变频率和相位轴上的采样率，独立地更改每一个图像维度的FOV也是可能的。
FOVf = 1 / Δkf
FOVp = 1 / Δkp

对于二维自旋卷折成像，获取比例为1:2的矩形FOV需要交替采样k空间中的相位编码线，但是保留最大和最小相位编码梯度的幅值不变。这个过程使得相位编码步骤（Np）只有原来的一半，但是相邻两个步骤之间的增量翻倍。

因此在频率编码方向上的FOV（FOVf）和采样率不受影响，此外，由于FOVp和Np都减少一半，相位编码方向上的像素尺寸（FOVp/Np）和图像总体的空间分辨率也不变。

.. figure::http://www.mri-q.com/uploads/3/2/7/4/3274160/2989454_orig.jpg
   :alt: Rectangular FOV with wrap-around (aliasing) artifact from chin (red arrow)
   :align: right
   :width: 250

   矩形FOV中下巴（红色箭头）导致的卷折（混淆）伪影

所有的MR厂商都提供矩形FOV作为适用于大多数脉冲序列的标准选择，但是名称略有不同：“矩形FOV（Rectangular FOV）”（Philips, Hitachi, Toshiba），“相位FOV（Phase FOV）”（Siemens），“部分FOV（Partial FOV）”（GE）。

选择矩形FOV在扫描脊柱和四肢时特别有用，因为这些场景中一个解剖方向上的尺寸比其他方向长很多。大多数扫描仪允许在一个大范围内调整相位采样率，因此，矩形FOV的尺寸和形状可调整的自由度还比较大。

但是，矩形FOV技术有两个主要的缺点。首先，因为采集的相位编码步数变少，信噪比（SNR）与整FOV成像相比会降低。其次，如果成像物体的尺寸超过了定义的FOVp（相位编码方向上的FOV），卷折（混淆）就会发生。要想消除这些伪影，需要对病人仔细摆位，并且使用饱和带。

**参考材料**
     * Mezrich R. `A perspective on k-space <http://mriquestions.com/uploads/3/4/5/7/34572113/fourier.kspace.mezrich.1995.pdf>`_. Radiology 1995; 195: 297-315. [review].
     * Miller K. `MRI image formation (ppt) <http://mriquestions.com/uploads/3/4/5/7/34572113/miler-image_formation.ppt>`_. On-line lecture notes available at `users.fmrib.ox.ac.uk/~karla/teaching/image_formation.ppt <http://users.fmrib.ox.ac.uk/~karla/teaching/image_formation.ppt>`_

**相关问题**
	* `k空间与视野（FOV）和像素宽度的关系是什么？ <http://chunshan.github.io/MRI-QA/k-space/field-of-view-fov.html>`_
	* `Why does phase wrap-around occur? <http://mri-q.com/wrap-around-artifact.html>`_