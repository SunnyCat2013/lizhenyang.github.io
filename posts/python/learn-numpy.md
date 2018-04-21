# Numpy
Numpy 是 python 中用于科学计算的库中一个比较重要的库。
它对高维的数组计算有很多优化。

# Arrays

numpy array 是网络状的数据，所有的数据都是相同的类型，索引是非负的整数。
维度的数目是数组的层级数。
numpy array 的 shape 是一个 tuple。每个维度的大小，按照维度的顺序排列。

```

import numpy as np

a = np.array([1, 2, 3])   # 创建一维数组。
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # 修改元素
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # 创建二维数组
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

```
Numpy 也提供了一些用于创建数组的函数：

```
import numpy as np

a = np.zeros((2,2))   # 全是 0 的矩阵
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # 都是 1 的矩阵
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # 常数矩阵
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # 对角矩阵
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # 随机矩阵
                                                                   print(e)                     # Might print "[[ 0.91940167  0.08143941]
                                                                                        #               [ 0.68744134  0.87236687]]"
```
更多参考 [arrays-creation](https://docs.scipy.org/doc/numpy/user/basics.creation.html#arrays-creation)

# Array Index
Numpy 提供了一些 Index 的方法
## Slicing
与 Python 相同，numpy array 也可以用 slicing 的方法来使用获取子矩阵

```
import numpy as np

# 创建矩阵 shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# 获取前两行，下标是 1 和 2 两列的子矩阵
# [[2 3]
#  [6 7]]
# 但是这种方式，只能在 numpy.array 中使用，list 中只能用在一维 list 中。也就是说 list 只是一维，不能作为矩阵。
b = a[:2, 1:3]

# 但是一定要注意，数组的切片与原数据指向的是同一块数据。
# 对 slicing 数据的修改，也会修改原数据。
# list 中并不会
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"
```

使用整数和 slicing 混合索引的方式：
```
import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# 如果使用 integer 和 slicing indexing 两种方式，则矩阵的阶数就会降低
# 如果只使用 slicing indexing 则阶数不变。

row_r1 = a[1, :]    # 第二行的一阶切片
row_r2 = a[1:2, :]  # 第二行的二阶切片
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# 在列上的操作，同理:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)  # Prints "[[ 2]
                             #          [ 6]
                             #          [10]] (3, 1)"
```
## Integer array indexing

当然使用 slicing 方式得到的数组视图是原数组的一个子数组，也就是说修改 array view 是会同时修改原数组的。
integer slicing 混合的方式也是这样的。

而使用 integer 方式，得到的是一个全新的数组，是原数组的深度拷贝。
还可以使用下面这种整数数组的方式：
```
import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])

# 下面这种方式，作用相同
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"

print(a[[0, 0], [1, 1]])  # Prints "[2 2]"
print(np.array([a[0, 1], a[0, 1]]))  # Prints "[2 2]"

```
