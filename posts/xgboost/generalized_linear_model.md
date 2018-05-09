

```python
import xgboost as xgb
import numpy as np
dtrain = xgb.DMatrix('./demo/data/agaricus.txt.train')
dtest = xgb.DMatrix('./demo/data/agaricus.txt.test')
```


```python
param = {
    'silent': 1,
    'objective': 'binary:logistic',
    'booster': 'gblinear', # 选择线性模型
    'alpha': 0.0001, # L1 正则系数
    'lambda': 1 # L2 正则系数
}
```


```python
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
```


```python
num_round = 4
```


```python
bst = xgb.train(param, dtrain, num_round, watchlist)
```

    [0]	eval-error:0.114215	train-error:0.104714
    [1]	eval-error:0.116698	train-error:0.106249
    [2]	eval-error:0.120422	train-error:0.10671
    [3]	eval-error:0.121043	train-error:0.107017



```python
pred = bst.predict(dtest)
```


```python
label = dtest.get_label()
```


```python
print('Error = %f' % (sum([1 for i in range(len(pred)) if ((pred[i] > 0.5) != label[i])]) / float(len(label))))
```

    Error = 0.121043



```python
# print('Error = %f' % (np.sum((pred > 0.5) != label)) / float(len(label))) # 这种先变成一个 str，再执行 /
```


```python
print('Error = %f' % ((np.sum((pred > 0.5) != label)) / float(len(label)))) 
```

    Error = 0.121043


这个文件学习了创建线性模型和 L1 L2 正则
