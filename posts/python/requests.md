# requests
> 最近想架一个服务器，接收 http://name.xx/key=xx?value=xx 这种请求，并得到参数。现在还不知道改用哪个包，先了解一下 requests。

# HTTP 及 POST/GET/PUT/DELETE 的区别
> HTTP(Hyper Text Transfer Protocol)，是从服务器到浏览器传输 Hyper Text 的协议。
## get 安全且幂等
1. 只获取信息，不修改信息
2. 幂等意味着，多次请求，得到的结果是相同的。

例如，用户请求新闻主页内容。

## post 可能会修改服务器上的资源
例如，用户发表自己对新闻的评论。

## 参考
https://www.jianshu.com/p/80e25cb1d81a
https://www.cnblogs.com/hyddd/archive/2009/03/31/1426026.html
# 参考
[Requests: HTTP for Humans](http://docs.python-requests.org/en/master/)

