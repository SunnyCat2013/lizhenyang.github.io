# 修改服务器默认编码

```
$ locale charmap
ANSI_X3.4-1968
```
这个导致我上传的文件都是乱码。。。

在 `/etc/profile` 中添加：
```
export LANG="zh_CN.UTF-8"  
export LC_ALL="zh_CN.UTF-8"
```
再执行一次：`source /etc/profile`。这样 `locale` 的信息就变成了 `UTF-8`。
不过使用 vim 打开文件，我发现使用（使用 `set fileencoding` 查看当前的编码）的默认编码不是 `UTF-8`。
所以在 `~/.vimrc` 中再添加一行 `set encoding=utf-8`，强制使用 `UTF-8` 编码。
# 参考
<http://www.linuxfly.org/post/424/>
