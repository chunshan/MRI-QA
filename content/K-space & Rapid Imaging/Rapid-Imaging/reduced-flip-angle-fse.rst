Question-减小翻转角的FSE：为什么想要在FSE中减小翻转角？小翻转角难道不会使MR信号消失么？
======================================================================================================================

:date: 2014-10-31
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: reduced-flip-angle-fse
:authors: Chunshan
:summary: 在FSE中减小翻转角

原文链接:\ `Why would you want to use reduced flip angles in FSE? Wouldn't smaller flip angles kill the MR signal? <http://mriquestions.com/reduced-flip-angle-fse.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/1531600_orig.png?301
    :alt: summary
    :align: center
    :width: 700

快速自旋回波的一个主要限制是组织过度发热，这是FSE设计中180°脉冲密集使用必然带来的后果。RF脉冲产生的能量沉积正比于翻转角的平方（α²），因此，180°脉冲沉积的能量是90°脉冲的4倍。

RF翻转角从180°减小到50°-150°的范围，热能量沉积可以显著减少，但小翻转角不也会造成MR信号减小么？答案是yes，但可能没有想象中那么多。

当RF翻转角减小到180°以下，每一个回波的磁化矢量不再单纯回聚于横向平面。磁化强度的相当一部分“存储”在纵向方向，通过T1弛豫机制增长。回波链中连续的每一个非180°脉冲都会将磁化强度分解为纵向和横向分量，这些存储的纵向分量会不断产生受激回波，而且对磁共振信号的贡献逐渐变大，此时磁共振信号既依赖于T1也依赖于T2。受激回波使得当翻转角变小时获得的信号比预期要大。

对一组具有相同翻转角（α <180°）的回聚脉冲，系统最初会振荡但是横向磁化会达到一种伪稳态（PSS，pseudo-steady state），与全部为180°脉冲相比造成信号幅值减小至约sin(α/2)倍。因此，如果使用100°脉冲而不是180°脉冲，FSE信号将减少至其最大值的sin(50º) ≈ 77%。一旦稳态建立，PSS的水平随着FSE回波链中翻转角的变化而变化。这项技术可简写为TRAPS（TRansition between Pseudo-steady States），并说明如下。

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/4759292_orig.gif?631
   :alt: reduced flip angle FSE imaging
   :align: center
   :width: 800

   减小翻转角FSE成像的三种方法。第一种情况，全部使用100°RF脉冲使得几个震荡后出现伪稳态（PSS）。第二种情况在序列一半时增加翻转角到120°使伪稳态发生转换。第三种情况开始处使用预备脉冲，然后使用倾斜变化的翻转角。由此产生的理论信号强度在下面显示（忽略T1和T2效应）。

对减小翻转角方法的其他几种改进会使得平均信号更高，能量沉积更低。在序列开始之前使用一组5-10个预备或“启动”脉冲可以显著增加PSS的初始水平。另外一种修改是使翻转角呈线性或正弦斜坡沿回波链从小到大。在回波链的早期使用最小的翻转角，此时纵轴储存了磁化强度的很大一部分，这些储存的磁化强度会使得在回波链的后面产生更强的信号。在最低阶的相位编码步骤中应用最大的翻转角，因为此时的信号决定整体的MR信号和基本的图像对比度。第三种修改是使用对称的强回波，这是 `下面一个Q&A <http://mriquestions.com/hyperechoes.html>`_ 的主题。

**参考材料** 
    * Alsop DC. `The sensitivity of low flip angle RARE imaging <http://mriquestions.com/uploads/3/4/5/7/34572113/alsop_low_flip_angle_rare.pdf>`_. Magn Reson Med 1997;37:176–184.
    * Busse RF, Brau ACS, Vu A, et al. `Effects of refocusing flip angle modulation and view ordering in 3D fast spin echo <http://mriquestions.com/uploads/3/4/5/7/34572113/busse_variable_fa_3dfsenihms127396.pdf>`_. Magn Reson Med 2008;60:640-649.     
    * Hennig J, Weigel M, Scheffler K. `Multiecho sequences with variable refocusing flip angles: optimization of signal behavior using smooth transitions between pseudo steady states (TRAPS) <http://mriquestions.com/uploads/3/4/5/7/34572113/traps_abstract.pdf>`_. Magn Reson Med 2003;49:527–535.
    * Mugler JP III. `Optimized three-dimensional fast spin echo MRI <http://mriquestions.com/uploads/3/4/5/7/34572113/hyperechoes_weigel.pdf>`_. J Magn Reson Imaging 2014;39:745-767. (Excellent up-to-date review).

**相关问题**
  * `什么是“强回波”？与普通回波有什么不同？ <http://chunshan.github.io/MRI-QA/rapid-imaging/hyperechoes.html>`_
  * `What is a stimulated echo? <http://mriquestions.com/stimulated-echoes.html>`_