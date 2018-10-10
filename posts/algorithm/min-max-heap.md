# min heap
每个结点的值比它的子树结点的所有值都小。

[min-heap](https://upload.wikimedia.org/wikipedia/commons/5/50/Min-max_heap.jpg)

## 100w 个数中找出最大的 100 个数

1. 取前 100 个数，形成 min heap。
// 遍历 100w - 100 个数
2. 当前值与 min heap 的根结点的值；如果小于等于根结点，访问下一个值回到 2；如果大于根结点，跳到 3；
3. 调整 min 根堆。

## 复杂度

时间复杂度：
    - 最小 100*log100 +（100w - 100)  
    - 最坏 100*log100 + (100w - 100)*log100

空间复杂度： 100

# max heap
与 min heap 相反，如果要获取最小的 top k 个数，就可以用 max heap。通过遍历，获取 top k 个最小的数。
