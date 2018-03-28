# 了解 range 和 xrange 的区别
今天做了个 leetcode 的题，用了 range 和 xrange，感觉在速度上 range 竟然要快一些。
因为这样单纯对比，实现是太不严谨，我觉得深入研究一下这两个实现。

在 [Built-in Functions](https://docs.python.org/2.7/library/functions.html) 找到了 range 的说明。
看了说明，了解到了下面这些有趣的用法。

```
range(start, stop[, step])

得到的 list 是：

[start, start + step, start + 2 * step, ...]

1. 如果 step 是正整数
则最大的结果是：start + i * step，且小于等于 stop。

2. 如果 step 是负整数
则最后的输出结果是：start + i * step，且大于等于 stop。
如：
>>> range(0, -10, -1)
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

3. range(0) 输出空 list []
```

# 参考
https://docs.python.org/2.7/library/functions.html
