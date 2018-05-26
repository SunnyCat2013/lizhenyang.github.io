# Logistic 函数
Logistic 函数是一组函数集合，公式如下：
$$
f(x) = \frac{L}{1 + e^{-k(x - x_0)}}
$$
```
- e = 自然对数的底
- x_0 = x 值的中点
- L = 曲线的最大值
- k = 曲线的曲率
```


# sigmoid function
Sigmoid function 是一个数学函数，数学曲线是 "S" 型，或者说是 sigmoid 弯曲。
通常情况下 sigmoid 函数被认为是 logistic 函数的一个特例。
当 k = 1, L = 1, x_0 = 0 时，logistic 函数就是一个 sigmoid 函数。
## 属性
满足下面属性的函数都可以认为是 sigmoid 函数。

- 有界
- 可导
- 单调
- 一阶导数非负，且为钟形
- 水平渐近线 

# 例子
- Logistic function
$$
f(x) = \frac{1}{1 + e^{-x}}
$$

- hyperbolic tangent(平移、缩放之后的 logistic function)
$$
f(x) = \tanh x = \frac{e^x - e^{-x}}{e^x + e^{-x}} = \frac{e^x + e^{-x} - 2e^{-x}}{e^x + e^{-x}} = 1 - \frac{2e^{-x}}{e^x + e^{-x}} = 1 - \frac{2}{e^{-(-2)(x - 0)} + 1}
$$







# Reference
https://en.wikipedia.org/wiki/Sigmoid_function
https://en.wikipedia.org/wiki/Logistic_function
