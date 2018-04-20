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



