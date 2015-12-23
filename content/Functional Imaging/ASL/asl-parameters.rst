Question-ASL成像参数 - 如何选择成像参数来优化ASL的采集？
=======================================================================================

:date: 2015-11-07
:tags: Perfusion, ASL
:slug: asl-parameters
:authors: Chunshan
:summary: 如何选择成像参数来优化ASL的采集

原文链接:\ `How should imaging parameters be chosen to optimize an ASL acquisition? <http://www.mri-q.com/asl-parameters.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/19616_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/2204283_orig.jpg?177
   :alt: Children have higher relative blood flows and shorter mean transit times than adults
   :align: right
   :width: 300 

   儿童有相对成年人更高的血流量，更短的平均通过时间。

最佳成像参数的选择依赖于使用的ASL方法（2D vs 3D， PICORE vs FAIR vs pCASL等）。即使每个序列小的变种（如背景抑制和脉冲形状的类型）都会影响参数选择。预期的血流量也应该考虑，如儿童比成人有更强的血液循环。许多选择是经验型的，因此应该从厂商或是脉冲序列设计人员推荐的参数开始。也就是说，一些一般的规则适用于任何一种ASL实现。

1. **成像平面**  所有ASL方法在垂直于成像板的横断面上采集图像时效果最好。
2. **设备**  使用尽可能高的磁场强度。ASL技术的信噪比（SNR）有限，因此3.0T比1.5T或更低场强有更好的效果。必须使用多通道线圈。低级别的并行加速（R≈2）对3D采集或许有用，但是对2D采集就需要谨慎采用，因为会造成信噪比损失。
3. **重复时间（TR）** 需要足够长使得标记的自旋在两次采集之间真正驰豫，通常大于3500ms。
4. **最小回波时间（TE）** 应总是使用最短回波时间防止信号T2/T2*衰减。
5. **空间分辨率**  避免“高分辨率”成像。以目前的技术状态，SNR上的考虑需要获取的图像分辨率必须比较低，而不能从标准诊断要求的分辨率上考虑。2D ASL的平面矩阵一般在64x64到128x128之间，相应的层厚在4-6mm之间。3D ASL各向同性是可行的但是由于图像采集时间的限制仍然选择各向异性。
6. **信号平均**  为了在合理的成像时间（4-6分钟）获得可接受的SNR，需要取多个信号的平均值。2D技术而言，3.0T情况下需要取30到50个信号平均，1.5T情况下更多。对3D技术而言，需要2-4个信号平均。
7. **标记持续时间和标记后延迟反转时间（TI）** 这取决于磁场强度，使用的ASL方法和预期的血流速度。如果是1.5T下的脑成像，PASL的标记持续时间为700ms，pCASL为1500ms，TI值则一般为1800ms。由于3.0T下血液的T1更长，TI也需要稍微延长。如果预期动脉血流比较慢，如老年患者或血管病变与低心输出量患者，TI也需要延长。相反，对儿童建议使用较短的TI因为他们的血液循环更快。
8. **破碎梯度**  它们的使用是有争议的。尽管可以减少血流相关的伪影，但是也需要延长最短TE，因此SNR减小。它们也会在ASL图像中引入更多T2（T2*）对比度，这种效应必须在定量血流测量中考虑。破碎梯度也可能从ASL图像中去除重要的临床信息，如延迟或侧支循环。
9. **背景抑制**  对每个TR使用单一激励的隔离的3D成像方法是必须的。背景抑制对多层的2D方法不是很有效、高效，因此是可选的。背景抑制会略微减弱ASL信号（约5%），如果要做定量血流测量，这种效应要考虑在内。

**高级讨论**

一些软件为了更高的性能，使用快速，非常低分辨率的多TI ASL序列来评估血团到达时间。如果这种技术可用，可以为每个患者选择最优的TI。

**参考材料**
    * Alsop DC, Detre JA, Gola X, et al. `Recommended implementation of arterial spin-labeled perfusion MRI for clinical applications: A consensus of the ISMRM perfusion study group and the European consortium for ASL in dementia <http://www.mri-q.com/uploads/3/2/7/4/3274160/recommended_implementation_of_asl.pdf>`_. Magn Reson Med 2015; 73:102-116.
    * Ferré J-C, Bannier E, Raoult H, et al. `Arterial spin labeling (ASL) perfusion: techniques and clinical use <http://www.mri-q.com/uploads/3/2/7/4/3274160/asl_review_1156841300209x_1-s2.0-s221156841300209x-main.pdf>`_. Diagn Interv Radiol 2013; 94:1211-1223
    * Wong EC. `Quantifying CBF with pulsed ASL: technical and pulse sequence factors <http://www.mri-q.com/uploads/3/2/7/4/3274160/wong-2005-journal_of_magnetic_resonance_imaging.pdf>`_. J Magn Reson Imaging 2005; 22:727-731.
    * Ye FQ, Mattay VS, Jezzard P, et al. `Correction for vascular artifacts in cerebral blood flow values measured by using arterial spin tagging techniques <http://www.mri-q.com/uploads/3/2/7/4/3274160/wong-2005-journal_of_magnetic_resonance_imaging.pdf>`_. Magn Reson Med 1997; 37:226–235. (use of bipolar crusher gradients to suppress ASL signal in large arteries)

**相关问题**
	* `您能解释一下各种ASL方法的不同之处么？哪一种最好？ <http://chunshan.github.io/MRI-QA/asl/pasl.html>`_