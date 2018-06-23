
code: https://github.com/dmlc/xgboost/tree/master/demo/multiclass_classification

data: https://archive.ics.uci.edu/ml/datasets/Dermatology


```python
import numpy as np
import xgboost as xgb
```


```python
data = np.loadtxt('./dermatology.data', delimiter=',',
        converters={33: lambda x:int(x == '?'), 34: lambda x:int(x) - 1})
```


```python
sz = data.shape
```


```python
train = data[:int(sz[0] * 0.7), :]
test = data[int(sz[0] * 0.7):, :]

train_X = train[:, :33]
train_Y = train[:, 34]

test_X = test[:, :33]
test_Y = test[:, 34]
```


```python
xg_train = xgb.DMatrix(train_X, label=train_Y)
xg_test = xgb.DMatrix(test_X, label=test_Y)
```


```python
# setup parameters for xgboost
param = {}
# use softmax multi-class classification
param['objective'] = 'multi:softmax'
# scale weight of positive examples
param['eta'] = 0.1
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 6
```


```python
watchlist = [(xg_train, 'train'), (xg_test, 'test')]
num_round = 5
bst = xgb.train(param, xg_train, num_round, watchlist)
```

    [0]	train-merror:0.011719	test-merror:0.127273
    [1]	train-merror:0.015625	test-merror:0.127273
    [2]	train-merror:0.011719	test-merror:0.109091
    [3]	train-merror:0.007812	test-merror:0.081818
    [4]	train-merror:0.007812	test-merror:0.090909



```python
# get prediction
pred = bst.predict(xg_test)
error_rate = np.sum(pred != test_Y) / test_Y.shape[0]
print('Test error using softmax = {}'.format(error_rate))

```

    Test error using softmax = 0.09090909090909091



```python
# do the same thing again, but output probabilities
param['objective'] = 'multi:softprob'
bst = xgb.train(param, xg_train, num_round, watchlist)
# Note: this convention has been changed since xgboost-unity
# get prediction, this is in 1D array, need reshape to (ndata, nclass)
pred_prob = bst.predict(xg_test).reshape(test_Y.shape[0], 6)
pred_label = np.argmax(pred_prob, axis=1)
error_rate = np.sum(pred_label != test_Y) / test_Y.shape[0]
print('Test error using softprob = {}'.format(error_rate))

```

    [0]	train-merror:0.011719	test-merror:0.127273
    [1]	train-merror:0.015625	test-merror:0.127273
    [2]	train-merror:0.011719	test-merror:0.109091
    [3]	train-merror:0.007812	test-merror:0.081818
    [4]	train-merror:0.007812	test-merror:0.090909
    Test error using softprob = 0.09090909090909091

