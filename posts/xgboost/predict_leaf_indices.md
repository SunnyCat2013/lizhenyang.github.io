

```python
import xgboost as xgb
```


```python
dtrain = xgb.DMatrix('./demo/data/agaricus.txt.train')
dtest = xgb.DMatrix('./demo/data/agaricus.txt.test')
param = {'max_depth': 2, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
num_round = 3
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
```


```python
bst = xgb.train(param, dtrain, num_round, watchlist)
```

    [0]	eval-error:0.042831	train-error:0.046522
    [1]	eval-error:0.021726	train-error:0.022263
    [2]	eval-error:0.006207	train-error:0.007063



```python
print('Start testing predict the leaf indices')
```

    Start testing predict the leaf indices



```python
leafindex = bst.predict(dtest, ntree_limit = 2, pred_leaf = True)
```


```python
print(leafindex.shape)
```

    (1611, 2)



```python
print(leafindex)
```

    [[4 3]
     [3 3]
     [4 3]
     ...
     [3 3]
     [5 4]
     [3 3]]



```python
print('Predict all trees')
```

    Predict all trees



```python
leafindex = bst.predict(dtest, pred_leaf = True)
```


```python
print(leafindex.shape)
```

    (1611, 3)



```python
print(leafindex)
```

    [[4 3 5]
     [3 3 5]
     [4 3 5]
     ...
     [3 3 3]
     [5 4 5]
     [3 3 3]]

