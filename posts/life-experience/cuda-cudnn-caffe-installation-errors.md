> 最近在安装 CUDA/CUDNN/CAFFE，简直是呕心沥血、可歌可泣，说多了都是泪。其主要原因是，这几个库和本机的多种软硬件环境的差异造成的。我觉得在这个过程中，我收获最多的就是我的耐心得到了极大的锻炼[doge]。
![doge](http://i0.kym-cdn.com/entries/icons/mobile/000/013/564/doge.jpg)

# 安装过程中遇到的问题
## ImportError: libcublas.so.8.0: cannot open shared object file: No such file or directory
我选择在线安装 [`cuda 8.0`](https://developer.nvidia.com/cuda-80-ga2-download-archive) 。但是，这样安装下来，竟然安装的是 `libcublas 9.0`。后面只能用 `deb(local)` 的模式安装。
目前还不明白为什么。

![cuda](./cuda.png)


## protoc: Command not found
这个需要安装一下 [`protobuf`](https://github.com/google/protobuf)
```Shell
sudo apt-get install protobuf-c-compiler protobuf-compiler
```
## ./include/caffe/util/mkl_alternate.hpp:14:19: fatal error: cblas.h: No such file or directory

```
sudo apt-get install libblas-dev
```

## cannot find -lcblas & -latlas
```
/usr/bin/ld: cannot find -lcblas
/usr/bin/ld: cannot find -latlas
```
解决方法
```
sudo apt-get install libatlas-base-dev
```

## hdf5.h: No such file or directory
```
# in Makefile.config
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/
```

## Makefile:625: recipe for target '.build_release/tools/compute_image_mean.bin' failed
出现这个问题是在使用 `OpenCV` 相关库的时候出错了，可能是没找到。只需使 `Makefile.config` 里面的 `USE_PKG_CONFIG := 1`，然后再编译一遍。

## cudnn 版本太旧
这个的错误提示比较多，像什么 `too few xxx`、`CUDNN XXX` 都可以考虑一下这个原因。
把当前 `cudnn` 安装目录下的文件和最新版本的目录保持一致就地。

一个博主的解决方法 [原地址](http://blog.csdn.net/alickr/article/details/78512405)：
```
下载最新版本的caffe，将旧版caffe里的几个文件替换成最新版里面的
caffe-fast-rcnn/include/caffe/util/cudnn.hpp  
caffe-fast-rcnn/include/caffe/layers/下面cudnn_开头的所有文件
caffe-fast-rcnn/src/caffe/util/cudnn.cpp
caffe-fast-rcnn/src/caffe/layers/ 下面cudnn_开头的所有文件
提示：要将旧代码从文件夹里面移除，不能只改名字做备份，否则依旧有错误提示
```

# 注意事项
- 安装 `tensorflw` 时，需要一些库可能会与 `caffe` 的库起冲突，所以要先安装 `caffe` 再安装 `tensorflow`。
- `OpenCV` 在安装的过程中，会检查本机中相关的 `cuda` 等库，所以要先安装 `cuda` 再安装 `OpenCV`。
- 不同库的安装顺序*很重要*
- 如果在编译 `caffe` 时候出错了，最好 `make clean` 之后再编译一次。
- 安装 `caffe` 和使用 `pycaffe` 的时候，要安装两个 `protobuf`。注意这两个 `protobuf` 的版本可能导致安装时出错。