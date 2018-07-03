# 学习 Decision Tree\(Classification and Regression Tree\)

[https://machinelearningmastery.com/classification-and-regression-trees-for-machine-learning/](https://machinelearningmastery.com/classification-and-regression-trees-for-machine-learning/)

# 问题

1. 整体的损失函数是怎么反射求导传播的？还是说，分裂求划分的时候已经完成了次优的求解过程？

> Classically, this algorithm is referred to as “decision trees”, but on some platforms like R they are referred to by the more modern term CART.

原来 DT 和 CART 是一个概念啊。  
也就是说，我们平时说的决策树，既可以做分类，也可以做回归。

> The CART algorithm provides a foundation for important algorithms like bagged decision trees, random forest and boosted decision trees.

CART 是很多重要的机器学习方法的基石，如，bagged decision trees，random forest 和 boosted decision trees。  
那么 bagged trees 和 random forest 分别是什么，它两有什么区别？

> This is a numerical procedure where all the values are lined up and different split points are tried and tested using a cost function. The split with the best cost \(lowest cost because we minimize cost\) is selected.

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

> For classification the Gini index function is used which provides an indication of how “pure” the leaf nodes are \(how mixed the training data assigned to each node is\).


$$
G = \sum^{n}_{k = 1} p_k * (1 - p_k)
$$


Gini Index 是变了判断一个划分里面的分类结果的混乱程度。  
其中，$p\_k$ 指在一个划分里面，类别为 k 的样本点占所有样本点的比率。  
如在二分类中，如果全部分成同一类则 $G==0$，如果是均分的话就是 $G==\frac{1}{2}$。

> G 越大，说明分类越混乱，我们认为划分的越不好。或者说划分作用越差。反之，则说明划分越好。

Gini Index 可能会出现一个划分（Group）中样本比较少，但是比较乱，而生成得分较高。  
比如只有两个样本，这样就是 0.5 。另外一个划分样本比较多，但是相对没胡那么乱，得到就较低。  
把这两个划分用同样的权重进行考虑是不合理的。

## Gini Score


$$
G = \sum^{n}_{i = 1}\{[\sum^{n}_{k = 1} p_k * (1 - p_k)] * \frac{SumOfInstancesInThisGroup_i}{SumOfAllInstances}\}
$$


与 Gini Index 相比，Gini Score 更好地考虑了不同划分中样本个数的权重。

# Stop Criterion 停止分裂的标准。

如果，我们把训练数据里面的每个点都细分到叶子结点中，那么我们的模型就对训练数据过于拟合。  
在这种情况下，得到的模型在测试集中就可能没有太好的表现性能。

所以我们需要一个判断什么时候停止细分的条件。  
比较常见的方法是限制一个样本个数的值，如果一个划分中的值小于阈值，则该结点就成为叶子结点不再细分。

> The stopping criterion is important as it strongly influences the performance of your tree. You can use pruning after learning your tree to further lift performance.

影响决策树的两个非常重要的条件：  
1. 停止分裂条件。这个条件一视同仁地给出了停止分裂的条件，该方法不对当前划分里面的数据进行判断，只判断样本数量。  
2. 剪枝方法。这个对当前划分及相关子划分的数据进行计算，减少树的分支。

# Pruning The Tree

决策树的复杂度可以用决策树的分裂结点数表示。  
一般来讲，复杂度低的决策树更好一些。  
它更易解释，更不易过拟合。

> The fastest and simplest pruning method is to work through each leaf node in the tree and evaluate the effect of removing it using a hold-out test set. Leaf nodes are removed only if it results in a drop in the overall cost function on the entire test set. You stop removing nodes when no further improvements can be made.

剪枝的方法属于控制变量法：剪掉一个叶子结点，如果模型的整体损失下降，那么就应该剪去这个结点。就这样一直剪下去，直到没有效果的提升为止。

# 总结

1. 决策树的传统名字是 Decision Tree，现代一点的名字是 Classification And Regression Trees \(CART\)。
2. CART 使用二叉树表示。
3. 给定一个输入之后，CART 模型通过遍历二叉树分支进行预测。
4. 树模型的生成，使用的是贪心算法寻找每次划分的分割点。
5. 停止条件决定是模型的学习力度，剪枝提高了模型性能（适应性）。



