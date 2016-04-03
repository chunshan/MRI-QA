Question-k空间：k空间是什么？
================================================================================

:date: 2014-10-01
:tags: K-space & Rapid Imaging, K-space (Basic)
:slug: what-is-k-space
:authors: Chunshan
:summary: k空间是什么？

原文链接:\ `What is k-space? <http://mriquestions.com/what-is-k-space.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1001270_orig.gif?240
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/9714122_orig.jpg
   :alt: k-space
   :align: right
   :width: 450

对许多学生而言，k空间的概念很可怕而且容易混淆，其实没有这么恐怖。k空间的核心可以用如下简单的术语定义：

**k空间是表示MR图像中空间频率的数组。**                                                       

k空间常见的图形表示看起来像“银河”，充满神秘感。k空间中的每一个“亮星”就是直接来自MR信号的数据点。每一个星的亮度代表该星特定的空间频率对最终图像的相对贡献。

虽然k空间“银河”与MR图像看起来非常不同，它们包含扫描对象的相同信息。这两种表示可以使用一种“高级”的数学方法（傅里叶变换，Fourier Transform）相互转换。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/_459970_orig.jpg
   :alt: K-space is the Fourier transform of the MR image
   :align: left
   :width: 400

   k空间是MR图像的傅里叶变换

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/__6298283_orig.jpg
   :alt: X-ray crystallography pattern of DNA
   :align: right
   :width: 200

   DNA的X射线衍射图案。
   这实际上就是分子螺旋结构的k空间表示。

k空间的数据单元通常在以kx和ky为主轴的矩形网格中显示，k空间中的kx和ky轴与图像中的水平轴(x-)和垂直轴(y-)对应，但是kx和ky轴表示x-和y-方向的空间频率而不是位置，k空间中每个数据点(kx,ky)也并不与图像中每个像素点(x,y)一一对应。k空间中每个点含有最终图像中所有像素的空间频率和相位信息，反过来，图像中的每个像素也映射到k空间中所有的点。MR图像的k空间表示因此类似于X线晶体学，光学或全息摄影中产生的衍射。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4956435_orig.jpg?597
   :alt: Each point in k-space maps to every point in the image
   :align: center
   :width: 800

   k空间中每一个点映射到图像中的所有点，反过来也一样

这是一个简单介绍。请看下面的“高级讨论”和本章节其他的Q&A对k空间的进一步解释。

**高级讨论**

k空间的概念公认比较抽象，难以想象。在过去的几年里，我尝试了许多不同的方法将此概念解释给我的学生，有不同程度的效果。下面是使用镜头作比喻的例子，许多人发现对理解k空间概念很有帮助。

.. figure:: http://mriquestions.com/uploads/3/2/7/4/3274160/optical-FT-upside-downnefertiti-2-way-with-grid.gif
   :alt: k space
   :align: center
   :width: 800

考虑透过一对透镜看著名的雕塑女王奈费尔提蒂，光波被雕塑反射进入第一片透镜，被第一片透镜折射（弯曲）作为空间频率的函数。低频率的光波仅被微弱的折射，直接穿过透镜的中心，高频率的光波在透镜边缘被折射地更强。第一个透镜的“输出”是高空间频率在周围低空间频率在中心的一系列散波。这些波既有建设性的干涉也有破坏性的干涉，可以认为第一个镜片对入射光线进行了“光学”傅里叶变换。

如果把你的头放在两片透镜之间（所谓的傅里叶平面），回头看女王，除了模糊的弥散的光什么都看不到，这些光就代表光线穿过第一片透镜的平均强度。这些光波是零散的，不会在你的视网膜上形成图像。你身处“光”的k空间。

第二片透镜逆转了这个过程，按照原来的关系重新聚集了在光学k空间分散的光波。第二片透镜进行的是傅里叶逆变换，重新塑造为聚焦的图像。

为什么当你把眼睛置于傅里叶平面内时看不到k空间“银河”中的图像？一个原因是眼睛仅对幅度敏感，而透镜将相位和幅度的信息混合在了一起。如果要检测光学k空间，需要一种更加复杂的设备，称为“4-f”装置。4-f装置含有一个高度准直的单色激光光源，一个放置在傅里叶平面的滤波器或屏幕，和一个敏感的电荷耦合探测器。这样的4-f实验通常在研究生水平的物理或工学的光学课程中展示，4-f装置也可以从科学教育机构购买。

即使女王奈费尔提蒂的例子还是不能帮助你，最重要的一点是：k空间是原对象固有空间频率的解构表示。对光波而言，从物体到光学k空间的变换通过一个透镜就能简单而且瞬时的实现，对MRI而言，过程更加复杂，也更为耗时，需要在使用多射频脉冲和可变梯度激发物体后对信号进行收集，但结果是一样的：产生k空间中按空间频率组织的数据阵列。在光学和磁共振成像中都一样，还需要一个逆过程，重新组装分散的信号波成为一幅连贯的最终图像。

**参考材料**
     * Brown TR, Kincaid BM, Ugurbil K. `NMR chemical shift imaging in three dimensions <http://mriquestions.com/uploads/3/4/5/7/34572113/pnas-1982-brown-3523-6.pdf>`_. Proc Natl Acad Sci USA 1982; 79:3523-6.
     * Ek L, Thaning A. `Fourier optics <http://mriquestions.com/uploads/3/4/5/7/34572113/fourieroptics_lab.pdf>`_. KTH Royal Institute of Technology, 2012.
     * Likes RS. `Moving gradient zeugmatography <http://mriquestions.com/uploads/3/4/5/7/34572113/us4307343.pdf>`_. US Patent #4307343 issued 22 Dec 1981. (First use of the term K-space in the MR literature I can find. He capitalized it!)   
     * Ljunggren S. `A simple graphical representation of Fourier-based imaging methods <http://mriquestions.com/uploads/3/4/5/7/34572113/ljunggren-kspace.pdf>`_. J Magn Reson 1983;54:338-343.
     * Mezrich R. `A perspective on k-space <http://mriquestions.com/uploads/3/4/5/7/34572113/ljunggren-kspace.pdf>`_. Radiology 1995; 195: 297-315. [review]. 
     * Sykora S. `K-space formulation of MRI <http://mriquestions.com/uploads/3/4/5/7/34572113/stans_k-space_formulation_of_mri.pdf>`_. 2005. (A generalized mathematical formulation that is not too difficult to follow found on-line at `http://www.ebyte.it/library/educards/mri/K-SpaceMRI.html <http://www.ebyte.it/library/educards/mri/K-SpaceMRI.html>`_)
     * Twieg DB. `The k-trajectory formulation of the NMR imaging process with applications in analysis and synthesis of imaging methods <http://mriquestions.com/uploads/3/4/5/7/34572113/twieg-kspace.pdf>`_. Med Phys 1983; 10: 610-621.

**相关问题**
	* `k空间中点与图像中的点并不对应，它们的意义是什么？ <http://chunshan.github.io/MRI-QA/k-space/parts-of-k-space.html>`_
	* `从哪儿获得数据填充k空间？ <http://chunshan.github.io/MRI-QA/k-space/data-for-k-space.html>`_	