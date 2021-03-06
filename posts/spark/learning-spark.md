# spark 学习笔记
> 目前对 spark 的认识停留在，它是一个基于内存的大数据计算框架，也不知道对不对。

# 写在前面
## 疑惑
1. dataframe 的操作可以代替sql?
2. 获取 dataframe 的正确方式是什么？ 我现在只会用 spark.sql 取一个 dataframe。
3. RDD 是什么？


# 读 Spark.apache.org
这个 Spark SQL、Unlike the basic Spark RDD API 是个什么鬼。。
# Spark SQL
Spark SQL 是 Spark 用于处理结构化数据的一个模块。
Spark SQL 比基础的 Spark RDD 有更多的数据和计算的信息。
与 Spark SQL 交互的方式有：SQL, DataFrame API 和 Datasets API，但是在做计算的时候，无论你使用的哪种方式，它们在 Spark SQL 里面都是用的同一种计算引擎，与你用的哪种 API 和语言没有关系。
这样，开发者可以随意用开发者自己熟悉或者方便处理业务的 API。

## SQL
Spark SQL 执行的 SQL 语句可以是基础的 SQL 语法，或者 HiveQL。
Spark SQL 还可以从现有的 Hive 中读数据。
下面这句话的前半句，不是特别明白：
> When running SQL from within another programming language the results will be returned as a DataFrame.

是说，在另外一种封装的工具中操作 SQL ，返回的就是 DataFrame。
我的理解是，没有直接执行 SQL，返回值就是一个 DataFrame 了呗。

## DataFrames
DataFrame 是用列名组织起来的分布式数据集合。这里的分布式数据是一个很重要的特征。
它与关系型数据库、R/Python 里的 data frame，但是有更多的优化操作。
DataFrame 可以由很多数据源构成，比如结构数据文件、Hive 里面的表、外部数据库和现有的 RDDs。

DataFrame API 有 Scala, Java, Python 和 R 语言的版本。

## Datasets
Dataset 是 Spark 1.6 中加入的新接口，它使用 Spark SQL 的优化引擎，把 RDD 的优势（如，存储类型、lambda 函数）引入进来。

对下面这个话也不是很明白：
>  A Dataset can be constructed from JVM objects and then manipulated using functional transformations (map, flatMap, filter, etc.).

Dataset 可以用 Java 虚拟机对象构建，然后使用函数转换函数（如，map, flatMap, filter 等）进行操作。

Dataset 提供了 Scala 和 Java 的 API。Python 还不支持 Dataset API，是因为 python 自有的动态语言特征，很多操作都可以通过 python 自身实现（如，可以通过 row.columnName 获得一行）。


# 实例
假如已有 DataFrame 对象 df。

```Python
# 选择出 name 和 age 两列，并将 age 列加 1，同时显示出来。
df.select(df['name'], df['age'] + 1).show()
```

# 常用函数
- count()
- collect()
- agg()
调用函数有哪种几种常用函数的方式？
几种方式生成的默认别名的规则？
如何修改别名？

- SparkSession.createDataFrame
从 RDD 或者 pandas.DataFrame 数据里，创建一个 DataFrame。
最近遇到一个问题，我关联几个表得到一个 DataFrame。我需要把 DataFrame 里面的数据都取出来，于是就执行了 df.collect()，然而我还需要把这个表在到 hive 里面，以备不时之需。
因为 df 是由一系列 Spark SQL 操作生成的，鉴于 DataFrame 是惰性的，所以我先用 collect 把数据取出来，再把它插回去。代码如下：
```
df = Spark.select.xxxx
data = df.collect()
tdf = spark.createDataFrame(data)
tdf.createOrReplaceTempView('tempTable')
spark.sql('create table xxx if not exist as select * from tempTable')
```
如果先保存到 hive 里面，再执行 collect，那么 Spark SQL 部分就需要计算再次，比较费时间。


## select 去重
1. select.dropDuplicates()
2. select.distinct

# 注意事项
1. 在 pyspark shell 里面运行操作的时候，默认计算资源有限。
我在  pyspark shell 里面测试的时候，就感觉比 hive shell 里面直接跑要慢上很多。
后来请教了一下同事，应该是这两个客户端配置的默认计算资源不同导致的。

2. dataframe.groupby 之后得到的是一个 GroupedData 对象。


# 学习参数
提交 pyspark 的时候，并不理解参数的含义，导致在 pyspark shell 里可以运行，而在 spark-submit 里面不能运行。



# 参考
[Spark SQL, DataFrames and Datasets Guide](https://spark.apache.org/docs/preview/sql-programming-guide.html)
[documentation](http://spark.apache.org/documentation.html)
这里提供了很多书和教程
