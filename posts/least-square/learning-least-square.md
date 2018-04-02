# 最小二乘法（Least Square）学习笔记
> 在工作中，构造了一个算法用到了最小二乘法，现在花点时间来全面了解一下。

# 简介
最小二乘法(下面简称 LS)是用来寻找数据的最优拟合曲线的方法。
最基本的问题是给定数据 $$(x_n, y_n), n \in {1, \cdots, N}$$ 寻找最优直线 $$y = ax + b$$。
LS 很容易就可以做如下推广：
$$
y = a_1 f_{1}(x) + \cdots + c_{K}f_{K}(x);
$$
*注意：*$$f_K$$ 未必是 x 的线性函数。
y 是所有这些 $$f_K$$ 的线性组合。

# 参考
[The Method of Least Squares](https://web.williams.edu/Mathematics/sjmiller/public_html/BrownClasses/162/Handouts/MethodLeastSquares.pdf)
