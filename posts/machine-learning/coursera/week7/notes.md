# 
SVM 中的 C 与 1/lambda 类似，但是，C 越大，对分错的点的惩罚越大。这样就会导致分类平面过于拟合。
通过下图可以非常直观的看出，C 太大的时候，哪怕只有少量的点与另外的类靠得比较近，分类平面也要把它分开。这是因为错分类的点的惩罚会很大（因为条数 C 很大）。
如果 C 适中，就可以有更好的适应性。
![svm-c](./svm-c.png)



# math behind large margin classification


# Kernel I
landmark? 是一个距离函数。越靠近这个点，函数值越大。自然就可以把靠近的点和远离的点分开。

1. How do we choose those landmarks/How do we get those landmarks
2. Other similiarity function 

3. SVM 与 similarity function 的关系是什么？
突然想到 similarity function 可以认为是距离函数，这样就和我之前的理解有一些共同之处了。
