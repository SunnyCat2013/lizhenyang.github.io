# xgboost get_fscore 判断特征重要程度的三种指标

get_fscore 有三种种评判特征重要程度的方法：
```
‘weight’ - the number of times a feature is used to split the data across all trees.
‘gain’ - the average gain of the feature when it is used in trees.
‘cover’ - the average coverage of the feature when it is used in trees.

weight - 该特征在所有树中被用作分割样本的特征的次数。
gain - 在所有树中的平均增益。
cover - 在树中使用该特征时的平均覆盖范围。(还不是特别明白)
```
