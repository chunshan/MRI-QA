Question-零插值填充：某些序列中可选择使用零插值填充（ZIP，Zero-Interpolation Filling）技术，这是一种文件压缩方式么？
================================================================================================================================

:date: 2014-10-23
:tags: K-space & Rapid Imaging, K-space (Advanced)
:slug: zip
:authors: Chunshan
:summary: 零插值填充

原文链接:\ `A option called ZIP is available for some sequences. Is this a type of file compression? <http://mri-q.com/zip.html>`_

**概要** 
 .. figure:: http://mri-q.com/uploads/3/4/5/7/34572113/14101_orig.png?293
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/7015770_orig.gif?286
   :alt: Zero filling
   :align: right
   :width: 400

处理MRI数据通常在阵列处理器上运行快速傅里叶变换（Fast Fourier Transform，FFT）算法。这些计算一般要求输入数据（一个矩阵）的维度是2的幂，比如128x128, 256x256, 或者512x512。如果采集k空间数据不能完全填充这样的矩阵，习惯上以零点填充缺失的数据，这种技术称为零填充或者零插值填充（Zero-Interpolation Filling，ZIP）。

MRI中的ZIP与文件压缩中的*.zip技术毫无关系，与邮政编码也毫无关系！

零填充通常用于扩展图像矩阵在相位编码方向上的尺寸，对2D成像而言，图像矩阵尺寸的增加是“平面内”（如从256个像素变为512个像素），对3D成像而言，零填充可“跨平面”用于增加选层方向上的显示分辨率（如从64层变为128层）。图像矩阵尺寸的第一次翻倍时这种技术会带来好处，此后，将没有任何收益。

虽然零填充不会增加输入裸数据的任何信息，但它可以提高图像显示的空间分辨率，减少了部分容积伪影。零填充实际上利用临近体素的信号进行插值的方法，会使得图像看起来更平滑，降低图像的“马赛克”效应。

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/8121028_orig.jpg?464
   :alt: Examples of cranial MRAs without and with zero-interpolation filling
   :align: center
   :width: 700

   使用/不使用零填充（Zero-Interpolation Filling, ZIP）技术的头部MRA。左边，使用128x128和256x256（全部数据）矩阵获得的图像；右边，使用了零填充，图像矩阵尺寸分别变为256x256和512x512。注意图像质量上的改进，特别是128x128的数据集

**高级讨论**

为什么零填充与图像空间中的像素插值效果类似？背后的数学有些难，感兴趣的读者可以参考下面的文献（尤其是Bartholdi-Ernst的文章）。

简单来说，无论选择多大的矩阵，总是比一个物体理论上无限的k空间表示要小，必须在某个点上截断（缩短）。截断等效于k空间数据与一个“厢式车”/矩形函数相乘，等效于在图像空间与SINC函数（矩形函数的傅里叶变换）进行卷积。零填充会在显示矩阵中产生额外的SINC插值的像素。

一个令人着迷的结果是，使用零填充将数据点首次翻倍时实际上增加了“新鲜的信息”，而不只是简单的插值。额外的零怎么会添加“新数据”？原因是普通的FFT不会提取FID中所有可用的信息，通过将数据点翻倍，FFT在提取所有“真实数据”时变得更加有效。也就是说并不是ZIP创造了新信息，而是标准FFT不能挖掘出所有可用的信息。初始的倍增之后，优势不会继续增加，因为傅里叶系数变得彼此完全相关，所以数据处理时只会进行一次ZIP处理。

如上所述，2D成像中，ZIP的应用是“平面内”的；3D成像中，ZIP可以在“平面内”，“平面间”或二者同时应用。各厂商对这两种类型的ZIP技术也有不同的命名，比如，GE将平面内的ZIP技术称为“ZIP 512”或“ZIP 1024”，将跨平面的ZIP技术称为“ZIP x 2”或“ZIP x 4”。

**参考材料**
     * Bartholdi E, Ernst RR. `Fourier spectroscopy and the causality principle <http://mri-q.com/uploads/3/4/5/7/34572113/bartholdi_ernst_ft_causality_main.pdf>`_. J Magn Reson 1973; 11:9-19.   
     * Bernstein MA, Fain SB, Riederer SJ. `Effect of windowing and zero-filled reconstruction of MRI data on spatial resolution and acquisition strategy <http://mri-q.com/uploads/3/4/5/7/34572113/bernstein_windowing_zip.pdf>`_. J Magn Reson Imaging 2001;14:270-280.
     * Du YP, Parker DL, Davis WL, Cao G. Reduction of partial volume artifacts with zero-filled interpolation in three dimensional MR angiography. J Magn Reson Imaging 1994; 4:733-741     
     * Ebel A, Dreher W, Leibfritz D. `Effects of zero-filling and apodization on spectral integrals in discrete Fourier-transform spectroscopy of noisy data <http://mri-q.com/uploads/3/4/5/7/34572113/zip_ac.els-cdn.com_s1090780706001911_1-s2.0-s1090780706001911-main.pdf>`_. J Magn Reson 2006;182:330-338.

**相关问题**
	* `为什么k空间被画为网格状？k空间的轴意味着什么？ <http://chunshan.github.io/MRI-QA/k-space-grid.html>`_