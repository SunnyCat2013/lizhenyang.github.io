

```python
import numpy as np
import xgboost as xgb
```

Advanced customised loss function


```python
print('Start running example to use customised objective function.')
```

    Start running example to use customised objective function.



```python
dtrain = xgb.DMatrix('./demo/data/agaricus.txt.train')
```


```python
dtest = xgb.DMatrix('./demo/data/agaricus.txt.test')
```


```python
param = {'max_depth': 2, 'eta': 1, 'silent': 1}
```


```python
watchlist = [(dtest, 'eva'), (dtrain, 'train')]
```


```python
num_round = 2
```


```python
def logregobj(preds, dtrain):
    labels = dtrain.get_label()
    preds = 1.0 / (1.0 + np.exp(-preds)) # 不是很明白这里为什么要进行 sigmoid 计算
    grad = preds - labels
    hess = preds * (1.0 - preds)
    return grad, hess
```


```python
def evalerror(preds, dtrain):
    labels = dtrain.get_label()
    return 'error', float(sum(labels != (preds > 0.0)) / len(labels))
```


```python
bst = xgb.train(param, dtrain, num_round, watchlist, logregobj, evalerror)
```

    [0]	eva-rmse:1.59229	train-rmse:1.59597	eva-error:0.042831	train-error:0.046522
    [1]	eva-rmse:2.40519	train-rmse:2.40977	eva-error:0.021726	train-error:0.022263

