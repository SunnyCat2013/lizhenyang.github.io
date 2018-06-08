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

The second group of multiclassifiers contain the hybrid methods. They use a set of learners too, but they can be trained using different learning techniques. Stacking is the most well-known. If you want to learn more about Stacking, you can read my previous post, “Dream team combining classifiers“.

第二种多分类器包含一种混合方法，它们使用多种不同学习方法进行优化。比较知名的就是 Stacking。


> 也就是 用一种方法优化多个分类器是 ensemble ，使用多种方法优化多个分类器是 stacking？

The main causes of error in learning are due to noise, bias and variance. Ensemble helps to minimize these factors. These methods are designed to improve the stability and the accuracy of Machine Learning algorithms. Combinations of multiple classifiers decrease variance, especially in the case of unstable classifiers, and may produce a more reliable classification than a single classifier.

To use Bagging or Boosting you must select a base learner algorithm. For example, if we choose a classification tree, Bagging and Boosting would consist of a pool of trees as big as we want.
