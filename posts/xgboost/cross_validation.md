

```python
import numpy as np
import xgboost as xgb
```


```python
dtrain = xgb.DMatrix('./demo/data/agaricus.txt.train')
param = {'max_depth': 2, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
num_round = 2
```


```python
print('Running cross validation')
```

    Running cross validation



```python
xgb.cv(param, dtrain, num_round, nfold = 5, 
       metrics = {'error'}, seed = 0,
       callbacks = [xgb.callback.print_evaluation(show_stdv = True)])
```

    [0]	train-error:0.0506682+0.009201	test-error:0.0557316+0.0158887
    [1]	train-error:0.0213034+0.00205561	test-error:0.0211884+0.00365323





    {'train-error-mean': [0.0506682, 0.0213034],
     'train-error-std': [0.009200997193782855, 0.0020556122786167634],
     'test-error-mean': [0.055731600000000006, 0.021188400000000003],
     'test-error-std': [0.015888666194492227, 0.0036532266614597024]}



只用训练数据做 cross validation


```python
print('Running cross validation, disable standard deviation display')
```

    Running cross validation, disable standard deviation display



```python
res = xgb.cv(param, 
             dtrain, 
             num_boost_round = 10, nfold = 5, 
       metrics = {'error'}, seed = 0,
       callbacks = [xgb.callback.print_evaluation(show_stdv = True), xgb.callback.early_stop(3)])
```

    [0]	train-error:0.0506682+0.009201	test-error:0.0557316+0.0158887
    Multiple eval metrics have been passed: 'test-error' will be used for early stopping.
    
    Will train until test-error hasn't improved in 3 rounds.
    [1]	train-error:0.0213034+0.00205561	test-error:0.0211884+0.00365323
    [2]	train-error:0.0099418+0.00607648	test-error:0.0099786+0.00482795
    [3]	train-error:0.0141256+0.00170577	test-error:0.0144336+0.00351713
    [4]	train-error:0.0059878+0.00187791	test-error:0.0062948+0.00312318
    [5]	train-error:0.0020344+0.00146961	test-error:0.0016886+0.000574184
    [6]	train-error:0.0012284+0.000260265	test-error:0.001228+0.00104094
    [7]	train-error:0.0012284+0.000260265	test-error:0.001228+0.00104094
    [8]	train-error:0.0009212+0.000506197	test-error:0.001228+0.00104094
    [9]	train-error:0.0006142+0.000506319	test-error:0.001228+0.00104094
    Stopping. Best iteration:
    [6]	train-error:0.0012284+0.000260265	test-error:0.001228+0.00104094
    



```python
print(res)
```

    {'train-error-mean': [0.0506682, 0.0213034, 0.009941799999999999, 0.014125599999999999, 0.0059878, 0.0020344, 0.0012284], 'train-error-std': [0.009200997193782855, 0.0020556122786167634, 0.006076479256938181, 0.0017057689878761427, 0.0018779069625516596, 0.001469605198684327, 0.00026026494193417596], 'test-error-mean': [0.055731600000000006, 0.021188400000000003, 0.009978599999999999, 0.0144336, 0.006294800000000001, 0.0016885999999999997, 0.001228], 'test-error-std': [0.015888666194492227, 0.0036532266614597024, 0.004827953421482027, 0.003517125508138713, 0.0031231752688570006, 0.0005741844999649501, 0.0010409403441119958]}



```python
def fpreproc(dtrain, dtest, param):
    label = dtrain.get_label()
    ratio = float(np.sum(label == 0)) / np.sum(label == 1)
    param['scale_pos_weight'] = ratio
    return (dtrain, dtest, param)
```


```python
xgb.cv(param, dtrain, num_round, nfold = 5, metrics = {'auc'}, seed = 0, fpreproc = fpreproc)
```




    {'train-auc-mean': [0.9582284, 0.9814142],
     'train-auc-std': [0.001441856664166039, 0.0006469174290433207],
     'test-auc-mean': [0.9582322, 0.9814308],
     'test-auc-std': [0.005778480990710278, 0.002595425545069615]}




```python
print('Running cross validation with customised loss function')
```

    Running cross validation with customised loss function



```python
def logregobj(preds, dtrain):
    labels = dtrain.get_label()
    preds = 1.0 / (1.0 + np.exp(-preds))
    grad = preds - labels
    hess = preds * (1.0 - preds)
    return grad, hess
```


```python
def evalerror(preds, dtrain):
    labels = dtrain.get_label()
    return 'Error', float(sum(labels != (preds > 0.0)) / len(labels))
```


```python
param = {'max_depth': 2, 'eta': 1, 'silent': 1}
```


```python
xgb.cv(param, dtrain, num_round, nfold = 5, seed = 0, obj = logregobj, feval = evalerror)
```




    {'train-Error-mean': [0.0506682, 0.0213034],
     'train-Error-std': [0.009200997193782855, 0.0020556122786167634],
     'train-rmse-mean': [1.5950724, 2.4426004000000003],
     'train-rmse-std': [0.0038675500565603345, 0.07683424711312019],
     'test-Error-mean': [0.055731600000000006, 0.021188400000000003],
     'test-Error-std': [0.015888666194492227, 0.0036532266614597024],
     'test-rmse-mean': [1.5980429999999999, 2.4492819999999997],
     'test-rmse-std': [0.012825987899573323, 0.08089986739914967]}


