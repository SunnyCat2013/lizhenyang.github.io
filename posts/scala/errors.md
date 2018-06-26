# error: value repartition is not a member of org.apache.spark.sql.RelationalGroupedDataset
这个是因为 做 group by 之后，没有调用 agg 函数。

# object apache is not a member of package org

# import org.apache.spark.sql.functions._
sum 什么的一些值
