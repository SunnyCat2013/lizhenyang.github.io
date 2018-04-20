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
