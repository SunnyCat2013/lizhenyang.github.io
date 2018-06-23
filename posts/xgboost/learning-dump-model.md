# [Dump model](https://github.com/dmlc/xgboost/tree/master/demo/binary_classification)
Dump model 是一个基础特性，目前为止只有树形模型支持文本输出。
它可以把决策树用文本的方式输出出来。
下面看一个例子：
```
booster[0]:
0:[odor=pungent] yes=2,no=1
	1:[stalk-root=cup] yes=4,no=3
		3:leaf=1.71218
		4:leaf=-1.70044
	2:[spore-print-color=orange] yes=6,no=5
		5:leaf=-1.94071
		6:leaf=1.85965
booster[1]:
0:[stalk-root=missing] yes=2,no=1
	1:[odor=pungent] yes=4,no=3
		3:leaf=0.784718
		4:leaf=-0.96853
	2:leaf=-6.23624
```
# 读法
以下面一行为例：

```
0:[f30<1.5] yes=1,no=2,missing=1
```
结点: 0

选择特征: f30
    - 特征小于 1.5，则选择结点 1
    - 否则，选择结点 2 
    - missing 这个暂时还不清楚。

当然，它需要一个特征与文件的对照表，就是一个 feature map 文件

## Feature map 文件
Feature map 文件格式如下：
```
Format of featmap.txt: <featureid> <featurename> <q or i or int>\n:

    Feature id must be from 0 to number of features, in sorted order.
    i means this feature is binary indicator feature
    q means this feature is a quantitative value, such as age, time, can be missing
    int means this feature is integer value (when int is hinted, the decision boundary will be integer)
```

```

0	cap-shape=bell	i
1	cap-shape=conical	i
2	cap-shape=convex	i
3	cap-shape=flat	i
.
.
.
通过实例我们可以看出，feature map 的格式：
    <特征 id> <特征名称=特征值> <q or i or int>
    - 特征 id 排序从 0 开始升序
    - i 二选一的特征
    - q 数量值，如年龄、时间。这个值可以是空
    - int 整型特征，它的决策边界也应该是整型
同时注意，这有一个元素之间的分割符是不可见字符。所以在 <featureid> <featurename> 不能有空格。
```

