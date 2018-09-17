# Advice for Applying Machine Learning
- improving its performance
- machine learning system design

- machine learning diagnostic

# Evaluating Your Hypothesis
为什么说只分为 test/train 的时候，test 多了一个参数呢？
是因为，theta 维度不一样的时候，模型就不一样。
我们选择 使用 test 效果最好的 theta 的维度。这种 theta 维度的选择本身就是一种偏向 test 的过拟合。

所以我们把数据分成 train/cross validation/test

使用 train 训练，使用 cross validation 选择模型（theta 的维度），用 test 作为模型的评估。


# Bias vs. Variance

https://www.coursera.org/learn/machine-learning/supplement/81vp0/diagnosing-bias-vs-variance

variance: 这个还比较好理解的，因为多项式的最高次幂越高，模型越复杂越容易过拟合呗。如果 training 损失较小，而 validation 损失较大，说明过拟合。
bias: variance 比较小的时候，training and validation data set 的损失都比较大。这个时候 bias 影响较大，说明 欠拟合（underfit）

具体的可以看这个课：https://www.coursera.org/learn/machine-learning/lecture/yCAup/diagnosing-bias-vs-variance

[biase-variance](./bias-variance.png)


# 选择 lambda 时 validation set and test set 的作用。
- 使用 validation set 选出最优的 lambda 值
- 使用选出的 lambda 在 test set 上测试，在 test set 得到的损失值更能说明 当前 lambda 的泛化能力。

在 validation set 上选出 lambda 的过程中，已经加入了人工筛选（在一组数据中选出最优的），不能代表该 lambda 的泛化能力（在未知数据上的表现）。


