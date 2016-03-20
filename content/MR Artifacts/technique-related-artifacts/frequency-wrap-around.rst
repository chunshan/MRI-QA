Question-卷折方向：为什么卷折伪影在频率编码方向上看不到？
================================================================================

:date: 2015-12-24
:tags: MR Artifacts, technique related artifacts
:slug: frequency-wrap-around
:authors: Chunshan
:summary: 为什么卷折伪影在频率编码方向上看不到？

原文链接:\ `Why aren't wrap-around artifacts seen in the frequency-encode direction, too? <http://mri-q.com/frequency-wrap-around.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/7941466_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/5564610_orig.gif?297
   :alt: frequency aliasing
   :align: right
   :width: 400

卷折（混叠（aliasing）的一种）是数字信号处理的一种基础现象，理论上在相位编码和频率编码方向上都会出现。这一现象的基础如右图所示，高频信号的采样频率不够，被错误地当做低频信号。这种高频信号错配到低频会导致MR图像空间上的模糊，或卷折伪影。

为了避免频率混叠，磁共振信号的数字采样频率必须至少是信号最高频率的两倍，这个关键的采样频率称为Nyquist频率。如果采样频率低于Nyquist频率，高频信号被错认为低频信号的情形就会发生。

与在相位编码方向上的混叠不同，频率编码方向上的混叠在现代临床磁共振成像中通常不是问题。这是因为频率混叠被两种方法基本消除了：1）信号过采样；2）图像重建前的带通滤波。

过采样意味着采集了比显示所需分辨率更多的磁共振信号数据。在大多数现代磁共振扫描仪中，每个回波期间要采集512-1024次磁共振信号（虽然频率编码方向上的显示分辨率通常取为256）。换句话说，Nyquist采样率是信号最高频率的2-4倍。因为这项任务仅通过增加采样电路的数字化频率就可以完成，基本没有时间上的损失。

大多数磁共振扫描仪中默认的频率过采样系数为2倍，虽然此过采样因子是可调的。不同厂商对此技术也有不同的称呼，“频率过采样（frequency oversampling）”（Siemens，Philips，Hitachi），“抗混叠（anti-aliasing）”（GE），“频率卷折抑制（frequency-wrap suppression）”（Toshiba）。

带通滤波可以是模拟的，数字的或混合的，这种方法可以消除假的高频分量。这种滤波器允许期望带宽内的所有频率成分通过，但衰减/拒绝选择范围之外的频率分量。

由于在图像重建前对原始磁共振信号的过采样和滤波，现代MRI中频率编码方向上的混叠在不知不觉中被有效消除了。

**参考材料**
     * Pusey E, Yoon C, Anselmo ML, Lufkin RB. Aliasing artifacts in MR imaging. Comput Med Imag Graphics 1988;12:219-224.  

**相关问题**
	* `什么是混叠？ <http://chunshan.github.io/MRI-QA/technique-related-artifacts/aliasing.html>`_