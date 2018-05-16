# 学习 xgboost
> 久闻 xgboost 大名，一直没有去了解。最近工作要用到，我打算了解一下。现在我对它没有任何概念。。


# 疑问
- 分类树、回归树分别是什么，有什么区别

# References
https://machinelearningmastery.com/gentle-introduction-xgboost-applied-machine-learning/
https://www.cnblogs.com/ModifyRong/p/7744987.html
https://cloud.tencent.com/developer/article/1005611
https://www.cnblogs.com/pinard/p/6140514.html

https://xgboost.readthedocs.io/en/latest/model.html
# https://homes.cs.washington.edu/~tqchen/pdf/BoostedTree.pdf
model: 给定 x 输出 y 的数学函数。
Objective function: model 确定，评价参数性能的函数。
    - Training loss
    - Regularization

- classification and regression trees (CART)
simple and predictive: The tradeoff between the two is also referred as bias-variance tradeoff in machine learning.

## So-called tree esamable model
What is actually used is the so-called tree ensemble model, which sums the prediction of multiple trees together.
![](https://raw.githubusercontent.com/dmlc/web-data/master/xgboost/model/twocart.png)

## what is the model for random forests?
It is exactly tree ensembles! 

## questions
- For example, you should be able to describe the differences and commonalities between boosted trees and random forests.



# gbdt
在 https://blog.csdn.net/w28971023/article/details/8240756 文章里面，提到
> 残差向量(-1, 1, -1, 1)都是它的全局最优方向

这个确实之前没有想到过。
这样理解的话，每个树，都是在原有树（或者一个组合的基础上）再优化（指向最优方向），而不是每个树都在做相同的优化，做重复的工作。这样貌似可以每个树有一个专一的优化方向，而不用每个树都胡子眉毛一把抓。。。


# 番外
![decision tree]('./dt-pro-con.md')
缺点是，它只能按照坐标轴划分，不能有斜线，不能有曲线。
如果要实现相同的斜线或者曲线，需要非常复杂的划分。看上图。

# kaggle 中学习 xgboost
https://www.kaggle.com/dansbecker/learning-to-use-xgboost/code
