

```python
import numpy as np
import xgboost as xgb
```


```python
# load data
dtrain = xgb.DMatrix('./demo/data/agaricus.txt.train')
dtest = xgb.DMatrix('./demo/data/agaricus.txt.test')
```


```python
param = {'max_depth': 2, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
```


```python
num_round = 3
```


```python
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
```


```python
bst = xgb.train(param, dtrain, num_round, watchlist)
```

    [0]	eval-error:0.042831	train-error:0.046522
    [1]	eval-error:0.021726	train-error:0.022263
    [2]	eval-error:0.006207	train-error:0.007063



```python
print('Start testing prediction from first n tree')
```

    Start testing prediction from first n tree



```python
label = dtest.get_label()
```


```python
ypred1 = bst.predict(dtest, ntree_limit = 1)
```


```python
ypred2 = bst.predict(dtest) # 默认情况下使用所有的树
```


```python
print('error of ypred1 = %f' % (np.sum((ypred1 > 0.5) != label) / float(len(label))))
```

    error of ypred1 = 0.042831



```python
print('error of ypred2 = %f' % (np.sum((ypred2 > 0.5) != label) / float(len(label))))
```

    error of ypred2 = 0.006207


这个文件只是用来学习控制树的数量，可是我现在还不了解树是怎么构造的、结构是什么样的。
