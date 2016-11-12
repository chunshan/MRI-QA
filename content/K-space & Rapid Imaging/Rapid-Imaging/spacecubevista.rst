Question-3D FSE：什么是SPACE/CUBE/VISTA技术？
======================================================================================================================

:date: 2014-11-02
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: spacecubevista
:authors: Chunshan
:summary: 3D Fast Spin Echo

原文链接:\ `What are the SPACE/CUBE/VISTA techniques? <http://mriquestions.com/spacecubevista.html>`_

**概要** 
 .. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/6802947_orig.png
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://mriquestions.com/uploads/3/4/5/7/34572113/635710_orig.jpg
   :alt: T2-FLAIR-CUBE brain images
   :align: right
   :width: 400

   T2-FLAIR-CUBE大脑图像

它们是密切相关的快速自旋回波技术，做了一些特殊的修改实现各向同性3D成像的最优化。各向同性指的是3D采集产生的体素在每个方向上尺寸一致，比如0.6mm x 0.6mm x 0.6mm，使得图像在任何一个方向上重建时有相同的分辨率。

CUBE仅是GE此序列的名字而不是简称，VISTA是Philips的版本，是“Volume ISotropic Turbo spin echo Acquisition”的简写，Hitachi的名字是isoFSE，Toshiba则成为3D MVOX（“MultiVOXel”），Siemens的名字可能最有创意，SPACE（“Sampling Perfection with Application optimized Contrasts using different flip angle Evolution”）。

厂商之间对此技术的具体实现各有不同，但有如下通用的元素：
* 3D快速自旋回波采集
* 很长的回波链长度，通常100-250个回波
* 超短的回波间隔，通常3-4ms
* 非选择性地回聚脉冲
* 减小的翻转角（可能是常数但通常是可变的，一般30°-120°，减少组织发热）
* 1D或2D并行采集减少成像时间
* 使用零填充的部分傅里叶成像减少成像时间
* 使用最优化/有效的k空间采样轨迹，包括信号演变过程中在平面内和平面间的相位编码方向上同时采样
* 能够产生T1加权，T2加权，质子密度加权或FLAIR图像
* 合理的成像时间（5-10min）

SPACE/CUBE/VISTA技术已经被证明在广泛的临床应用中都有价值，主要可以分为两大类：

* 复杂解剖结构（大脑，内耳，关节，MRCP）所需的高分辨率，连续，薄层各项同性图像
* 部分2D采集（脊柱，盆腔）的替代

.. raw:: html

    <div>
        <div class="wsite-flash"><div style="padding-top: 0px; padding-bottom: 0px; text-align: center;">
        <object type="application/x-shockwave-flash" codebase="//download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,0,0" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" align="middle"  height="256px" width="256px" >
          <param name="movie" value="http://mriquestions.com/uploads/3/4/5/7/34572113/knee.swf"> 
          <param name="quality" value="high"> 
          <param name="play" value="true"> 
          <param name="loop" value="true"> 
          <param name="wmode" value="transparent"> 
          <param name="allowFullScreen" value="true"> 
          <param name="flashvars" value=""> 
          <embed src="http://mriquestions.com/uploads/3/4/5/7/34572113/knee.swf" quality="high" pluginspage="//www.macromedia.com/go/getflashplayer" play="true" loop="true" wmode="transparent" allowfullscreen="true" flashvars="" type="application/x-shockwave-flash" align="middle"  height="256px" width="256px"></embed>
        </object>
      </div></div>

    <div class="paragraph" style="text-align:center;">SPACE MR膝关节检查，使用3D数据集进行多平面可交互的重建</div></div>

**高级讨论**

*SPACE/CUBE/VISTA技术的补充解释*

虽然回聚脉冲一般是非选择性的，激发脉冲可以是非选择性地也可以是层面选择性的。

有时候会一起使用部分信号平均与相位循环减少伪影。为了减少测量时间，可能会使用不均匀数目的信号平均，换句话说，仅针对k空间中心部分的线进行平均。

图像对比度与标准FSE/TSE序列中并不完全一致，总体而言，有效回波时间（TEeff）需设置为比标准FSE的长20%才能获得相同水平的T2加权。

SPACE/CUBE/VISTA与很多协议都有兼容性，包括T1，T2，PD，T1-FLAIR，T2-FLAIR，双IR和相位校正的IR技术。

**参考材料** 
    * Busse R. `3D FSE reduces scan time, generates thinner slices <http://mriquestions.com/uploads/3/4/5/7/34572113/gehealthcare-signapulse-magazine-3d-fse-reduces-scan-time-generate-thinner-slices-20071001.pdf>`_. Signa Pulse, A GE Healthcare MR Publication, Autumn, 2007, pp 34-5. 
    * Kitajima M, Hirai T, Shigematsu Y et al. `Comparison of 3D FLAIR, 2D FLAIR, and 2D T2-weighted MR imaging of brain stem anatomy <http://mriquestions.com/uploads/3/4/5/7/34572113/vista_ajnr.a2874.full.pdf>`_. AJNR Am J Neuroradiol 2012; 33:922-927.
    * Mugler JP III. `Optimized three-dimensional fast-spin-echo MRI <http://mriquestions.com/uploads/3/4/5/7/34572113/mugler-2014-journal_of_magnetic_resonance_imaging.pdf>`_. J Magn Reson Imaging 2014; 39:745-767.

**相关问题**
	* `什么是快速自旋回波成像？ <http://chunshan.github.io/MRI-QA/rapid-imaging/what-is-fsetse.html>`_