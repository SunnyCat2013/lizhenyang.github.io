# 第二周
编程作业的收获：
1. 使用 octave 写 cost function。体会了一下矩阵运算带来的便利。

$$
J(\theta) = \frac{1}{2m} \sum_{i = 1}^{m}(h_\theta(x_i) - y_i)^2
$$

2. 学习了使用梯度下降和 normal equations 两种方法求线性回归参数的方法。
通过这周的学习，我有点理解梯度下降的样子。
梯度下降与 normal equations 相比，计算量可能会小一些（在数据量非常大的时候）。
同时也避免了 normal equations 矩阵不可逆时的计算困难。
