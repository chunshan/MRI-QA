Question-化学位移的相位效应：水和脂肪质子的化学位移难道不会导致它们之间的相位变化么？如果如此，为什么化学位移伪影在相位编码方向没有出现？
=================================================================================================================================================

:date: 2015-11-21
:tags: MR Artifacts, tissue related artifacts
:slug: chemical-shift-in-phase
:authors: Chunshan
:summary: 化学位移的相位效应

原文链接:\ `Doesn't the chemical shift between water and fat protons also result in a phase shift between them? If this is so, then why aren't chemical shift artifacts seen in the phase-encode direction also? <http://www.mri-q.com/chemical-shift-in-phase.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/3042442_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4331262_orig.jpg
   :alt: EPI image with chemical shift artifact in PE direction
   :align: left
   :width: 400

   相位编码方向上有化学位移伪影的EPI图像(↑)

实际上，水和脂肪质子之间的化学位移不仅指两者之间的频率位移，也有相位位移。在常规自旋卷折成像中，脂肪质子相对于水质子的相位偏移在相位编码方向上不会累积，因此，如果给定成像位置，连续的相位编码步骤之间水和脂肪的相位偏移是一个常量。由于傅里叶变换在给相位编码方向上的空间位置赋信号值时考虑了相位差，常规的自旋回波或梯度回波成像中，相位编码方向上不会发生水-脂肪位置失配。

然而，在平面回波成像（EPI）中会发生完全相反的现象。化学位移伪影在频率编码方向上很小在相位编码方向上可能极大。自旋卷折和平面回波技术之间存在这种差异的原因是由于后者采集数据的方式不同。

在EPI中，一次射频激发后会立刻采集所有行的裸数据，频率编码方向上每个像素的带宽非常大（如在50-100kHz的级别），因此化学位移伪影不显著。然而在相位编码方向上，每个像素的带宽非常小（在1kHz的级别），因为所有的相位编码行只有几十毫秒就采集完成了。1.5T下，脂肪/水的化学位移约215Hz，相位编码方向上的窄带宽会造成10+像素宽的显著伪影。平面回波技术必须使用特殊的校正和修正方法来最小化脂肪信号，消除化学位移伪影。

**参考材料**
     * Jezzard P, Balaban RS. `Correction for geometric distortion in echo planar images from Bo field variations <http://www.mri-q.com/uploads/3/2/7/4/3274160/jezzardbalabanmrm95.pdf>`_. Magn Reson Med 1995;34:65-73.

**相关问题**
	* `什么是化学位移伪影？ <http://chunshan.github.io/MRI-QA/tissue-related-artifacts/chemical-shift-artifact.html>`_