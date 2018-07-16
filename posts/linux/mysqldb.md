# Unable to locate package libmysqlclient-dev
https://ubuntuforums.org/showthread.php?t=1676973

```sql
apt-get install -y libmysqlclient-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
E: Unable to locate package libmysqlclient-dev
```
# 解决方法

```
apt-get update -y
apt-get install -y libmysqlclient-dev
```

