1. Logistic Regression(LR)
LR和Linear SVM本质不同来自于loss function不同
支持向量机​基于几何间隔最大化原理，认为存在最大几何间隔的分类面为最优分类面所以SVM只考虑分类面上的点，而LR考虑所有点，SVM中，在支持向量之外添加减少任何点都对结果没有影响，而LR则是每一个点都会影响决策。
Logistic Regression https://zhuanlan.zhihu.com/p/74874291

2. Xgboost 

3. Least square method最小二乘法
残差平方和，即SSE（Sum of Squares for Error）
[线性回归(Linear Regression)](https://zhuanlan.zhihu.com/p/66519299)是利用称为线性回归方程的最小平方函数（least squares method）对一个或多个自变量（independent variable）和因变量（dependent variable）之间关系进行建模的一种回归分析。这种函数是一个或多个称为回归系数的模型参数的线性组合。只有一个自变量的情况称为简单回归,大于一个自变量情况的叫做多元回归。

3. [SVM](https://zhuanlan.zhihu.com/p/43827793) 是一种二类分类模型。它的基本模型是在特征空间中寻找间隔最大化的分离超平面的线性分类器。
- 当训练样本线性可分时，通过硬间隔最大化，学习一个线性分类器，即线性可分支持向量机；
- 当训练数据近似线性可分时，引入松弛变量，通过软间隔最大化，学习一个线性分类器，即线性支持向量机；
- 当训练数据线性不可分时，通过使用核技巧及软间隔最大化，学习非线性支持向量机。
- 以上各种情况下的数学推到应当掌握，硬间隔最大化（几何间隔）、学习的对偶问题、软间隔最大化（引入松弛变量）、非线性支持向量机（核技巧）。

4. [正则化](https://zhuanlan.zhihu.com/p/376282535)
a、欠拟合：偏差过大，做特征工程、减小(弱)正则化系数；
b、过拟合：方差过大，可增加样本、减少特征、增加(强)正则化系数；
[回归模型偏差&方差&残差](https://zhuanlan.zhihu.com/p/50214504)

5. [神经网络各层作用](https://zhuanlan.zhihu.com/p/49907831) receptive field 感受野

6. [Resnet结构与功能]https://zhuanlan.zhihu.com/p/31852747

7. [YOLO](https://zhuanlan.zhihu.com/p/32525231) Non maximum suppression


## Sensetime Interview
1. principle of back-propagation algorithm
BP算法的学习过程由正向传播过程和反向传播过程组成。在正向传播过程中，输入信息通过逐层处理并传向输出层。如果在输出层得不到期望的输出值，则通过构造输出值与真实值的损失函数作为目标函数，转入反向传播，逐层求出目标函数对各神经元权值的偏导数，构成目标函数对权值向量的梯度，作为修改权值的依据，网络的学习在权值修改过程中完成。输出值与真实值的误差达到所期望值时，网络学习结束。
2. object detection algorithm, transformer mechanism
[传统+深度 目标检测](https://blog.51cto.com/u_15274944/2924095)
[Transformer](https://zhuanlan.zhihu.com/p/82312421)中抛弃了传统的CNN和RNN，整个网络结构完全是由Attention机制组成。更准确地讲，Transformer由且仅由self-Attenion和Feed Forward Neural Network组成。一个基于Transformer的可训练的神经网络可以通过堆叠Transformer的形式进行搭建。
3. How to find the shortest path given loss function



## batchnorm, ResNet and Faster R-CNN
[Batchnorm](https://zhuanlan.zhihu.com/p/34879333)
BN使得网络中每层输入数据的分布相对稳定，加速模型学习速度
BN使得模型对网络中的参数不那么敏感，简化调参过程，使得网络学习更加稳定
BN允许网络使用饱和性激活函数（例如sigmoid，tanh等），缓解梯度消失问题
BN具有一定的正则化效果


## R-CNN
[R-CNN, fast R-CNN, faster R-CNN](https://zhuanlan.zhihu.com/p/55856134)
这个网络也是目标检测的鼻祖了。其原理非常简单，主要通过提取多个Region Proposal(候选区域)来判断位置，作者认为以往的对每个滑动窗口进行检测算法是一种浪费资源的方式。在RCNN中，不再对所有的滑动窗口跑算法，而是只选择一些窗口，在少数窗口上运行CNN。
1. 输入图像
2. 利用selective search对图像生成1K~2K的候选区域（region proposal），这个量比传统的算法要少得多。具体一点，选出region proposal的方法是运行图像分割算法，对于分割算法跑出来的块，把它作为可能的region proposal输出。
3. 提取特征：将region proposal resize为统一大小，送进去掉了softmax的CNN，对每个候region proposal提取特征
对区域进行分类：对从CNN output出来的特征向量送进每一类的SVM分类, 如果十个类别，那么每个region proposal要跑10个SVM，得到类别。这里为什么要用SVM而不是softmax，一种说法是解决样本不均衡的问题，另外是早期神经网络还不如现在这样发达，当时SVM还是比较领先的分类器。
4. 修正：对CNN output的特征向量（这个特征向量和第4步中拿去喂给SVM的是一个向量）做回归（左上角右下角的四个坐标），修正region proposal的位置。
RCNN问题：
- 计算量是非常大的，要对每个候选区域都进行特征计算。
- 冗余计算太多，候选区域高度重叠。
- 不是端到端的训练，麻烦。
- 内存占用：需要储存多个SVM分类器和bounding box 回归器.
- 对输入图片的大小有硬性要求.

## Fast R-CNN
流程：
1. 将任意size的图片输入CNN，得到特征图。在RCNN中，先生成region proposals再做卷积，相当于做了多次卷积，浪费时间。对原始图片使用selective search算法得到约2k region proposals（相当于RCNN的第一步）
2. 在特征图中找到每一个region proposals对应的特征框。在ROI池化层中将每个特征框池化到统一大小
统一大小的特征框经过全连接层得到固定大小的特征向量，分别进行softmax分类（使用softmax代替了RCNN里面的多个SVM分类器）和bbox回归。
Fast R-CNN组合了classification和regression, 做成single Network，实现了端到端的训练，实际上它相对RCNN最大的改进是抛弃了多个SVM分类器和bounding box回归器的做法，一起输出bbox和label, 很大程度上提升了原始RCNN的速度。

## Faster R-CNN
在Fast RCNN的基础上，Faster RCNN在性能上又有了进步。Faster RCNN将特征抽取(feature extraction)，proposal提取，bounding box regression，classification都整合在了一个网络中，使得综合性能有较大提高，在检测速度方面尤为明显。对比起Fast-RCNN，最重要的是使用RPN来代替原来使用分割算法生成候选框的方式，极大的提升了检测框生成速度。总地来说，Faster RCNN对Fast RCNN的改进点在于获得region proposals的速度要快很多。
1. 提取特征：输入固定大小的图片，进过卷积层提取特征图feature maps
2. 生成region proposals: 然后经过Region Proposal Networks(RPN)生成region proposals。该层通过softmax判断anchors属于foreground或者background，再利用bounding box 回归修正anchors获得精确的proposals（候选区域）。
3. ROI Pooling: 该层的输入是feature maps和proposals，综合这些信息后提取proposal feature maps
4. Classification: 将Roi pooling生成的proposal feature maps分别传入softmax分类和bounding box regression获得检测物体类别和检测框最终的精确位置。

## Coding & Technical
Coding: 2d Conv, recursion. 
Technical: denoising filter, noise, SVM, HDR, Gaussian filter.

## Gaussian filter：
高斯滤波器是一种线性滤波器，能够有效的抑制噪声，平滑图像。其作用原理和均值滤波器类似，都是取滤波器窗口内的像素的均值作为输出。其窗口模板的系数和均值滤波器不同，均值滤波器的模板系数都是相同的为1；而高斯滤波器的模板系数，则随着距离模板中心的增大而系数减小。所以，高斯滤波器相比于均值滤波器对图像个模糊程度较小。
HDR(High Dynamic Range)是用来实现比普通数位图像技术更大曝光动态范围（即更大的明暗差别）的一组技术。高动态范围成像的目的就是要正确地表示真实世界中从太阳光直射到最暗的阴影这样大的范围亮度。

[purpose of drop-out](https://zhuanlan.zhihu.com/p/38200980)



