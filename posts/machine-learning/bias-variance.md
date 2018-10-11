# Questions
1. biase 是在设置初始参数的时候造成的吧，如果初始参数设置的好，就不应该存在这个问题了。
2. 过拟合的时候，有几种方法
3. 导致过拟合的原因有哪些

# 结构

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




# 参考
https://www.coursera.org/learn/machine-learning/supplement/81vp0/diagnosing-bias-vs-variance
https://www.cnblogs.com/ooon/p/5711516.html
