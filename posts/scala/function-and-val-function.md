# Spark UDF 在使用函数和函数变量时是不同的
```
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.udf

object test {

  def main(args: Array[String]): Unit = {
    println("test")
    val spark = SparkSession
      .builder
      .master("local")
      .appName("test")
      .getOrCreate()
    import spark.implicits._
    val dataset = Seq((0, 1, "hello"), (1, 2, "world")).toDF("molecular", "denominator", "text")

    // use udf
    //dataset.withColumn("new", $"molecular"/"denominator").show
    // 使用函数变量
    val dividor = (a: Float, b:Float) => if (b == 0) 0 else a/b
    val dividorUDF = udf[Float, Float, Float](dividor)


    // 使用函数 udf[input type, ..., output type](defined function)
    val dividorUDF = udf[Float, Float, Float](dividorF)
    // or 
    // val dividorUDF = udf(dividorF _)


    dataset.withColumn("new", dividorUDF('molecular, 'denominator)).show

  }

  def dividorF(molecular: Float, denomilar: Float): Float = {
    if (denomilar == 0)
      return 0
    else
      return molecular / denomilar
    //return denomilar === 0 ? 0 : (molecular / denomilar)
  }
}
```
