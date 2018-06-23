

```python
import numpy as np
import xgboost as xgb
```


```python
dtrain = xgb.DMatrix('./demo/data/agaricus.txt.train')
```


```python
dtest = xgb.DMatrix('./demo/data/agaricus.txt.test')
```


```python
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
```


```python
print('Start running example to start from a initial prediction')
```

    Start running example to start from a initial prediction



```python
param = {'max_depth': 2, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
```


```python
bst = xgb.train(param, dtrain, 1, watchlist)
```

    [0]	eval-error:0.042831	train-error:0.046522



```python
ptrain = bst.predict(dtrain, output_margin = True) # output_margin? margin value 是什么？
```


```python
ptest = bst.predict(dtest, output_margin = True) 
```


```python
dtrain.set_base_margin(ptrain)
```


```python
dtest.set_base_margin(ptest)
```


```python
print('This is result of running from initial prediction')
```

    This is result of running from initial prediction



```python
bst = xgb.train(param, dtrain, 1, watchlist)
```

    [0]	eval-error:0.021726	train-error:0.022263


从结果上来看，错误率似乎下降了。
