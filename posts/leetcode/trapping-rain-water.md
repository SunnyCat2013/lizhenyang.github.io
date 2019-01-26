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

```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        res = 0
        h = height[0]
        for i in range(n):
            h = max(h, height[i])
            if h > height[i]:
                continue
            for j in range(i + 1, n):
                res = max(res, (j - i) * min(height[i], height[j]))

        return res
```

# 42. Trapping Rain Water

## Brute Force

```
# 10992 ms, faster than 0.81% of Python
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0

        res = 0
        for i in range(1, n - 1):
            left_max = height[i]
            right_max = height[i]
            for j in range(i):
                left_max = max(left_max, height[j])

            for j in range(i + 1, n):
                right_max = max(right_max, height[j])

            res += max(0, min(left_max, right_max) - height[i])

        return res
```
## Dynamic Programming

```
# 64ms, faster than 20.97%
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0

        res = 0
        left = []
        right = []
        lmax = 0
        for h in height:
            lmax = max(lmax, h)
            left.append(lmax)

        rmax = 0
        for h in height[::-1]:
            rmax = max(rmax, h)
            right.insert(0, rmax)

        for i in range(1, n - 1):
            res += max(0, min(left[i], right[i]) - height[i])

        return res
```

## Using stack, much better

```
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0

        lmax = height[0]
        stack = [height.pop(0)]

        res = 0
        for h in height:
            if h <= lmax:
                stack.append(h)
                continue
            while len(stack) > 1:
                rh = stack.pop()
                res += lmax - rh
            stack = [h]
            lmax = h

        if len(stack) < 3:
            return res

        stack = stack[::-1]

        rmax = stack.pop(0)
        for h in stack:
            res += max(0, rmax - h)
            rmax = max(rmax, h)

        return res

```
