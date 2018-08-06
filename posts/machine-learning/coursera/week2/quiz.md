# https://www.coursera.org/learn/machine-learning/exam/7pytE/linear-regression-with-multiple-variables
1. feature scaling and mean normalization

```
import pandas as pd
from io import StringIO
data = u'''
89	7921	96
72	5184	74
94	8836	87
69	4761	78
'''
df = pd.read_csv(StringIO(data), sep = '\t', header = None)
print (df - df.mean()) / (df.max() - df.min())

'''
      0         1         2
0  0.32  0.305644  0.556818
1 -0.36 -0.366012 -0.443182
2  0.52  0.530184  0.147727
3 -0.48 -0.469816 -0.261364
'''
```
