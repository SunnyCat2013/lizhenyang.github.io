# 共享内存超出机器使用限制
最近在使用 `torch.utils.data.dataloader` 时，出现了一个共享内存的问题。

```
Traceback (most recent call last):
  File "trainbatch.py", line 40, in <module>
    for X,Y in train_loader:
  File "/usr/local/lib/python2.7/dist-packages/torch/utils/data/dataloader.py", line 204, in __next__
    idx, batch = self.data_queue.get()
  File "/usr/lib/python2.7/multiprocessing/queues.py", line 378, in get
    return recv()
  File "/usr/local/lib/python2.7/dist-packages/torch/multiprocessing/queue.py", line 22, in recv
    return pickle.loads(buf)
  File "/usr/lib/python2.7/pickle.py", line 1388, in loads
    return Unpickler(file).load()
  File "/usr/lib/python2.7/pickle.py", line 864, in load
    dispatch[key](self)
  File "/usr/lib/python2.7/pickle.py", line 1139, in load_reduce
    value = func(*args)
  File "/usr/local/lib/python2.7/dist-packages/torch/multiprocessing/reductions.py", line 68, in rebuild_storage_fd
    fd = multiprocessing.reduction.rebuild_handle(df)
  File "/usr/lib/python2.7/multiprocessing/reduction.py", line 155, in rebuild_handle
    conn = Client(address, authkey=current_process().authkey)
  File "/usr/lib/python2.7/multiprocessing/connection.py", line 169, in Client
    c = SocketClient(address)
  File "/usr/lib/python2.7/multiprocessing/connection.py", line 308, in SocketClient
    s.connect(address)
  File "/usr/lib/python2.7/socket.py", line 228, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 111] Connection refused
```


在 [这个](http://noahsnail.com/2018/01/15/2018-01-15-PyTorch%20socket.error%20[Errno%20111]%20Connection%20refused/) 文章里面说是共享内存的问题。我就简单看了一下共享内存：`df -h /dev/shm/`。我现在的共享内存大约是 `64M`，好像不太够。


```
shm                                                                                               64M     0   64M   0% /dev/shm
```


就手动调整了一下。

```
mount tmpfs /some/path/to/mount -t tmpfs -o size=16G
```

文件类型和挂载点应该不太一样，我还没有试。


torch 里面的 shared memory 的参考应该可以在 [test_sharedmem.lua](https://github.com/torch/torch7/blob/master/test/test_sharedmem.lua) 找到。
## 共享内存

共享内存就是允许两个不相关的进程访问同一个逻辑内存。共享内存是在两个正在运行的进程之间共享和传递数据的一种非常有效的方式。不同进程之间共享的内存通常安排为同一段物理内存。进程可以将同一段共享内存连接到它们自己的地址空间中，所有进程都可以访问共享内存中的地址，就好像它们是由用C语言函数malloc分配的内存一样。而如果某个进程向共享内存写入数据，所做的改动将立即影响到可以访问同一段共享内存的任何其他进程。


# 参考

[yTorch socket.error](http://noahsnail.com/2018/01/15/2018-01-15-PyTorch%20socket.error%20[Errno%20111]%20Connection%20refused/)

[Linux - Shared Memory (SHM)(/dev/shm)](https://gerardnico.com/linux/shared_memory)
[shared memory](http://blog.csdn.net/ljianhui/article/details/10253345)
