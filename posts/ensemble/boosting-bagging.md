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

# Bagging 和 Boosting 的区别
Bagging 和 Boosting 的区别在于数据训练过程中如何增加数据。
每次采样的时候有 N 个新数据在样本集中抽取出来。同时，由于每次抽取的时候，旧样本都被放回样本池中，所以下次抽取的数据有可能在之前出现过。

采样过程中：
- Bagging 每次采样的时候，所有样本的权重一直不变。在训练过程中，不同的分类器可以同时进行训练。

- Boosting 每次采样的过程中，当前样本的权重由之前的分类情况决定。所以，Boosting 的分类器需要等待之前的分类器训练结束。它的训练过程是串行的。
Boosting 每次训练的过程中，之前被误分类的样本，会被提高权重。这样，新的分类器将会把“注意力”放在这些不太好分类的样本上。

![how-to-get-learners](https://quantdare.com/wp-content/uploads/2016/04/bb2.png)
因为 Bagging 和 Boosting 用的相同的基础学习器，而每次的训练样本有所区别，所以最终得到的分类器会有所不同。
![parallel-sequential](https://quantdare.com/wp-content/uploads/2016/04/bb3.png)

# 预测过程是怎么工作的呢？
How does the classification stage work?
- Bagging 把每个子分类器的输出结果取个均值就得到了最终的输出结果。
- Boosting 在做分类的时候，又出现了一个新的权重，每个分类器获得一个权重。所有分类器和权重结合得到最终分类结果。
好的分类器会被分得更大的权重，所以在评估新的分类器时，需要对比旧的分类器。

一个 Boosting 技术对单个分类器进行选择。如，AdaBoost 中如果一个错误率大于 50% 的分类器就会被丢掉。然后进行重复迭代获得一个新的合格（错误率比随机猜要低）的分类器。


![prediction](https://quantdare.com/wp-content/uploads/2016/04/bb4.png)
