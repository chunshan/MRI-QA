Question-视野与k空间：k空间与视野（FOV）和像素宽度的关系是什么？
========================================================================================

:date: 2014-10-17
:tags: K-space & Rapid Imaging, K-space (Advanced)
:slug: field-of-view-fov
:authors: Chunshan
:summary: k空间与视野（FOV）和像素宽度的关系

原文链接:\ `How does k-space relate to field-of-view (FOV) and pixel width? <http://mri-q.com/field-of-view-fov.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/9239262_orig.png?297
    :alt: summary
    :align: center
    :width: 700

视野（Field-of-view，FOV）指的是MR图像采集或显示时的距离（用cm或mm表示）。FOV一般被分为几百个图像元素（像素），每一个的尺寸大约为1mm²。虽然不同方向上FOV和像素尺寸可以不同，为了能够解释地更清楚，我们仅考虑对称的情况，二维的情况下，FOVx = FOVy = FOV 并且 Δx = Δy = Δw。

定义好了视野（FOV）和像素宽度（Δw）就决定了k空间中数字化采样的数目，必须采集够这些数目，才能重建出所需分辨率的图像。像下表所示，FOV反比于k空间中采样之间的间距，具体来说，Δk = 1/FOV。

从对称性上考虑，像素宽度（Δw）和k空间中空间频率最大的正值（+kmax）和负值（−kmax）之间的范围也成反比。假设定义kFOV = (+kmax) − (−kmax) = 2kmax，Δw和kFOV之间的关系为Δw = 1/kFOV。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/1157917_orig.gif?546
   :alt: relation between k-space and field-of-view and pixel width
   :align: center
   :width: 800

对大多数人而言，Δk = 1/FOV 或者 Δw = 1/kFOV这样的关系并不是显而易见的，反而因此增加了混乱。希望下面的讨论能够让你对这些重要的结果感觉比较舒服一些。首先我们考虑为什么Δk = 1/FOV。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6816238_orig.gif?345
   :alt: Δk and FOV
   :align: right
   :width: 400

回忆前面一个Q&A中讲到傅里叶分析会将一个简单的信号分解为一系列不同谐波频率（ω, 2ω, 3ω等）的正弦波的和。

在k空间中成像物体空间频率的傅里叶投影也遵循傅里叶分析中简单的模式，只是复指数(cos nωt + i sin nωt)代替了简单的正弦波，但振荡频率仍然是ω（1/FOV）的整数倍。k空间中连续的两条采样线相差1/FOV。例如，线kn+1和kn之间的空间频率差异（Δk = kn+1 − kn）为Δk = (n+1)/FOV − n/FOV = 1/FOV。

与表达式Δk = 1/FOV一样，方程Δw = 1/kFOV也不是一眼就能看出来的。这种情况下，我们要考虑需要k空间中的多少相位周期来近似表征最小所需尺寸（Δw）的图像。

如下图所示，答案是至少需要一个完整的相位周期以唯一区分每个像素。如果视野FOV内有宽为Δw的N个像素，那么需要N个相位周期。我们前面定义kFOV = 2kmax对应于此要求的空间频率。由于空间频率(k)为[周期/距离]，我们可以将kFOV表示为kFOV = N /FOV。但是像素宽度（Δw）等于FOV / N。所以直接有kFOV = 1 /Δw。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8126576_orig.gif?511
   :alt: Δw and kFOV
   :align: center
   :width: 800

这两个成对儿的方程之所以重要是因为它们揭示了k空间中的间距或者采样的位置如何影响FOV和像素宽度。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/6578634_orig.png
   :alt: Inverse relationship between spacing of data samples (Δk) and image field-of-view
   :align: right
   :width: 500

   数据采样间隔(Δk)和图像FOV之间的反比关系

第一个例子演示了数据间隔和图像FOV之间的反比关系。左边，k空间数据采样率对应于FOV为30cm的图像。右边，数据点之间的间隔（Δk）翻倍了，结果是图像的像素尺寸不变但是FOV仅有原来的一半（15cm）。在此小FOV外部的脑的外缘“卷折”到重建图像的对侧，这种现象称为混叠。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4613719_orig.png
   :alt: Inverse relationship between pixel width (Δw) and range of sampled k-space frequencies
   :align: right
   :width: 500

   像素宽度（Δw）和k空间频率的采样范围（kFOV）之间的反比关系

第二个例子中，我们保持数据采样率和间隔（Δk）不变，但是我们仅取k空间中间三分之一的采样数据，也就是将kFOV减少为原来的1/3。对k空间进行这种操作后，FOV保持不变，但是像素宽度（Δw）翻了三倍，从1mm变为3mm。变大的像素尺寸意味着平面内的空间分辨率下降了，这个结果在意料之中，因为只有k空间中间低频率的点被采样了。

如果你仍然感到困惑，不要担心，毕竟这个话题属于“k空间高级话题”。对于更想从数学上一窥究竟的好学者，下面由Eric Wong给的YouTube视频可以提供更进一步的视角。

**参考材料**
     * Mezrich R. `A perspective on k-space <http://mriquestions.com/uploads/3/4/5/7/34572113/fourier.kspace.mezrich.1995.pdf>`_. Radiology 1995; 195: 297-315. [review].
     * Miller K. `MRI image formation (ppt) <http://mriquestions.com/uploads/3/4/5/7/34572113/miler-image_formation.ppt>`_. On-line lecture notes available at `users.fmrib.ox.ac.uk/~karla/teaching/image_formation.ppt <http://users.fmrib.ox.ac.uk/~karla/teaching/image_formation.ppt>`_

**相关问题**
	* `How does one obtain a rectangular field of view? Why would you want to use it? <http://chunshan.github.io/MRI-QA/k-space/k-space-grid.html>`_