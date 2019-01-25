# Trapping Water
最近遇到了几个 Trapping Water 的题，现在并不清楚它们的套路。打算系统看一下。

```
11. Container With Most Water
42. Trapping Rain Water
238. Product of Array Except Self
407. Trapping Rain Water II
```

# 11. Container With Most Water

## Brute force
> Time Limit Exceeded

```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, (j - i) * min(height[i], height[j]))

        return res
```
