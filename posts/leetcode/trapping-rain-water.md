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

改进一点，去掉无用的 heights。

https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQW2RfZQV9XTx0XqDPk2AEVCqvtOvuCSeS6-FMKQcE9FZ6TdIUuew

```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        res = 0
        forward = [0]

        for i in range(1, n):
            if height[i] > height[forward[-1]]:
                forward.append(i)

        backward = [n - 1]
        for i in range(n - 2, -1, -1):
            if height[i] > height[backward[0]]:
                backward.insert(0, i)

        for i in forward:
            for j in backward:
                if i < j:
                    res = max(res, (j - i) * min(height[i], height[j]))

        return res
```

## Two pointer
昨天回家，在梦里想到了这个的 O(n) 解法，感觉好神奇。。。

```
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        res = 0

        left = 0
        right = n - 1

        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

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
# 28 ms, faster than 82.26%
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

# 238. Product of Array Except Self

```
# O(n)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        backward = [nums[-1]]
        for i in range(n - 2, -1, -1):
            backward.insert(0, nums[i] * backward[0])

        res = [backward[1]]

        pre = nums[0]
        for i in range(1, n - 1):
            res.append(pre * backward[i + 1])
            pre *= nums[i]

        res.append(pre)

        return res
```
