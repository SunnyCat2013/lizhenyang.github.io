# -*- coding: utf-8 -*-

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    middle_point = len(arr) // 2
    pivot = arr[middle_point]

    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [ i for i in arr if i > pivot]

    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))
