# 数据类型
# Datatypes In SQLite
Sqlite 里面的数据类型是动态类型的系统。
> 是不是可以理解成每个值都可以有自己的数据类型，哪怕同一列的数据也可以有不同的数据类型？
# Storage Classes and Datatypes
Sqlite 里面存储的数据，属于以下几种类型中的一种：

- NULL: NULL 类型
- INTEGER: 整数类型，根据数据的量级存放数据的存储大小可以是 1, 2, 3, 4, 6 或者 8 个字节。
- REAL: 8 字节浮点数据类型。
- TEXT: 文本字符串，格式有，UTF-8, UTF-16BE, UTF-16LE。
- BLOB: 数据是什么就保存成什么类型。

# 参考
[Datatypes In SQLite Version 3](https://www.sqlite.org/datatype3.html)

