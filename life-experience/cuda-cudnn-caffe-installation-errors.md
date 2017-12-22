> 最近在安装 CUDA/CUDNN/CAFFE，简直是呕心沥血、可歌可泣，说多了都是泪。其主要原因是，这几个库和本机的多种软硬件环境的差异造成的。我觉得在这个过程中，我收获最多的就是我的耐心得到了极大的锻炼[doge]。
![doge](http://i0.kym-cdn.com/entries/icons/mobile/000/013/564/doge.jpg)

# 安装过程中遇到的问题
## ImportError: libcublas.so.8.0: cannot open shared object file: No such file or directory
我选择在线安装 [`cuda 8.0`](https://developer.nvidia.com/cuda-80-ga2-download-archive) 。但是，这样安装下来，竟然安装的是 `libcublas 9.0`。后面只能用 `deb(local)` 的模式安装。
目前还不明白为什么。

![cuda](./cuda.png)