# 对多个 pandas dataframe 进行 join
貌似没有对多个 dataframe 进行 join 的方法，比较笨的就是手动挨个 join。
今天学习到一个新的方法，使用 functools.reduce 方法。我之前还纳闷，python 这样一种 functional programming 的语言，怎么会没有 map/reduce/filter。原来 python3 把这几个函数放在 functools 里面了。。。

```
import pandas as pd
dfs = [df0, df1, df2, dfN]
from functools import reduce
df_final = reduce(lambda left,right: pd.merge(left,right,on='name'), dfs)
```



# Reference
https://stackoverflow.com/questions/23668427/pandas-joining-multiple-dataframes-on-columns
