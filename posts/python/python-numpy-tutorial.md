# 学习 python 和 numpy
>学习和使用 Python 也有几年了，期间我也写过七个月的 javascript （ES6 语法），也学习过一个多月的 Haskell。
但是，总感觉缺少一些整体的概念。
最近在学习 cs231n 公开课，趁机再来学习一下 python and numpy。
Python 是一种非常棒的多任务编程语言，在一些库（如，numpy, scipy, matplotlib）的帮助下，就可以作为一种非常强大的科学计算语言。

Python is a high-level, dynamically typed multiparadigm programming language. Python code is often said to be almost like pseudocode, since it allows you to express very powerful ideas in very few lines of code while being very readable. As an example, here is an implementation of the classic quicksort algorithm in Python:
Python 是一种高级编程语言，它有着动态的数据类型，同时它也是一种多范式编程语言。
它看起来就和伪代码一样，现实起程序来代码简洁。
下面来用 python 实现一个经典的快排算法。

```python 
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    middle_point = len(arr) // 2
    pivot = arr[middle_point]

    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [ i for i in arr if i > pivot]

    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))
```

因为 python 3.x 和 2.x 之间有很多不兼容的地方，所以我就来学习一下 3.x。下面也都用 3.x 的语法。

# Basic data types

和其它语言一样，python 有一些基本的数据类型，如，interger, floats, boolean 和 string 。
竟然还有复数类 [complex](https://docs.python.org/3.5/library/stdtypes.html#numeric-types-int-float-complex)，有时间可以再深入研究一下。
但是，它没有自增或者自减的操作。

```python
x = 3
print(type(x)) # Prints "<class 'int'>"
print(x)       # Prints "3"
print(x + 1)   # Addition; prints "4"
print(x - 1)   # Subtraction; prints "2"
print(x * 2)   # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"
y = 2.5
print(type(y)) # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2) # Prints "2.5 3.5 5.0 6.25"
```

python 中的逻辑运算使用英语单词，而不是 `|| && !` 等符号

```python
t = True
f = False
print(type(t)) # Prints "<class 'bool'>"
print(t and f) # Logical AND; prints "False"
print(t or f)  # Logical OR; prints "True"
print(not t)   # Logical NOT; prints "False"
print(t != f)  # Logical XOR; prints "True"
```
python 对 string 有着极好的支持

```python
hello = 'hello'    # 单双引号，都可以来表示字符串
world = "world"    # 
print(hello)       # Prints "hello"
print(len(hello))  # 获取字符串长度 prints "5"
hw = hello + ' ' + world  # 字符串拼接
print(hw)  # prints "hello world"
hw12 = '%s %s %d' % (hello, world, 12)  # 字符串定制
print(hw12)  # prints "hello world 12"

s = "hello"
print(s.capitalize())  # 大字首字母; prints "Hello"
print(s.upper())       # 字符串转成大字; prints "HELLO"
print(s.rjust(7))      # 右对齐，并用空格填充; prints "  hello"
print(s.center(7))     # 中间对齐，用空格填充; prints " hello "
print(s.replace('l', '(ell)'))  # 字符串替换;
                                # prints "he(ell)(ell)o"
print('  world '.strip())  # 剔除首尾指定字符，默认是空格; prints "world"
```
更多 string 内建函数参见 [String Methods](https://docs.python.org/3.5/library/stdtypes.html#string-methods)

# Containers
Python 自带了几种 Container：lists, dictionaries, sets 和  tuples。
## List
A list is the Python equivalent of an array, but is resizeable and can contain elements of different types:

list 是 python 中的 array，但是，list 却是大小可变、元素类型可以不同。
但是 list 和 array 还是有很多区别的，在深层操作元素时，一定要慎重。

```
xs = [3, 1, 2]    # 初始化 list 
print(xs, xs[2])  # Prints "[3, 1, 2] 2"
print(xs[-1])     # 打印最后一个元素; prints "2"
xs[2] = 'foo'     # 给最后一个元素赋值
print(xs)         # Prints "[3, 1, 'foo']"
xs.append('bar')  # 在 list 尾部添加一个元素
print(xs)         # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()      # 把 list 元素的头部元素『吐』出来，并作为返回值。这个一定要注意，哪些函数是有返回值的，哪些是没有返回值的。
print(x, xs)      # Prints "bar [3, 1, 'foo']"
```
更多参考 [more-on-list](https://docs.python.org/3.5/tutorial/datastructures.html#more-on-lists)
*Slicing* 在 python 中，有一种获取子列表简洁的语法，被称为 slicing。

```
nums = list(range(5))     # 初始化
print(nums)               # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])          # 获取数据 2 到 4 （不包括下标为 4 的元素）; prints "[2, 3]"
print(nums[2:])           # 从下标为 2 的元素开始读数据; prints "[2, 3, 4]"
print(nums[:2])           # 获取前两个元素 (下标为 2 的元素并不在获取之列); prints "[0, 1]"
print(nums[:])            # 获取所有数据; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])          # 使用负数作为下标; prints "[0, 1, 2, 3]"
nums[2:4] = [8, 9]        # 子列表赋值
print(nums)               # Prints "[0, 1, 8, 9, 4]"

还有一些更有意思的用法：
In [2]: n = list(range(5))

In [3]: n
Out[3]: [0, 1, 2, 3, 4]

In [4]: n[::-1]
Out[4]: [4, 3, 2, 1, 0]

In [5]: n[::-2]
Out[5]: [4, 2, 0]

In [6]: n[::-3]
Out[6]: [4, 1]
```
## Loop
python 里面的元素遍历是非常方便的：
```
animals = ['cat', 'dog', 'monkey']
for animal in animals:
        print(animal)
# Prints "cat", "dog", "monkey", each on its own line.
```
如果想获取元素的下标
```
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
        print('#%d: %s' % (idx + 1, animal))
# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line
```

*List comprehension*列表解析

如果我们需要做类似函数式编程里面的 map 操作，我们可以
```
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
        squares.append(x ** 2)
        print(squares)   # Prints [0, 1, 4, 9, 16]
```

当然也可以
```
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)   # Prints [0, 1, 4, 9, 16]
```
这种方式就被称为列表解析（list comprehension）
列表解析中也可以加入条件判断
```
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # Prints "[0, 4, 16]"
```

## Dictionary
类似于 java 中的 map，python 中的 dictionary 有相似的用法

```
d = {'cat': 'cute', 'dog': 'furry'}  # 初始化字典
print(d['cat'])       # 获取 key 是 'cat' 的值; prints "cute"
print('cat' in d)     # 判断字典中是否包含关键字; prints "True"
d['fish'] = 'wet'     # 在字典中创建一个新条目
print(d['fish'])      # Prints "wet"
# print(d['monkey'])  # 如果试图获取一个在字典中的关键字，那么就会报 KeyError
print(d.get('monkey', 'N/A'))  # 当一个 key 还存在时，给一个默认值; prints "N/A"
print(d.get('fish', 'N/A'))    # prints "wet"
del d['fish']         # 删除一个 key 
print(d.get('fish', 'N/A')) # prints "N/A"
```
更多参考 [dict](https://docs.python.org/3.5/library/stdtypes.html#dict)

我们可以方便地迭代字典中的 key
```
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
        legs = d[animal]
            print('A %s has %d legs' % (animal, legs))
# Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"
```

我们可以同时使用 key 和 value
```
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
        print('A %s has %d legs' % (animal, legs))
# Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"
```

与 list comprehension 一样，我们可以使用
```
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)  # Prints "{0: 0, 2: 4, 4: 16}"
```

## Set
Set 与 List 类似，但是它 *无序* 且 *不重复*。
```
animals = {'cat', 'dog'}
print('cat' in animals)   # 判断一个元素是不是在 set 里; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')       # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))       # Number of elements in a set; prints "3"
animals.add('cat')        # Adding an element that is already in the set does nothing
print(len(animals))       # Prints "3"
animals.remove('cat')     # Remove an element from a set
print(len(animals))       # Prints "2"
```
