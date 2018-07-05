# 配置
> 最近打算学习一下这个课
> 之前用过一段时间 Google Cloud，现在打算在这个课程里接着用。

- 按照 [gce-tutorial](http://cs231n.github.io/gce-tutorial/) 里面的介绍，开户、启动服务器。

下面做：Connect to Your Virtual Instance
- Install the latest Cloud Tools 
- 设置特定的时区 `us-west1-b`

# First time setup
开始第一次使用 gce。

# Using Jupyter Notebook with Google Compute Engine
Interesting!

# Submission: Transferring Files From Your Instance To Your Computer

# Start!

```
gcloud compute ssh --zone=us-west1-b cs231-vm
/home/shared/setup.sh && source ~/.bashrc

cd /home/shared
jupyter-notebook --no-browser --port=7000

注意更换前缀
http://35.197.80.166:7000/
```
