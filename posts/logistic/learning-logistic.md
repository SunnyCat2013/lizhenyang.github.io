https://www.zybuluo.com/frank-shaw/note/143260

https://blog.csdn.net/u010270082/article/details/44819379
```
逻辑回归不像朴素贝叶斯一样需要满足条件独立假设（因为它没有求后验概率）。但每个feature的贡献是独立计算的，即LR是不会自动帮你combine 不同的features产生新feature的 (时刻不能抱有这种幻想，那是决策树,LSA, pLSA, LDA或者你自己要干的事情)。举个例子，如果你需要TF*IDF这样的feature，就必须明确的给出来，若仅仅分别给出两维 TF 和 IDF 是不够的，那样只会得到类似 a*TF + b*IDF 的结果，而不会有 c*TF*IDF 的效果。
```
