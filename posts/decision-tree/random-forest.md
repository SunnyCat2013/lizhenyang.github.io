# 随机森林
之前学习随机森林，一直很迷糊。
尤其后面又接受了关于 Bagging/Boosting/Ensemble 等一些概念就更迷了。。。
还好，最近学习了 Ensemble 集成学习下面的两种技术 Bagging（等概率抽样训练子模型）和 Boosting（根据上次分类结果调整权重）两种方法，再来看 Random Forest 就豁然开朗了。

*Random Forest 不就是使用 Bagging 技术，并行训练 N 个子分类器的集成模型嘛！*

所以劝大家学习 Random Forest 之前，先搞清楚上面那几个概念。避免越学越乱。


# 随机森林的随机性

- 构建子模型的样本选择的*随机性*
- 子模型中选择进行分支的特征的时候，不是在所有特征中进行筛选，而是在所有特征集中*随机选出*一组备选特征，并在这组特征中找最优的分支特征。



# References

https://quantdare.com/random-forest-vs-simple-tree/
