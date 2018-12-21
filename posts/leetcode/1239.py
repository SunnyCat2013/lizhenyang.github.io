# -*- coding: utf-8 -*-
def solution(data):
    imax = 0
    #print data
    
    lmax = max(data, key = lambda x: x[1])[1] + 1
    table = [False] * (lmax + 1)
    
    table[0] = True
    data.sort(cmp = lambda a, b: a[1] - b[1])
    # print 'data', data
    
    for h, a, c in data:
        new_table = [False] * (lmax + 1)
        for i in range(min(imax + 1, a + 1 - h)):
            if table[i]:
                for j in range(1, c + 1): # 把从当前 table[i] 的所有可能的下一个点置为 True
                    hc = j * h
                    if i + hc < a:
                        new_table[i + hc] = True
                        imax = max(i + hc, imax)
                
        table = [a or b for a, b in zip(table, new_table)]
    
    return imax


# https://leetcode.com/problems/partition-equal-subset-sum/submissions/
def solution2(data):
    lmax = max(data, key = lambda x: x[1])[1] 
    table = [True] + [False] * lmax

    data.sort(cmp = lambda a, b: a[1] - b[1])
    dic = {}
    nums = []
    for h, a, c in data:
        dic[h] = a
        nums += [h] * c

    imax = 0
    for i in range(len(nums)):
        for j in range(dic[nums[i]], nums[i] - 1, -1):
            table[j] = table[j] or table[j - nums[i]]
            if table[j]:
                imax = max(imax, j)

    return imax



def main():
    for i in range(11):
        file_name = '1239/test%d.in' % i
        out_name = '1239/test%d.out' % i

        data = []

        with open(file_name, 'r') as inf:
            n = int(inf.readline())

            for line in inf.readlines():
                line = [int(i) for i in line.strip().split()]
                data.append(line)

        out = 0
        with open(out_name, 'r') as inf:
            out = int(inf.read())

        
        # res = solution(data)
        res = solution2(data)
        print 'out:', res, 'ans:', out, res == out

main()
