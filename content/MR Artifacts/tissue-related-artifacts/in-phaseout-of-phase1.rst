Question-同相和失相：同相位（in-phase）成像和失相位（out-of-phase）成像意思是什么？
============================================================================================

:date: 2015-11-24
:tags: MR Artifacts, tissue related artifacts
:slug: in-phaseout-of-phase1
:authors: Chunshan
:summary: 同相位（in-phase）成像和失相位（out-of-phase）成像意思是什么？

原文链接:\ `What is meant by in-phase vs out-of-phase imaging? <http://www.mri-q.com/in-phaseout-of-phase1.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/1493888_orig.png?290
    :alt: summary
    :align: center
    :width: 700

像在前一个Q&A中所描述的，同一个体素中水和脂肪信号间的相位取消导致梯度回波图像上第二类化学位移伪影的产生。这种伪影表现为器官和解剖结构在水-脂肪交界处的黑线。这种伪影的幅度依赖于水和脂肪间的相位循环，1.5T下由于化学位移导致的相位循环的频率约215Hz。

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/1046728_orig.gif
   :alt: phase cancellation artifact
   :align: right
   :width: 450

1.5T下，同相和失相之间的相位循环约每2.2ms发生一次。3.0T时循环速度加倍，每1.1ms发生一次。1.5T下采集的梯度回波图像当TE为2.2ms，6.6ms，11.0ms时称为失相（Out Of Phase，OOP），TE为4.4ms，8.8ms等值时称为同相（In Phase，IP）。

到1980年代末，一些研究者开始意识到相位消除效应可以在临床上用来识别甚至量化组织（如肝）中的脂肪含量。今天这一原则一个特别常见的应用是帮助区分肾上腺腺瘤（通常包含脂肪）和癌及转移瘤（一般不含脂肪）。其他各种腹部病变的诊断，包括血管平滑肌脂肪瘤，肾透明细胞癌和肝局灶性脂肪侵润都可以通过IP-OOP成像辅助诊断。这种技术在下图说明，包含一对梯度回波图像，有相同TR但是不同TE，一个同相，一个失相。如果病变处信号强度在OOP图像上显著下降说明很可能包含显微脂肪。因此，IP/OOP扫描是目前大多数腹部成像协议的一种标准组成部分。

+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/4404998_orig.jpg?246      | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/5503468_orig.jpg      | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/9856587_orig.jpg?169      |
|    :alt: Lipid-rich adrenal adenoma (arrow)                                         |    :alt: Out-of-phase GRE image at TE=2.2 msec                                  |    :alt: Lipid droplets (arrow) in adrenal adenoma.                                 |
|    :width: 300                                                                      |    :width: 300                                                                  |    :width: 150                                                                      |
|                                                                                     |                                                                                 |                                                                                     |
|    富含脂肪的肾上腺腺瘤（箭头）。同相的梯度回波图像（TE=4.4ms）显示中等强度信号肿瘤 |    失相的梯度回波图像（TE=2.2ms），腺瘤（箭头）信号下降，有相位取消伪影。       |    肾上腺腺瘤中的脂滴（箭头）                                                       |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/5292881_orig.jpg?242      | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/5894731_orig.jpg      | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/9983895_orig.jpg          |
|    :alt: Hepatic steatosis. In-phase GRE with TE=4.4 msec.                          |    :alt: Reduction in hepatic signal                                            |    :alt: Specimen shows lipid droplets                                              |
|    :width: 300                                                                      |    :width: 300                                                                  |    :width: 150                                                                      |
|                                                                                     |                                                                                 |                                                                                     |
|    肝脂肪变性。同相的梯度回波图像（TE=4.4ms）                                       |    失相梯度回波图像（TE=2.2ms）上肝脏信号降低                                   |    标本上显示存在脂滴                                                               |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

**参考材料**
     * Outwater EK, Blasbalg R, Siegelman ES, Vala M. `Detection of lipid in abdominal tissues with opposed-phase gradient-echo images at 1.5T: techniques and diagnostic importance <http://www.mri-q.com/uploads/3/4/5/7/34572113/outwater_fat_waterradiographics2e182e62e9821195.pdf>`_. Radiographics 1998; 18:1465-80.

**相关问题**
	* `什么是第二类化学位移伪影（Chemical Shift:2nd Kind）？ <http://chunshan.github.io/MRI-QA/tissue-related-artifacts/chemical-shift-2nd-kind.html>`_
	* `How do you produce multiple GRE's from a single pulse? <http://www.mri-q.com/multi-echo-gre.html>`_