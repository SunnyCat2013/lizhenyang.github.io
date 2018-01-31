# [learn scala in y minutes](https://learnxinyminutes.com/docs/scala/)
# 基本操作
基本操作没有什么多说的，随便看看。

# String
```
drop 
丢掉

take
拿出来

// String interpolation: notice the prefix "s"
val n = 45
s"We have $n apples" // => "We have 45 apples"



// Formatting with interpolated strings with the prefix "f"
f"Power of 5: ${math.pow(5, 2)}%1.0f"         // "Power of 5: 25"
f"Square root of 122: ${math.sqrt(122)}%1.4f" // "Square root of 122: 11.0454"


```

# Functions

```
// If you come from more traditional languages, notice the omission of the
// return keyword. In Scala, the last expression in the function block is the
// return value.
def sumOfSquares(x: Int, y: Int): Int = {
  val x2 = x * x
  val y2 = y * y
  x2 + y2
}

```
Scala 中不需要返回词的关键字 `return`，而是把最后一个结果作为返回值。


```
// You can use parameters names to specify them in different order
def subtract(x: Int, y: Int): Int = x - y

subtract(10, 3)     // => 7
subtract(y=10, x=3) // => -7
```
函数可以通过参数名来赋值。

```
ef sq(x: Int) = x * x  // Compiler can guess return type is Int
```
推导返回值。

```
// Functions can have default parameters:
def addWithDefault(x: Int, y: Int = 5) = x + y
addWithDefault(1, 2) // => 3
addWithDefault(1)    // => 6
```
设置默认参数类型。
