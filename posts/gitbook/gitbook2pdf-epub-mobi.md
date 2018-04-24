# gitbook to pdf
- install [Calibre](https://calibre-ebook.com/download)
- export ebook-convert to shell

```
echo 'export PATH=/Applications/calibre.app/Contents/MacOS/:$PATH' >> .zshrc
source ~/.zshrc
```
如果用的配置文件不是 zsh ，就换成自己的。

- check
打开命令行，看一下 `ebook-convert` 是不是能用了。

- gitbook to pdf
到 gitbook 文档根目录下

```
gitbook pdf ./ ./test.pdf
gitbook epub ./ ./test.pdf
gitbook mobi ./ ./test.pdf
```



# references
https://toolchain.gitbook.com/ebook.html
