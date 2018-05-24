# git 穿越

> 最近遇到一个问题：不小心把大文件加到了 git repo 里面，导致服务器不接收（gitlab 服务器有文件大小有限制）。我需要 reset 一下，因此借机了解一下 git 的几种『指针』。

## git checkout 
切换分支或克隆的过程也类似。 当检出一个分支时，它会修改 HEAD 指向新的分支引用，将 索引 填充为该次提交的快照，然后将 索引 的内容复制到 工作目录 中。

## git reset
- `--soft` 仅仅修改 HEAD 指针
这个其实还是比较好理解的，如果是默认 `--soft` ，我们的 work copy 文件并不会改变，只需要重新把这些文件加到 repo 里面就可以了（就是重新 git add/commit 就可以了）。
- `--mixed` 修改 HEAD 和 Index
如果添加了大文件，则需要同时修改 Index 中的数据，让它和 HEAD 一起回到添加大文件之前的某个结点。同样不用担心现在的文件发生改变。
- `--hard` 修改 HEAD、INDEX 和 working directory
这个就要小心了，它是会把当前的文件恢复到某个历史结点的。



# 参考
[7.7 git 工具](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E7%BD%AE%E6%8F%AD%E5%AF%86)
