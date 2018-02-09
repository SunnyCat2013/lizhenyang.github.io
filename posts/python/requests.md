# requests
> 最近想架一个服务器，接收 http://name.xx/key=xx?value=xx 这种请求，并得到参数。现在还不知道改用哪个包，先了解一下 requests。

# HTTP 及 POST/GET/PUT/DELETE 的区别
> HTTP(Hyper Text Transfer Protocol)，是从服务器到浏览器传输 Hyper Text 的协议。
## get 安全且幂等
例如，用户请求新闻主页内容。

1. 只获取信息，不修改信息
2. 幂等意味着，多次请求，得到的结果是相同的。

### 请求格式
GET请求的数据会附在URL之后（就是把数据放置在HTTP协议头中），以?分割URL和传输数据，参数之间以&相连，如：login.action?name=hyddd&password=idontknow&verify=%E4%BD%A0%E5%A5%BD。如果数据是英文字母/数字，原样发送，如果是空格，转换为+，如果是中文/其他字符，则直接把字符串用BASE64加密，得出如：%E4%BD%A0%E5%A5%BD，其中％XX中的XX为该符号以16进制表示的ASCII。

### 数据大小
GET方式提交的数据最多只能是1024字节


## post 可能会修改服务器上的资源
例如，用户发表自己对新闻的评论。

### 请求格式 
POST把提交的数据则放置在是HTTP包的包体中。
### 数据大小
理论上POST没有限制，可传较大量的数据，IIS4中最大为80KB，IIS5中为100KB。

## 参考
https://www.jianshu.com/p/80e25cb1d81a
https://www.cnblogs.com/hyddd/archive/2009/03/31/1426026.html


# requests 用法
> 简单了解了 HTTP 及 get/post 之后，我觉得我可能了解错方向了。requests 应该是发出信息的一方，而我想要的是接收数据的一方。
## 测试网站
[http://httpbin.org/](http://httpbin.org/)

```
import requests 
# 发送一个 get 请求，但是这个用作样例的 url 可能会变。
r = requests.get('http://git.io/17AROg')
r.status_code # 200

# put/delete/head/options 实例
>>> r = requests.put("http://httpbin.org/put")
>>> r = requests.delete("http://httpbin.org/delete")
>>> r = requests.head("http://httpbin.org/get")
>>> r = requests.options("http://httpbin.org/get")

```

## URL 传递参数

用字典的方式确实非常人性化。
```
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get("http://httpbin.org/get", params=payload)
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2
```


# 参考
[Requests: HTTP for Humans](http://docs.python-requests.org/en/master/)
[快速上手](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)
