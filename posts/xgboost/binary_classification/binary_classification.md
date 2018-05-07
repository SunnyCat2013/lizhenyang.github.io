
# 按照 https://github.com/dmlc/xgboost/tree/master/demo/binary_classification 获取数据

# 疑问
- `booster` 不同类型的区别
    - gblinear
    - gbtree


```python
import numpy as np
```


```python
import xgboost as xgb
```


```python
dtrain = xgb.DMatrix('agaricus.txt.train')
```


```python
dtest = xgb.DMatrix('agaricus.txt.test')
```


```python
params = {
    'booster': 'gbtree',
    'objective': 'binary:logistic', # 损失函数
    'eta': 1.0, # 学习率
    'gamma': 1.0, # minimum loss reduction required to make a further partition on a leaf node of the tree. The larger, the more conservative the algorithm will be.
    'min_child_weight': 1, # 如果子结点的实例权重之和小于这个值，就不再分块了。
    'max_depth': 3
    # the console version parameters 
    # num_round = 2
}
```

We use the tree booster and logistic regression objective in our setting. This indicates that we accomplish our task using classic gradient boosting regression tree(GBRT), which is a promising method for binary classification.
树形提升和 logistic regression objective 就是经典的树形提升回归树 (GBRT)


```python
watchlist = [(dtest, 'eval'), (dtrain, 'test')]
```


```python
num_round = 1
```


```python
bst = xgb.train(params, dtrain, num_round, watchlist)
```

    [0]	eval-error:0.015793	test-error:0.014524



```python
preds = bst.predict(dtest)
labels = dtest.get_label()
print('error=%f' % (sum(1 for i in range(len(preds)) if int(preds[i] > 0.5) != labels[i]) / float(len(preds))))
```

    error=0.015793



```python
bst.dump_model('dump.nice.model', 'featmap.txt')
```


```python
with open('dump.nice.model', 'r') as inf:
    print(inf.read())
```

    booster[0]:
    0:[odor=pungent] yes=2,no=1
    	1:[stalk-root=cup] yes=4,no=3
    		3:[stalk-root=missing] yes=8,no=7
    			7:leaf=1.899
    			8:leaf=-1.94737
    		4:[bruises?=no] yes=10,no=9
    			9:leaf=1.78378
    			10:leaf=-1.98135
    	2:[spore-print-color=orange] yes=6,no=5
    		5:[stalk-surface-below-ring=silky] yes=12,no=11
    			11:leaf=-1.98546
    			12:leaf=0.938776
    		6:leaf=1.87097
    

