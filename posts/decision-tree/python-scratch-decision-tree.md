
# 使用 python 自己写一个 决策树
很多复杂的学习方法，明白了其基础之后，一切就变得简单、易懂，并且符合直觉。
我今天打算手写一个决策树，或者说是“分类回归树”。

## 参考
https://machinelearningmastery.com/implement-decision-tree-algorithm-scratch-python/


决策树是一种强大的预测方法，在工业界的数据分析和决策中非常好用。
它受欢迎的一个主要原因是，它最终的模型就像给你写出了一堆 `if else` 的判断条件。
这样，无论通过模型获得怎样的结果，都可以通过判断条件进行反推。
因为这个优势的存在，决策树就可以帮助我们这些从业人员，更好地分析数据。

同时决策树还是其它先进的集成学习方法（advanced ensemble methods）的基石。
如，bagging, random forests 和 gradient boosting。

## 待解决的几个总是
- 如何评估分裂点。知道如何评估之后，就可以找到它了。
- How to arrange splits into a decision tree structure.
- 怎么在一个实际问题中使用决策树

## 简介
Classification and Regression Tree(CART) 是对决策树的一个比较现代的叫法。
决策树用到的模型是二叉树这种数据结构，每个结点有 0 个，或者 1 个，或者 2 个子结点。

每个结点，代表了一个输入变量和这个变量的分割点，叶结点包含一个输出。

决策树一旦创建，新的数据就可以通过根结点，经过各种判断条件，最终到叶结点，并把叶结点表示的结果作为输出。

### 分割时的损失函数
- *回归模型的损失函数:* 使用最小方差作为损失函数
- *分类模型损失函数:* 使用 Gini 损失函数，Gini Score 是用来衡量一个子结点中包含类型的混乱程度的，越混乱 Gini Score 越大，分类效果自然是就越差。

### 用来做测试的数据 Banknote Dataset
Banknote Dataset 给出了一些用来描述钞票图片的数据，并用这些数据对钞票的真伪进行判断。

这个数据集饮食 1372 个样本，每行有 5 个数值特征。
这个任务是一个二分类任务。

特征描述如下：
```
1. 图像的小波变换方差（连续数值）
2. 图像的小波变换偏度(skewness)（连续数值）
3. 图像的小波变换峭度(kurtosis)（连续数值）
4. 图像的熵（连续数值）
5. 样本的类别（整数）
```

数据示例如下：

```
3.6216,8.6661,-2.8073,-0.44699,0
4.5459,8.1674,-2.4586,-1.4621,0
3.866,-2.6383,1.9242,0.10645,0
3.4566,9.5228,-4.0112,-3.5944,0
0.32924,-4.4552,4.5718,-0.9888,0
4.3684,9.6718,-3.9606,-3.1625,0
```



> 未理解问题
Zero Rule Algorithm

> Using the Zero Rule Algorithm to predict the most common class value, the baseline accuracy on the problem is about 50%.
这个意思好像是说，就按大多数的类型作为全部的类别，进而得到分类正确率。并用它作为 baseline.

