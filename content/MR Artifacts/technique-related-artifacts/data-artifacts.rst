Question-其他伪影：我们还应该注意哪些其他数据相关的伪影？
============================================================================================================

:date: 2015-12-29
:tags: MR Artifacts, technique related artifacts
:slug: data-artifacts
:authors: Chunshan
:summary: Miscellaneous Artifacts

原文链接:\ `Are there any other data-related artifacts that we should be aware of? <http://mriquestions.com/data-artifacts.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/7856431_orig.png?296
    :alt: summary
    :align: center
    :width: 700

**中心点伪影**

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1873494_orig.jpg
   :alt: Central point artifact
   :align: right
   :width: 300

   中心点伪影

中心点伪影表现为图像正中心一个或明或暗的点。回顾磁共振扫描历史，这种伪影最初被误认为是多发性硬化斑块或腔隙性脑梗死。不要让这种情况在你身上发生！

中心点伪影是由接收器电路中一个恒定的直流（DC）电偏移导致的。理想情况下，当没有信号被记录时，接收器输出电压应为0。但是接收器偶尔会有漂移，在静息状态下也会一个小的或正或负的电压输出。当傅里叶变换时，这个小的常量偏移就会在图像中心产生一个信号的小尖峰。

在磁共振早期，这种伪影是一个常见的麻烦。然而由于射频相位变换和扫描仪电路中自校准检查的广泛使用，现在很少遇到。但是，如果直流偏移错误非常偶然地通过，中心点伪影还是会出现在图像中，所以要有所准备。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4955791_orig.gif
   :alt: Data clipping artifac
   :align: right
   :width: 300

   数据裁剪伪影

**数据裁剪**

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/5137061_orig.gif
   :alt: Data clipping artifac
   :align: left
   :width: 300

接收器放大器的增益如果校准不当可导致数据裁剪和诡异的数据，带有灰色背景的水模样图像。如果增益设置太高，射频信号超出了射频放大器的上限和下限截止水平（±Vmax），这种伪影就会发生。仔细校准和反复扫描是克服此伪影的唯一方法。   

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6865423_orig.gif
   :alt: Data Error Artifacts
   :align: right
   :width: 300

**数据错误伪影**

在数据处理链中不时产生的随机“毛刺”会导致图像中包含多条线，这些线纵横交错或者呈人字形。几个例子如下所示。通常，对裸数据简单地再处理就可以消除这种伪影，挽救一批不可辨读的图像。

+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4827677_orig.jpg?323 | .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6944682_orig.gif  |
|    :alt: Data Error Artifacts                                                     |    :alt: Data Error Artifacts                                                  |
|    :width: 350                                                                    |    :width: 350                                                                 |
|                                                                                   |                                                                                |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

**高级讨论**

一个常数的傅里叶变换是狄拉克函数δ(T)，是中心点伪影“尖峰”的来源。

同样地，(kx, ky)处一个错误的数据点会突出一个空间频率，反映在最终图像上就是此空间频率的一组平行线。

**参考材料**
     * Zhuo J, Gullapalli RP. `AAPM/RSNA physics tutorial for residents <http://mriquestions.com/uploads/3/4/5/7/34572113/zhuo_aritfacts_radiographics.pdf>`_. MR artifacts, safety, and quality control. Radiographics 2006;26:275-297.
     * Heiland S. `From A as in aliasing to Z as in zipper: artifacts in MRI <http://mriquestions.com/uploads/3/4/5/7/34572113/artifacts_a_to_z.pdf>`_. Clin Neuroradiol 2008; 1:25-36.

**相关问题**
	* `我们断断续续在我们图像看到拉链样伪影，它们是怎么产生的？ <http://chunshan.github.io/MRI-QA/technique-related-artifacts/zipper-artifact.html>`_
	* `Why is receiver gain adjustment necessary? What happens if it is set incorrectly? <http://mriquestions.com/receiver-gain.html>`_