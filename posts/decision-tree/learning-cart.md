# 学习 Decision Tree(Classification and Regression Tree)
https://machinelearningmastery.com/classification-and-regression-trees-for-machine-learning/

> Classically, this algorithm is referred to as “decision trees”, but on some platforms like R they are referred to by the more modern term CART.

原来 DT 和 CART 是一个概念啊。
也就是说，我们平时说的决策树，既可以做分类，也可以做回归。

> The CART algorithm provides a foundation for important algorithms like bagged decision trees, random forest and boosted decision trees.

CART 是很多重要的机器学习方法的基石，如，bagged decision trees，random forest 和 boosted decision trees。
那么 bagged trees 和 random forest 分别是什么，它两有什么区别？

> This is a numerical procedure where all the values are lined up and different split points are tried and tested using a cost function. The split with the best cost (lowest cost because we minimize cost) is selected.

选择一个特征，找到这个特征的分界点。
使用一个 cost function ，根据损失最小的原则到分界点。

## 回归预测模型的 cost function

> For regression predictive modeling problems the cost function that is minimized to choose split points is the sum squared error across all training samples that fall within the rectangle:

$$
Regression Cost Function = \sum^{2}_{i = 1}(y_i - prediction_i)^2
$$

使用 square error 最小的点作为分界点。这里的 prediction ，我理解是划分之后的均值。

> Where y is the output for the training sample and prediction is the predicted output for the rectangle.

prediction 是输出区间的输出值。

## 分类模型 cost function: Gini Index

> For classification the Gini index function is used which provides an indication of how “pure” the leaf nodes are (how mixed the training data assigned to each node is).

$$
G = \sum^{n}_{k = 1} p_k * (1 - p_k)
$$

Gini Index 是变了判断一个划分里面的分类结果的混乱程度。
其中，$p_k$ 指在一个划分里面，类别为 k 的样本点占所有样本点的比率。
如在二分类中，如果全部分成同一类则 $G==0$，如果是均分的话就是 $G==\frac{1}{2}$。
> G 越大，说明分类越混乱，我们认为划分的越不好。或者说划分作用越差。反之，则说明划分越好。




 
