# Rolling Hash
最近在做 leetcode rotate string 的时候，遇到了一个新知识点 ---- Rolling Hash，学习一下。
> A rolling hash (also known as recursive hashing or rolling checksum) is a hash function where the input is hashed in a window that moves through the input.

这句话，很符合 rotate string 这个题的直觉。
因为 string 只是平移了，它们字符之间的相对位置，只是发生了平移。用循环的相对关系来看，字母之前的前后字母并没有发生改变。

如果我们有一种映射，可以忽略这种平移，那么就可以判断两个 string 是不是 rotate string 了。

[(你可以想象成，找了一个长度为L的框，框住了S，每迭代一次向前移动一位，所以会移动n次，而对于每次每个框中的子串都需要迭代这个子串来算哈希值，所以复杂度为nL)。然而你可以看到这些子串中很多字符都是重复的。](https://blog.csdn.net/yanghua_kobe/article/details/8914970)
也就是说，移动一次，原先需要 L 次比较，现在只需要再次计算了（我猜应该是两次，掐头加尾）

# 我理解中的实现




# 参考
https://en.wikipedia.org/wiki/Rolling_hash
https://blog.csdn.net/yanghua_kobe/article/details/8914970
