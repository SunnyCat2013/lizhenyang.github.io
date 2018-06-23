# Gradient Boosting Decision Tree
Boosting 大体过程：

1. 原始输入生成一级预测结果 F(x_1) -> P_1
2. 计算残差（Residual）R(x_1) = label - P_1
3. 使用残差作为第二个模型的回归值，训练出回归模型 F_2(x_1) = P_2
4. 联合两次模型的输出结果 P_2' = P_1 + P_2
5. 计算残差

通过这个大致过程，我们可以看出没有一个地方说，我们一定要使用树模型。
难怪别人都说这个 GBDT 是对残差的优化。

> This is one of the broader concepts and advantages to gradient boosting. It’s really just a framework for iteratively improving any weak learner. So in theory, a well coded gradient boosting module would allow you to “plug in” various classes of weak learners at your disposal.

理论上，这种可以把任意类型的弱分类器集合成一个强分类器。
> 所以 gbdt 一定是回归树？

# References
http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/
