```python
import numpy as np
```

```python
import scipy.sparse
```

```python
import pickle
```

```python
import xgboost as xgb
```

# 从文件或者 xgboost 生成的二进制缓存中读取数据

```python
dtrain = xgb.DMatrix('demo/data/agaricus.txt.train')
dtest = xgb.DMatrix('demo/data/agaricus.txt.test')
```

# 用 dict 保存参数

```python
param = {
    'max_depth': 2,
    'eta': 1,
    'silent': 1,
    'objective': 'binary:logistic'
}
```

# 设置 validation set

```python
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
```

```python
num_round = 2
```

```python
bst = xgb.train(param, dtrain, num_round, watchlist)
```

```
[0]    eval-error:0.042831    train-error:0.046522
[1]    eval-error:0.021726    train-error:0.022263
```

# 预测

```python
preds = bst.predict(dtest)
```

```python
labels = dtest.get_label()
```

```python
labels
```

```
array([0., 1., 0., ..., 1., 0., 1.], dtype=float32)
```

```python
preds
```

```
array([0.28583017, 0.9239239 , 0.28583017, ..., 0.9239239 , 0.05169873,
       0.9239239 ], dtype=float32)
```

```python
preds > 0.5
```

```
array([False,  True, False, ...,  True, False,  True])
```

```python
pred_labels = np.copy(preds)
```

# 选择阈值进行二分类

```python
threshold = 0.5
```

```python
pred_labels[preds > threshold] = 1
```

```python
pred_labels[preds <= threshold] = 0
```

```python
pred_labels
```

```
array([0., 1., 0., ..., 1., 0., 1.], dtype=float32)
```

```python
print(sum(pred_labels == labels) / labels.shape)
```

```
[0.97827436]
```

```python
sum(np.array([True, False, True, False]))
```

```
2
```

```python
bst.save_model('test.model')
```

# dump model: 这个不是很理解，是说可以把模型和特征一一对应起来输出吗？看下面的 save\_model，好像 dump\_model 并不是保存模型，因为不能用 Booster\(\) 加载

```python
bst.dump_model('dump.raw.txt')
```

```python
bst.dump_model('dump.nice.txt', 'demo/data/featmap.txt')
```

```python
cat dump.nice.txt
```

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

```python
cat dump.raw.txt
```

```
booster[0]:
0:[f29<-9.53674e-07] yes=1,no=2,missing=1
    1:[f56<-9.53674e-07] yes=3,no=4,missing=3
        3:leaf=1.71218
        4:leaf=-1.70044
    2:[f109<-9.53674e-07] yes=5,no=6,missing=5
        5:leaf=-1.94071
        6:leaf=1.85965
booster[1]:
0:[f60<-9.53674e-07] yes=1,no=2,missing=1
    1:[f29<-9.53674e-07] yes=3,no=4,missing=3
        3:leaf=0.784718
        4:leaf=-0.96853
    2:leaf=-6.23624
```

看结果，好像是用特征名称代替了数字？

# 把 dmatrix  保存到二进制缓存中

```python
dtest.save_binary('dtest.buffer')
```

# save model

```python
bst.save_model('xgb.boost')
```

# load model

```python
bst2 = xgb.Booster(model_file = 'xgb.boost')
```

```python
dtest2 = xgb.DMatrix('dtest.buffer')
```

```python
preds2 = bst2.predict(dtest2)
```

```python
assert np.sum(np.abs(preds2 - preds)) == 0
```

# 使用 scipy.sparse.csr\_matrix 从稀疏矩阵中读取数据矩阵。

scipy.sparse.csr\_matrix\(\(data, \(row, col\)\)\)，数据 list 和每个数据对应的行列，很好理解。  
理解了这个参数，以及原始数据的格式之后，就可以自己写数据读取的代码了。  
可以在 [https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr\_matrix.html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html) 里面看看例子。

```python
print('\n\n Start running examples of build DMatrix from scipy.sparse CSR Matrix \n')
```

```
 Start running examples of build DMatrix from scipy.sparse CSR Matrix 
```

```python
label = []
```

```python
row = []
```

```python
col = []
```

```python
dat = []
```

```python
i = 0
```

```python
for l in open('./demo/data/agaricus.txt.train'):
    arr = l.split()
    label.append(int(arr[0]))
    for it in arr[1:]:
        k, v = it.split(':')
        row.append(i)
        col.append(int(k))
        dat.append(float(v))
    i += 1
```

```python
len(label)
```

```
6513
```

```python
type(label[0])
```

```
int
```

```python
len(row)
```

```
143286
```

```python
len(col)
```

```
143286
```

```python
len(dat)
```

```
143286
```

```python
csr = scipy.sparse.csr_matrix((dat, (row, col)))
```

```python
type(label[0])
```

```
int
```

```python
dtrain = xgb.DMatrix(csr, label = label)
```

```python
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
```

```python
bst = xgb.train(param, dtrain, num_round, watchlist)
```

```
[0]    eval-error:0.042831    train-error:0.046522
[1]    eval-error:0.021726    train-error:0.022263
```

```python
print('Start running examples of buid DMatrix from numpy array')
```

```
Start running examples of buid DMatrix from numpy array
```

```python
npymat = csr.todense()
```

```python
dtrain = xgb.DMatrix(npymat, label = label)
```

```python
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
```

```python
bst = xgb.train(param, dtrain, num_round, watchlist)
```

```
[0]    eval-error:0.042831    train-error:0.046522
[1]    eval-error:0.021726    train-error:0.022263
```



