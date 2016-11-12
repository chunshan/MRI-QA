Question-双回波FSE：双回波FSE序列如何工作？似乎没有足够的空间放置两套回波。
=====================================================================================================================

:date: 2014-10-29
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: dual-echo-fse
:authors: Chunshan
:summary: 双回波FSE序列

原文链接:\ `How does a dual-echo FSE sequence work? It seems there is not enough room for the two sets of echoes. <http://www.mri-q.com/dual-echo-fse.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/8062216_orig.png?305
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/1961184_orig.jpg
   :alt: Dual-echo FSE
   :align: right
   :width: 600

   双回波FSE。TR = 3000ms，TEeff 分别为17和85ms，分别产生质子密度和T2加权像。

磁共振进入临床的前20年，双回波序列是几乎所有身体部位标准协议的一部分。使用长重复时间（TR），短和长回波时间（TE）时分别采集回波信号实现在一次采集中产生质子密度和T2加权像。在过去的10年里，对于神经成像而言T2-FLAIR很大程度上取代了质子密度序列，但是双回波序列在肌肉骨骼和身体其他应用中仍然有用。

双回波FSE图像可以通过一个称为视图共享的过程得到。在FSE回波链的早期和后期都进行零和低振幅相位编码，这会产生有效TE分别为短和长（通常TE1eff <20 ms，TE2eff >80 ms）的两套低空间分辨率图像，分别反映质子密度加权和T2加权占主要对比度。剩余的包含边缘细节的中等和高幅值相位编码产生的信号被两套数据集共享，用于最后的图像重建。

**参考材料** 
     * Johnson B, Fram EK, Drayer BP, et al. `Evaluation of shared-view acquisition using repeated echoes (SHARE): a dual-echo fast spin-echo MR technique <http://www.mri-q.com/uploads/3/4/5/7/34572113/share_fse_667.full.pdf>`_. Am J Neuoradiol 1994;15:667-673.
     * Mekle R, Laine AF, Wu EX. `Combined MR data acquisition of mulitcontrast images using variable acquisition parameters and k-space data sharing <http://www.mri-q.com/uploads/3/4/5/7/34572113/mekle_k-space.pdf>`_. IEEE Transact Med Imaging 2003; 22:806-823.

**相关问题**
	* `什么是快速自旋回波成像？ <http://chunshan.github.io/MRI-QA/rapid-imaging/what-is-fsetse.html>`_