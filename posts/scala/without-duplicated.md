https://docs.databricks.com/spark/latest/faq/join-two-dataframes-duplicated-column.html

left.join(right, Seq("col1"))
col1 会被合并，但是 right 里面其它的列并不会。
所以最好

left.join(right.select("col1").distinct(), Seq("col1"))

