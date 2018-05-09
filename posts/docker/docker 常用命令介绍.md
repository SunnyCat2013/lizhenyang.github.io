# docker 常用命令介绍
下面是最近常用的 docker 命令
## 获取 image
`docker pull image_name:image_version`

## 运行 image
image 运行之后，就会产生一个 container。
运行并在 container 中进行操作 `docker run -it --name your_name image_name` or 后台运行 `docker run -d --name your_name image_name`

## 保存 image
`docker image save -o target_name.tar image_name:version`

## 从文件中加载 image
`docker load -i target_name.tar`

## 将当前的 container 保存成 image
`docker commit -m "commit message" container image_name:image_version`

## 从 Dockerfile 中打包 image
`docker build -t image_name:image_version .` Dockerfile 放在本目录下。

## 重命名 image
因为在 load image 之后，没有指定 image name 和 version，需要用 tag 指定一下。
`docker tag image_id image_name:version`

## 使用 docker 执行某个文件
docker run -d --rm --name some_name -w work_dir_in_container -v /path/to/local/dir:work_dir_in_container image:version bash run.sh parameters

## 在“隐身”状态下使用 docker image 中的工具

```
From docker
NOTE: This is just a tiny taste to let you feel that leetcode-cli is. Please use other ways above to install leetcode-cli if you like it.

$ alias leetcode='docker run -it --rm skygragon/leetcode-cli'
$ leetcode version
To persistent user data, you can mount a folder like this:

$ alias leetcode='docker run -it --rm -v /Users/skygragon/data:/root skygragon/leetcode-cli'
```
