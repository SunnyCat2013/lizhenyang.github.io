# boosting 和 bagging 都是 ensemble 的一种
参考： https://quantdare.com/what-is-the-difference-between-bagging-and-boosting/

boosting 和 bagging 都是集成学习(ensemble learning)中的一种技术。
它们都是把一些弱分类器组合到一起，形成一个新的强分类器。

# Bagging 和 Boosting 的区别

Bagging 和 Boosting 都是集成学习(ensemble methods)中的一种方法。但是它们的各自的特点是什么呢？
 
Bagging 和 Boosting 都是集成学习的技术。这种技术将多个弱分类器组合成一个强分类器，进行将性能提高。


# 什么是集成学习方法（ensemble method)?
集成，是机器学习里面的一种方法，在这种方法里使用一种学习方法可以训练多个模型。
集成学习使用一组（成千上万）的学习模型，朝着一个目的进行优化。

第二种多分类器包含一种混合方法，它们使用多种不同学习方法进行优化。比较知名的就是 Stacking。


> 也就是 用一种方法优化多个分类器是 ensemble ，使用多种方法优化多个分类器是 stacking？

在模型的学习过程中，主要的问题是噪声、样本采样偏差以及样本分布的偏差。集成学习的方法旨在降低这些因素的影响。集成学习是为了提高最终模型的稳定性和准确率。
组合起来的多分类器，尤其是对于不稳定的分类器，会更稳定一些。

无论是使用 Bagging 还是 Boosting 都需要选择一个基础的学习算法。
例如，如果我们以决策为基础算法，Bagging 和 Boosting 都可以用尽可能多的单个树分类器。

![single-bagging-boosting](https://quantdare.com/wp-content/uploads/2016/04/bb1.png)
