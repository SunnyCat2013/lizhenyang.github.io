# Gradient Boosting Decision Tree
Boosting 大体过程：

1. 原始输入生成一级预测结果 F(x_1) -> P_1
2. 计算残差（Residual）R(x_1) = label - P_1
3. 使用残差作为第二个模型的回归值，训练出回归模型 F_2(x_1) = P_2
4. 联合两次模型的输出结果 P_2' = P_1 + P_2

# References
http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/
