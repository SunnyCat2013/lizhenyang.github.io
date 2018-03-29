# 提交应用
> 参考 https://spark.apache.org/docs/latest/submitting-applications.html

spark-submit 可以把任务分配到 spark 集群的每台机器上。

# 打包依赖
如果你的应用依赖于其他的工程，那么这些工程应该一并提交。因为 spark-submit 需要把这些依赖一并发送到其他 spark cluster 结点上。
因为 cluster manager 已经在运行时把 Spark 和 Hadoop 提供给了各个结点，所以在打包的时候把 Spark 和 Hadoop 列为 provided dependencies 就可以了。
在使用 Python 的时候，可以使用 `--py-files` 把 Python 文件和应用一同发布。如果有多个文件的话，建议打包成 `.zip` 或者 `.egg` 文件。

# 使用 spark-submit 发布应用

