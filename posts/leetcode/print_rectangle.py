# -*- coding: utf-8 -*-
# lizhenyang_2008@163.com
# 2018.06.01 Happy children's day~
import sys

assert (len(sys.argv) == 3), 'Wrong parmeters, right parameter format: python print_rectangle.py row col'
m = int(sys.argv[1])
n = int(sys.argv[2])

res = [[0 for ni in range(n)] for mi in range(m)]

count = 1

for r in range(m + n - 1):
    if r % 2 == 1:
        if r < m:
            i = r
            j = 0
        else:
            i = m - 1
            j = r - i

        while i >= 0 and j < n:
            res[i][j] = count
            count += 1
            i -= 1
            j += 1
    else:
        if r < n:
            j = r
            i = 0
        else:
            j = n - 1
            i = r - j
        
        while j >= 0 and i < m:
            res[i][j] = count
            count += 1
            j -= 1
            i += 1

for i in range(m):
    print(res[i])
