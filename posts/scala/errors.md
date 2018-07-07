# error: value repartition is not a member of org.apache.spark.sql.RelationalGroupedDataset
这个是因为 做 group by 之后，没有调用 agg 函数。

# object apache is not a member of package org

# import org.apache.spark.sql.functions._
sum 什么的一些值


# 是因为 用 大表 join 小表了？
18/07/03 10:04:39 ERROR TransportRequestHandler: Error sending result RpcResponse{requestId=8459265240292359228, body=NioManagedBuffer{buf=java.nio.HeapByteBuffer[pos=0 lim=4073 cap=5600]}} to /172.21.82.43:8730; closing connection
java.nio.channels.ClosedChannelException
