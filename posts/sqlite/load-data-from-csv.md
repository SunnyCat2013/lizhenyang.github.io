# sqlite: 从 csv 文件中导入数据
1. 把 csv 文件导入进 sqlite，不需要手动创建新表，sqlite3 会把 csv 文件的第一行作为将要创建的表的列名。
2. sqlite3 会把从第二行开始的所有数据导入进创建的表中。

# 例子
原文给了个测试文件 [city.csv](http://www.sqlitetutorial.net/wp-content/uploads/2016/05/city.csv)。

```shell
1. 首先进入 csv 模式
sqllite> .mode csv

2. 导入 csv 文件
sqlite>.import /path/to/city.csv cities

3. 查看结果
sqlite>.shema cities
CREATE TABLE cities(
"name" TEXT,
"population" TEXT
);
```

# 参考
http://www.sqlitetutorial.net/sqlite-import-csv/
