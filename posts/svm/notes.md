# 学习支持向量机
下面，我打算依照 [SVM Tutorial](https://www.svm-tutorial.com/2017/02/svms-overview-support-vector-machines/) 的结构学习一下支持向量机。

1. 支持向量机的目标
2. 如何计算间隔
3. 无约束条件的最小解
4. 凸优化函数
5. 拉格朗日对偶问题

# 参考
https://www.svm-tutorial.com/2017/02/svms-overview-support-vector-machines/

## The margin
1. 支持向量机的目标是找分隔平面
 - 支持向量机是什么
 - 支持向量的作用是什么
 - 什么时分隔平面
 - 如何找最优超平面 
 

2. 分隔平面要在训练数据上表面良好，同时要有良好的泛化能力

## Calculate the margine

1. 向量运算
 - 向量的方向和模
 - 加减
 - 点乘
 - 映射

2. 计算 margine
 - 超平面公式
 - 计算 间隔

3. dot product 定义了 \theta 和 (x_1，y_1)，(x_2, y_2) 之间的关系
这样在知道两个向量的定义的时候，就能算出来它们之间的夹角
$$
a \dot b = ||a|| \dot ||b|| \cos \theta = x_1 * x_2 + y_1 * y_2
$$

4. 最后把点到直线的距离变成直线法向量和点的向量之间的关系。