#### 下载
[banknote authentication Data Set](http://archive.ics.uci.edu/ml/datasets/banknote+authentication)


```python
banknote_authentication = './data_banknote_authentication.csv'
```

## 目录
下面分五部分分别实现
1. Gini Index
2. Create Split
3. Build a Tree
4. Make a Prediction
5. Banknote Case Study

# Gini Index


```python
def gini_score(groups, classes):
    '''
    row = [col1, col2, col3, col4, class]
    group: [row, row, ..., row]
    groups: [group, group, ..., group]
        
    classes: [0, 1]
    '''
    # weight = sum(group) / sum(sum(group))
    # Gini index = sum(sum(one_class) / sum(group))
    instances_num = sum([len(group) for group in groups])
    gini_score = 0.0
    for group in groups:
        group_num = len(group)
        if group_num == 0:
            continue
        gini_index = 1.0
        for c in classes:
            c_num = 0
            for i in group:
                if c == i[-1]:
                    c_num += 1
            c_p = c_num / group_num # group_num == 0?
            gini_index = gini_index - c_p * c_p
        group_gini_score = gini_index * group_num / instances_num
        gini_score += group_gini_score
    return gini_score
```


```python
row1 = [0,0,0,0,1]
row2 = [0,0,0,0,0]
group1 = [row1, row2]
row3 = [0,0,0,0,0]
row4 = [0,0,0,0,1]
row5 = [0,0,0,0,1]
group2 = [row3, row4, row5]

test_data_for_gini_index = [group1, group2]

classes = [0, 1]
```


```python
gini_score(test_data_for_gini_index, classes)
```




    0.4666666666666667



### 博客里面的函数对比测试



```python
# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
	# count all samples at split point
	n_instances = float(sum([len(group) for group in groups]))
	# sum weighted Gini index for each group
	gini = 0.0
	for group in groups:
		size = float(len(group))
		# avoid divide by zero
		if size == 0:
			continue
		score = 0.0
		# score the group based on the score for each class
		for class_val in classes:
			p = [row[-1] for row in group].count(class_val) / size
			score += p * p
		# weight the group score by its relative size
		gini += (1.0 - score) * (size / n_instances)
	return gini

# test Gini values
groups1 = [[[1, 1], [1, 0]], [[1, 1], [1, 0]]]
groups2 = [[[1, 0], [1, 0]], [[1, 1], [1, 1]]]
classes = [0, 1]
print(gini_index(groups1, classes))
print(gini_index(groups2, classes))
print(gini_score(groups1, classes))
print(gini_score(groups2, classes))
```

    0.5
    0.0
    0.5
    0.0


# Create Split

在某个维度上，对样本进行二分类


```python
def split_group(index, split_value, group):
    less = list()
    big = list()
    for row in group:
        if row[index] < split_value:
            less.append(row)
        else:
            big.append(row)
         
    return less, big
```


```python
# test 
l, b = split_group(1, 0.5, [[1, 1], [1, 0]])
print(l, b)
```

    [[1, 0]] [[1, 1]]


使用穷举和贪心算法进行处理（This is an exhaustive and greedy algorithm.）

> We will use a dictionary to represent a node in the decision tree as we can store data by name. When selecting the best split and using it as a new node for the tree we will store the index of the chosen attribute, the value of that attribute by which to split and the two groups of data split by the chosen split point.


```python
import math
print(math.inf)
```

    inf



```python
import math
# 找到最佳分裂特征点，并分裂
def get_split(group):
    best_index = 0
    best_split_value = 0
    best_gini = math.inf
    best_groups = None
    classes = list(set([row[-1] for row in group]))
    for i in range(len(group[0]) - 1): # minus 1, because the last value is label
        tem_split_values = list(set([row[i] for row in group]))
        for split_value in tem_split_values:
            groups = split_group(i, split_value, group)
            gini = gini_score(groups, classes)
            
            #print('X%d < %.3f Gini=%.3f' % ((i + 1), split_value, gini))
            if gini < best_gini:
                best_gini = gini
                best_index = i
                best_split_value = split_value
                best_groups = groups
    return {
        'index': best_index,
        'split_value': best_split_value,
        'groups': best_groups
    }  
```


```python
group = [[2.771244718,1.784783929,0],
    [1.728571309,1.169761413,0],
    [3.678319846,2.81281357,0],
    [3.961043357,2.61995032,0],
    [2.999208922,2.209014212,0],
    [7.497545867,3.162953546,1],
    [9.00220326,3.339047188,1],
    [7.444542326,0.476683375,1],
    [10.12493903,3.234550982,1],
    [6.642287351,3.319983761,1]]
split = get_split(group)
print('Split: [X%d < %.3f]' % ((split['index']+1), split['split_value']))

```

    X1 < 1.729 Gini=0.500
    X1 < 2.771 Gini=0.444
    X1 < 3.961 Gini=0.167
    X1 < 3.678 Gini=0.286
    X1 < 2.999 Gini=0.375
    X1 < 6.642 Gini=0.000
    X1 < 7.498 Gini=0.286
    X1 < 7.445 Gini=0.167
    X1 < 9.002 Gini=0.375
    X1 < 10.125 Gini=0.444
    X2 < 0.477 Gini=0.500
    X2 < 1.785 Gini=0.500
    X2 < 2.813 Gini=0.320
    X2 < 2.620 Gini=0.417
    X2 < 1.170 Gini=0.444
    X2 < 2.209 Gini=0.476
    X2 < 3.163 Gini=0.167
    X2 < 3.339 Gini=0.444
    X2 < 3.235 Gini=0.286
    X2 < 3.320 Gini=0.375
    Split: [X1 < 6.642]



```python
print(split)
```

    {'index': 0, 'split_value': 6.642287351, 'groups': ([[2.771244718, 1.784783929, 0], [1.728571309, 1.169761413, 0], [3.678319846, 2.81281357, 0], [3.961043357, 2.61995032, 0], [2.999208922, 2.209014212, 0]], [[7.497545867, 3.162953546, 1], [9.00220326, 3.339047188, 1], [7.444542326, 0.476683375, 1], [10.12493903, 3.234550982, 1], [6.642287351, 3.319983761, 1]])}


其实可以看出，每次查找的点都不一定是全局最优的，也没有一个全局最优函数。

# Build a Tree

创建一个树的三个过程：
1. 找到终止结点
2. 递归分裂
3. 创建一个树

## 停止条件
常见的停止条件有两种
1. 一个划分里面的样本个数少于某个值的时候停止。分的太细容易过拟合。
2. 当树的深度大于某个值的时候停止（xgboost 里面默认的就是这个）。分的太深容易过拟合。

其实这两个异曲同工，一个是深度，一个是广度。

一旦找到终止结点，这个结点将用于做最终的预测。


```python
# Create a terminal node value, find the majority class and use it as the label or value.
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count) # 返回出现次数最多的值
```


```python
to_terminal(group)
```




    0




```python
outcomes = [1,2,2,2]
max(set(outcomes), key=outcomes.count) # 
```




    2




```python
set(outcomes)
```




    {1, 2}




```python
outcomes.count(2)
```




    3



## 递归分裂


```python
def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])
    ##
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    ##
    if depth >= max_depth:
        node['left'] = to_terminal(left)
        node['right'] = to_terminal(right)
        return 
    
    if len(left) < min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth + 1)
    
    if len(right) < min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth + 1)
    
```

## 开始创建树


```python
root = get_split(group)
split(root, 2, 1, 1)
```

    X1 < 1.729 Gini=0.500
    X1 < 2.771 Gini=0.444
    X1 < 3.961 Gini=0.167
    X1 < 3.678 Gini=0.286
    X1 < 2.999 Gini=0.375
    X1 < 6.642 Gini=0.000
    X1 < 7.498 Gini=0.286
    X1 < 7.445 Gini=0.167
    X1 < 9.002 Gini=0.375
    X1 < 10.125 Gini=0.444
    X2 < 0.477 Gini=0.500
    X2 < 1.785 Gini=0.500
    X2 < 2.813 Gini=0.320
    X2 < 2.620 Gini=0.417
    X2 < 1.170 Gini=0.444
    X2 < 2.209 Gini=0.476
    X2 < 3.163 Gini=0.167
    X2 < 3.339 Gini=0.444
    X2 < 3.235 Gini=0.286
    X2 < 3.320 Gini=0.375
    X1 < 1.729 Gini=0.000
    X1 < 2.771 Gini=0.000
    X1 < 3.961 Gini=0.000
    X1 < 3.678 Gini=0.000
    X1 < 2.999 Gini=0.000
    X2 < 1.785 Gini=0.000
    X2 < 2.813 Gini=0.000
    X2 < 2.620 Gini=0.000
    X2 < 1.170 Gini=0.000
    X2 < 2.209 Gini=0.000
    X1 < 6.642 Gini=0.000
    X1 < 7.445 Gini=0.000
    X1 < 7.498 Gini=0.000
    X1 < 9.002 Gini=0.000
    X1 < 10.125 Gini=0.000
    X2 < 0.477 Gini=0.000
    X2 < 3.339 Gini=0.000
    X2 < 3.320 Gini=0.000
    X2 < 3.163 Gini=0.000
    X2 < 3.235 Gini=0.000



```python
root
```




    {'index': 0,
     'split_value': 6.642287351,
     'left': {'index': 0, 'split_value': 1.728571309, 'left': 0, 'right': 0},
     'right': {'index': 0, 'split_value': 6.642287351, 'left': 1, 'right': 1}}




```python
def build_tree(train_group, max_depth, min_size):
    root = get_split(train_group)
    split(root, max_depth, min_size, 1)
    return root
```


```python
def print_tree(node, depth = 0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % (depth*' ', node['index'] + 1, node['split_value']))
        print_tree(node['left'], depth + 1)
        print_tree(node['right'], depth + 1)
    else:
        print('%s%.3f' % (depth*' ', node))
```


```python
dataset = [[2.771244718,1.784783929,0],
    [1.728571309,1.169761413,0],
    [3.678319846,2.81281357,0],
    [3.961043357,2.61995032,0],
    [2.999208922,2.209014212,0],
    [7.497545867,3.162953546,1],
    [9.00220326,3.339047188,1],
    [7.444542326,0.476683375,1],
    [10.12493903,3.234550982,1],
    [6.642287351,3.319983761,1]]
tree = build_tree(dataset, 2, 1)
print_tree(tree)

```

    X1 < 1.729 Gini=0.500
    X1 < 2.771 Gini=0.444
    X1 < 3.961 Gini=0.167
    X1 < 3.678 Gini=0.286
    X1 < 2.999 Gini=0.375
    X1 < 6.642 Gini=0.000
    X1 < 7.498 Gini=0.286
    X1 < 7.445 Gini=0.167
    X1 < 9.002 Gini=0.375
    X1 < 10.125 Gini=0.444
    X2 < 0.477 Gini=0.500
    X2 < 1.785 Gini=0.500
    X2 < 2.813 Gini=0.320
    X2 < 2.620 Gini=0.417
    X2 < 1.170 Gini=0.444
    X2 < 2.209 Gini=0.476
    X2 < 3.163 Gini=0.167
    X2 < 3.339 Gini=0.444
    X2 < 3.235 Gini=0.286
    X2 < 3.320 Gini=0.375
    X1 < 1.729 Gini=0.000
    X1 < 2.771 Gini=0.000
    X1 < 3.961 Gini=0.000
    X1 < 3.678 Gini=0.000
    X1 < 2.999 Gini=0.000
    X2 < 1.785 Gini=0.000
    X2 < 2.813 Gini=0.000
    X2 < 2.620 Gini=0.000
    X2 < 1.170 Gini=0.000
    X2 < 2.209 Gini=0.000
    X1 < 6.642 Gini=0.000
    X1 < 7.445 Gini=0.000
    X1 < 7.498 Gini=0.000
    X1 < 9.002 Gini=0.000
    X1 < 10.125 Gini=0.000
    X2 < 0.477 Gini=0.000
    X2 < 3.339 Gini=0.000
    X2 < 3.320 Gini=0.000
    X2 < 3.163 Gini=0.000
    X2 < 3.235 Gini=0.000
    [X1 < 6.642]
     [X1 < 1.729]
      0.000
      0.000
     [X1 < 6.642]
      1.000
      1.000


# 测试


```python
file = 'data_banknote_authentication.csv'
```


```python
from csv import reader
```


```python
def load_csv(filename):
    with open(filename, 'r') as inf:
        lines = reader(inf)
        dataset = list(lines)
        return dataset
```


```python
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())
```


```python
# Split a dataset into k folds
# CART on the Bank Note dataset
from random import seed
from random import randrange
def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split
```


```python
# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0
```


```python
# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
            
        print('lenght of test_set', len(test_set))
        predicted = algorithm(train_set, test_set, *args)
        print('length: predicted', len(predicted))
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores
```


```python
# Prediction
def predict(node, row):
    
    if isinstance(node, dict):
        index = node['index']
        split_value = node['split_value']
        if row[index] < split_value:
            return predict(node['left'], row)
        else:
            return predict(node['right'], row)
    else:
        return node
```


```python
# Classification and Regression Tree Algorithm
def decision_tree(train, test, max_depth, min_size):
    tree = build_tree(train, max_depth, min_size)
    predictions = list()
    print('test', len(test))
    for row in test:
        prediction = predict(tree, row)
        predictions.append(prediction)
    return predictions
```


```python
filename = 'data_banknote_authentication.csv'
dataset = load_csv(filename)
# convert string attributes to integers
for i in range(len(dataset[0])):
    str_column_to_float(dataset, i)
# evaluate algorithm
n_folds = 5
max_depth = 5
min_size = 10
scores = evaluate_algorithm(dataset, decision_tree, n_folds, max_depth, min_size)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
```

    lenght of test_set 274
    test 274
    length: predicted 274
    lenght of test_set 274
    test 274
    length: predicted 274
    lenght of test_set 274
    test 274
    length: predicted 274
    lenght of test_set 274
    test 274
    length: predicted 274
    lenght of test_set 274
    test 274
    length: predicted 274
    Scores: [94.8905109489051, 97.08029197080292, 98.90510948905109, 94.8905109489051, 98.54014598540147]
    Mean Accuracy: 96.861%


# 学到的 python



```python
depth = 3
depth*'h'
```




    'hhh'




```python
data = [1,2,3,4]
data_copy = list(data)
```


```python
not []
```




    True


