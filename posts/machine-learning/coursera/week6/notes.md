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
