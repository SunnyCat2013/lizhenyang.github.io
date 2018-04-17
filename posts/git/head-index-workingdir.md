# git 穿越

> 最近遇到一个问题：不小心把大文件加到了 git repo 里面，导致服务器不接收（gitlab 服务器有文件大小有限制）。我需要 reset 一下，因此借机了解一下 git 的几种『指针』。

## git checkout 
切换分支或克隆的过程也类似。 当检出一个分支时，它会修改 HEAD 指向新的分支引用，将 索引 填充为该次提交的快照，然后将 索引 的内容复制到 工作目录 中。

## git reset
- `--soft` 仅仅修改 HEAD 指针
- `--mixed` 修改 HEAD 和 Index
- `--hard` 修改 HEAD、INDEX 和 working directory

# 参考
[7.7 git 工具](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E7%BD%AE%E6%8F%AD%E5%AF%86)
