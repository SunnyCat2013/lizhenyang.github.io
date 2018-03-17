# 从实例入手学习 svg
我发现我有很强的强迫症。。如果我在做一项工作的时候，我不能完全理解这件事情里面的每个东西，我会非常难受。
正如我想写一个通过经纬度和距离算另外一个点的经纬度的库的时候，我就想知道 [haversine](https://en.wikipedia.org/wiki/Haversine_formula)

# 知识预览

[w3school](http://www.w3school.com.cn/svg/index.asp) 的教程看起来很短，知用它补充一点基础知识。

## 基本图形
SVG 的形状元素：

```
矩形 <rect>
圆形 <circle>
椭圆 <ellipse>
线 <line>
折线 <polyline>
多边形 <polygon>
路径 <path>
```

如圆：![circle](./circle.svg)

```
<svg with="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
        <circle fill="white" cx="100" cy="50" r="40" stroke="black" stroke-width="2"/>
</svg>

```

> path 非常强大。

下面还介绍了一些特效，实在没什么兴趣，先不看了。

# 画 haversine 问题图
我想解决的问题在 [问题讨论](https://sunnycat2013.gitbooks.io/blogs/content/posts/haversine/haversine-formula.html) 中。

[原图](https://upload.wikimedia.org/wikipedia/commons/c/cb/Illustration_of_great-circle_distance.svg)

[-] 改大写 P、Q 为小写
[-] 连接 u、v
[-] 画出球心
[-] 连接 op, oq
[ ] 添加过 p 的纬度线
[ ] 添加过 q 的经度线


> 周末在公司学习好爽啊。。安静又舒坦。。
