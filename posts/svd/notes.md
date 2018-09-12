https://www.cnblogs.com/pinard/p/6251584.html

# 为什么奇异值越大，这个维度保留的信息量越多？
应该反过来说，维度的信息越多，奇异值越大。

举个例子。

一个数据集沿向量 (2, 1) 上下浮动。
那么从 y 轴水平看到的点的数量，可以就比沿 x 轴竖直看到的少。（因为重叠的缘故）


如果保留一个维度，那么一定要保留 x (eigenvalue is more big)
如果能还原回去，x 的信息（点的数量，点的间距信息）也更多。


# Implementation of SVD

https://jeremykun.com/2016/05/16/singular-value-decomposition-part-2-theorem-proof-algorithm/

https://jeremykun.com/2016/05/16/singular-value-decomposition-part-2-theorem-proof-algorithm/

http://www.cs.utexas.edu/users/inderjit/public_papers/HLA_SVD.pdf

https://blog.statsbot.co/singular-value-decomposition-tutorial-52c695315254

https://github.com/j2kun/svd

http://www-users.math.umn.edu/~lerman/math5467/svd.pdf
