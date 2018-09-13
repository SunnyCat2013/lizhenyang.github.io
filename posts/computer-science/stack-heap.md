# 栈和堆的区别
栈 (stack) 是静态分配的。

条目 | Stack(栈) | Heap(堆)
----|----|----
内存分配方式 |静态（编译时）分配，直接分配到内存。读取速度快。|
时刻|编译|程序运行的任意时刻
位置|内存|虚拟内存
速度|快|慢
回收方式|LIFO，最近访问的，最先被释放掉|与生成顺序无关，可以随机读取、释放
回收成本|低，移动一个指针|高

# 使用
- stack, 如果在编译之前就知道要用多少空间，并且所用空间并不是太多。
- heap, 如果运行之前不知道要用多少，并且要用的空间应该比较多的时候。

# 多线程
- stack 线程独享，每个线程分配
- heap 线程之间可以共享


下面这句话不是特别明白。
> The stack is important to consider in exception handling and thread executions.



# 参考

http://net-informations.com/faq/net/stack-heap.htm
