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

选择和修改列
```
import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

print(a)  # prints "array([[ 1,  2,  3],
#                [ 4,  5,  6],
#                [ 7,  8,  9],
#                [10, 11, 12]])"

b = np.array([0, 2, 0, 1])

# 使用 b 选择每一行的某一列
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

# 修改列
a[np.arange(4), b] += 10

print(a)  # prints "array([[11,  2,  3],
#                [ 4,  5, 16],
#                [17,  8,  9],
#                [10, 21, 12]])
```

## Boolean array indexing
使用这种方式，可以在一个数组中选出符合某一条件的元素

```
import numpy as np

a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)   # 找出大于 2 的元素;
                     # 这个操作返回一个与 a 具有相同 shape 的一个 boolean 数组
                     # 这个数组中的每个元素，代表了这个元素是不是大于 2

print(bool_idx)      # Prints "[[False False]
                     #          [ True  True]
                     #          [ True  True]]"

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print(a[a > 2])     # Prints "[3 4 5 6]"
```
更多参考 [indexing](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html)

## Datatype

每个 numpy 数组，都是一组相同数据类型的数据。
numpy 给出大量的数据类型，可以用来构建数组。
在构建数组的时候，可以指明数据类型。
numpy 也会自己去『猜』给定数据的类型。
```
import numpy as np

x = np.array([1, 2])   # numpy 自己去猜数据类型
print(x.dtype)         # Prints "int64"

x = np.array([1.0, 2.0])  
print(x.dtype)             # Prints "float64"

x = np.array([1, 2], dtype=np.int64)   # 指定数据类型
print(x.dtype)                         # Prints "int64"
```
更多数据类型 [arrays.datatypes](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)

# Array math
基本的数据运算，按元素进行计算。
并且，运算重载符和函数都可以完成这种运算。

```
# 按元素加、减、乘、除及开方。
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))
```

与 MATLAB 中的矩阵简洁 `*` 不同，numpy 中的 `*` 是按元素相乘的。
在 python 中的矩阵乘法是 `dot`。
`dot` 在 numpy 模块和 array 对象中都有。

```
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# v w 的内积
print(v.dot(w))
print(np.dot(v, w))

# 矩阵和向量的乘积
print(x.dot(v))
print(np.dot(x, v))

# 矩阵和矩阵的乘积。
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
```

numpy 也提供了一些有用的函数，如 sum

```
import numpy as np

x = np.array([[1,2],[3,4]])

print(np.sum(x))  # 计算所有元素的和; prints "10"
print(np.sum(x, axis=0))  # 计算每列的和; prints "[4 6]"
print(np.sum(x, axis=1))  # 计算每行的和; prints "[3 7]"
```
怎么理解 `axis = 0` 呢？是按行的方向增长，于是就是列的和。
更多数学函数 [routines.math](https://docs.scipy.org/doc/numpy/reference/routines.math.html)

有时候，我们可能还需要改变一下 array 中元素的位置，如 reshape 或者 transpose。
```
import numpy as np

x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# 对于秩为 1 的数组，不改变任何事情。
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"
```
更多参考 [routines.arry-manipulation](https://docs.scipy.org/doc/numpy/reference/routines.array-manipulation.html)

# Broadcasting
Broadcasting 这个机制可以对不同 shape 的数组之间按照某种补全逻辑进行一些操作，这个机制我之间倒也没有用过。
如，我有个 (n,) 大小的数组 a 和一个 (m, n) 大小的数组 b，我想得到数组 c，而其中 c 的每行是 a 和 b 的每行的加和。
如果没有 broadcasting 机制，我们可以这样做：
```
import numpy as np

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # y 随机生成数据

for i in range(4):
        y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)
```

然而这种方式，需要显示的进行一次遍历操作，可能会比较慢，我们可以通过复制的方式来代替这种方式。

```
import numpy as np

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))   # 拷贝 4 份 v 
print(vv)                 # Prints "[[1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]]"
y = x + vv  
print(y)  # Prints "[[ 2  2  4
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"
```

而 broadcasting 方式，便可以隐式地完成这种方式。

```
import numpy as np

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v   
print(y)  # Prints "[[ 2  2  4]
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"

```

这种方式把 (3,) 大小的数组当 (4, 3) 大小的数组来用。
x 的每行都与 v 进行按元素进行加和。

--------------------------------------------- 待补充 ---------------------------------------
两个数组的 broadcasting 机制的原则如下：
- 
