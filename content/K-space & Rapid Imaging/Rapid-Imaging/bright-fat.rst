Question-FSE中明亮的脂肪：为什么脂肪在快速自旋回波序列的图像中是明亮的？
======================================================================================================================

:date: 2014-10-27
:tags: K-space & Rapid Imaging, Rapid Imaging(FSE&EPI)
:slug: bright-fat
:authors: Chunshan
:summary: 为什么脂肪在快速自旋回波序列的图像中是明亮的

原文链接:\ `Why is fat bright on fast spin echo images? <http://www.mri-q.com/bright-fat.html>`_

**概要** 
 .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/8177119_orig.png?303
    :alt: summary
    :align: center
    :width: 700

.. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/2899238_orig.jpg
   :alt: Conventional spin-echo image (left) and fast spin-echo image (right)
   :align: right
   :width: 600

   传统自旋回波图像（左）和快速自选回波图像（右），TR/TE(eff)都是3000/80。注意到FSE上头皮脂肪信号更亮。

二十世纪九十年代当快速自旋回波（FSE， Fast Spin-Echo）序列技术首次投入使用时，与传统自旋回波（CSE， Conventional Spin-Echo）技术相比最显著的不同是FSE图像中可见“异常”明亮的脂肪信号。这种现象如右图所示。

虽然有几个因素都会导致FSE上的“明亮脂肪”现象，占主导地位的机制一般认为是继发于J偶联相互作用瓦解后的T2延长，此现象通常发生在相邻脂肪质子之间。

我知道这个声明需要一些更进一步的背景和解释，所以请看一下下面的讨论！

组织中的脂肪主要以长链甘油三酯的形式存在，每个甘油三酯分子中含有1打不同类型的¹H原子分布于不同化学环境中，这些长链中相邻的原子核通常会通过它们之间电子云的扭曲而相互作用，这个过程称为J偶联。

+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/6229716_orig.png        | .. figure:: http://www.mri-q.com/uploads/3/4/5/7/34572113/2663607_orig.gif?206     |
|    :alt: Structure of a typical triglyceride                                      |    :alt: J-coupling interaction between neighboring protons                        |
|    :width: 400                                                                    |    :width: 400                                                                     |
|                                                                                   |                                                                                    |
|    典型的甘油三酯（脂肪）分子的结构                                               |    相邻质子之间的J偶联相互作用是一种量子衍生效应，由电子云的扭曲介导。             |
+-----------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

J偶联相互作用的强度用因子J进行量化，J表示脂肪中不同质子的谐振频率偏移，值在6-8Hz的范围内。这种小的频率偏移意味着脂肪中不同的质子以稍微不同的频率进动。它们的信号彼此之间以循环的方式不断进行建设性和破坏性的干涉（这类似于更熟悉的水-脂肪化学位移干涉，在此单独的Q&A中有描述，不同的是这儿仅涉及脂肪中的质子而且与场强无关）。第一个失相位的干涉发生在TE=1/2J处，大约60-80ms。

需要指出的是TE为60-80ms在常规自旋回波成像中通常用于产生T2加权像。选择此范围中的TE，由于J偶联效应的影响，记录的脂肪信号实际会低一些，看起来像是选择了更短或更长TE的结果。

某种意义上应该说，T2加权的常规自旋回波成像中的脂肪异常暗，而不是快速自选回波成像中的脂肪异常亮。

FSE成像中，发生在回波间隔处的多个180°脉冲在10ms的量级，打破了J偶联失相位的模式，虽然J偶联造成的相位偏移不会被180°脉冲回聚。完全理解这一过程需要了解量子力学的知识，远远超出了本网站的范围。然而，这个过程可以从如下角度理解，多个180°脉冲施加的间隔如果比1/J短，会使得所有的J偶联自旋化学上“等效”，导致结果信号不再受偶联调制。因此，FSE成像上的脂肪看起来比CSE图像上的脂肪更亮。

**高级讨论**

虽然大多数专家认为J偶联机制瓦解是造成明亮脂肪信号的首要原因，其他因素可能也很重要。Henkelman等曾指出自旋在局部磁场敏感性不同的区域（水和脂肪）弥散时，紧密间隔的RF脉冲减少了弥散导致的失相。由多个RF脉冲导致的受激回波也会在明亮脂肪效应中占约10%的作用。Mulkern等也指出脂肪信号相对增加的程度具有场依赖性，1.5T时比更高或更低场强时更加突出。因为J偶联是不依赖于场强的，这意味着存在其他与场强相关的机制。

但其实任何情况下，我都怀疑这个问题对现代的MR用户而言是否仍然是个问题。FSE成像已经在MRI的各个方面很大程度上取代CSE。FSE图像上的脂肪不再看起来“异常”亮，因为FSE已经成为“新常态”。可能这个讨论现在更多是对MRI历史上的兴趣。但FSE上脂肪明亮的现象却可以解释我们为什么通常在T2加权像上要进行脂肪抑制，而在“旧时代”CSE的T2加权像一般不进行脂肪抑制。

**参考材料** 
     * Henkelman RM, Hardy PA, Bishop JE, Poon CS, Plewes DB. `Why fat is bright in RARE and fast spin-echo imaging <http://www.mri-q.com/uploads/3/4/5/7/34572113/why_fat_is_bright_on_fse.pdf>`_. J Magn Reson Imaging 1992; 2: 533-540.
     * Mulkern RV, Packard AB, Gambarota G. `Field dependence of the bright fat effect in fast spin echo imaging: theory and experiment <http://www.mri-q.com/uploads/3/4/5/7/34572113/mulkern_fse_1107.pdf>`_. Proc Intl Soc Mag Reson Med 2003; 11:1107.
     * Stables LA, Kennan RP, Anderson AW, Gore JC. `Density matrix simulations of the effects of J coupling in spin echo and fast spin echo imaging <http://www.mri-q.com/uploads/3/4/5/7/34572113/stabler_density_matrix1-s2.0-s109078079891655x-main.pdf>`_. J Magn Reson 1999;140:305-314.
     * Stokes AM, Feng Y, Mitropoulos T, Warren WS. `Enhanced refocusing of fat signals using optimized multipulse echo sequences <http://www.mri-q.com/uploads/3/4/5/7/34572113/stokes_fat_jcouple_mrm24340.pdf>`_. Magn Reson Med 2013;69;1044-55.

**相关问题**
	* `什么是快速自旋回波成像？ <http://chunshan.github.io/MRI-QA/rapid-imaging/what-is-fsetse.html>`_