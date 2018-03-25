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


# 参考
[Spark SQL, DataFrames and Datasets Guide](https://spark.apache.org/docs/preview/sql-programming-guide.html)
