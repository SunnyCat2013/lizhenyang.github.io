# Questions
1. biase 是在设置初始参数的时候造成的吧，如果初始参数设置的好，就不应该存在这个问题了。
2. 过拟合的时候，有几种方法
3. 导致过拟合的原因有哪些

# 结构
1. 讨论 bias 与 variance 的时候，模型的复杂度是变化的

2. 讨论 正则项 的时候，模型一定要足够复杂（达到过拟合的程度），这时候 lambda 是变化的。

3. 讨论样本集的大小对模型的影响的时候，模型是固定的。

# Diagnosing Bias vs. Variance

![biase-variance](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/I4dRkz_pEeeHpAqQsW8qwg_bed7efdd48c13e8f75624c817fb39684_fixed.png?expiry=1539388800000&hmac=aA-IallqzlEMDqBNyK0UfiWsx1fR-9WIsNtuGGrdR1Y)

通过上图，我们可以看出两个规律：

1. 随着模型复杂度的增大（d 变大，参数变多），模型在训练集上的损失变小。这是因为模型变复杂了，对训练数据的拟合效果越来越好。

2. 验证集的损失，随着 d 变大，先下降，此时是因为模型复杂度提升从训练数据中学习到更多信息；后下降，是因为模型向训练集靠拢，学习出来的模型泛化能力变弱。

## Underfitting(high bias)
模型初始化造成的误差。此时只需要加入数据，就可以提升模型精度。

## Overfitting(high variance)
模型过多描述训练数据。
此时模型的表现，在训练集中，效果较好。而在验证集中损失越来越大。

# Regularization and Bias/Variance
如果正则项系数 $\lambda$ 作用不明显，说明模型欠拟合。
当模型过拟合的时候：

![regularization](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/3XyCytntEeataRJ74fuL6g_3b6c06d065d24e0bf8d557e59027e87a_Screenshot-2017-01-13-16.09.36.png?expiry=1539388800000&hmac=-LAbFGmqyfZIZb8Z5j1V8-8TY6ehceIdb5ZmHE_sg1o)

1. lambda 过大，对参数惩罚过大，使模型的复杂度不能完全展现，造成欠拟合。
2. lambda 适度，拟合效果比较理想。
3. lambda 较小，对参数惩罚较小，模型复杂度体现，造成过拟合。


# Learning Curves
## Experience high bias
我对这个 high bias 的理解是，模型复杂程度不足，使初始 参数 在数据的不断注入下接近当前最优。
此时模型已经到达自己的极限，再多投入数据，也不到学习出更多信息。
![high-bias](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/bpAOvt9uEeaQlg5FcsXQDA_ecad653e01ee824b231ff8b5df7208d9_2-am.png?expiry=1539388800000&hmac=wjkumFulg4vuZcf3UAK7jgAKJSRk0pTMBJAzUwdv1wE)


## Experiencing high variance
当模型足够复杂的时候，多加入一些数据，使模型能够再优化一些。

![high-variance](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/vqlG7t9uEeaizBK307J26A_3e3e9f42b5e3ce9e3466a0416c4368ee_ITu3antfEeam4BLcQYZr8Q_37fe6be97e7b0740d1871ba99d4c2ed9_300px-Learning1.png?expiry=1539388800000&hmac=g9z14eSTayikqkZmDGxRqrS0g3KyAqBDK1xspHb3nZo)

# 参考
https://www.coursera.org/learn/machine-learning/supplement/81vp0/diagnosing-bias-vs-variance
https://www.cnblogs.com/ooon/p/5711516.html
