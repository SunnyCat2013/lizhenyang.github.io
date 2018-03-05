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
就手动调整了一下。


# 参考

[yTorch socket.error](http://noahsnail.com/2018/01/15/2018-01-15-PyTorch%20socket.error%20[Errno%20111]%20Connection%20refused/)

[Linux - Shared Memory (SHM)(/dev/shm)](https://gerardnico.com/linux/shared_memory)
