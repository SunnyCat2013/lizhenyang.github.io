# 提交应用
> 参考 https://spark.apache.org/docs/latest/submitting-applications.html

spark-submit 可以把任务分配到 spark 集群的每台机器上。

# 打包依赖
如果你的应用依赖于其他的工程，那么这些工程应该一并提交。因为 spark-submit 需要把这些依赖一并发送到其他 spark cluster 结点上。
因为 cluster manager 已经在运行时把 Spark 和 Hadoop 提供给了各个结点，所以在打包的时候把 Spark 和 Hadoop 列为 provided dependencies 就可以了。
在使用 Python 的时候，可以使用 `--py-files` 把 Python 文件和应用一同发布。如果有多个文件的话，建议打包成 `.zip` 或者 `.egg` 文件。

# 使用 spark-submit 发布应用
`spark-submit` 可以用来提交 spark 任务，管理类路径和依赖。并支持 spark 的多种结点管理模式。

```
./bin/spark-submit \
  --class <main-class> \
  --master <master-url> \
  --deploy-mode <deploy-mode> \
  --conf <key>=<value> \
  ... # other options
  <application-jar> \
  [application-arguments]

```
一些比较常用的选项如下：
 - `--class`： 应用入口（如，`org.apache.spark.examples.SparkPi`）
 - `--master`：spark 集群的 master URL 
 - `--deploy-mode`： client 模式还是 cluster 模型。
 - `--conf`：任意的 spark 配置，用 `key=value` 这样的形式。如果 value 中包含空格，则用 qoutes 把键值对包含起来：`"key=value"`
 - `application-jar`： 应用打包文件的路径
 - `application-arguments`：传给主函数的参数

