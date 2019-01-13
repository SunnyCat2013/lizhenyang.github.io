# -*- coding: utf-8 -*-
# learning generator

def yield_i(i = 0, cap = 100):
    while i < cap:
        yield i
        i = i + 1


ig = yield_i()

print('第 {} 次打印'.format(next(ig) + 1))
print('第 {} 次打印'.format(next(ig) + 1))
print('第 {} 次打印'.format(next(ig) + 1))
print('第 {} 次打印'.format(next(ig) + 1))
print('第 {} 次打印'.format(next(ig) + 1))
print('ig.send(100)')
print('第 {} 次打印'.format(ig.send(100) + 1))
print('第 {} 次打印'.format(next(ig) + 1))
print('第 {} 次打印'.format(next(ig) + 1))
print('第 {} 次打印'.format(next(ig) + 1))
print('第 {} 次打印'.format(next(ig) + 1))
