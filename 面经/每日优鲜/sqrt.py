# -*- coding: utf-8 -*-
'''
给定正整数N 求根号N  精确到0.001
'''
__author__ = 'Foxlora'
__time__ = '2020/11/18 22:40'


def sqrt_binary(n):
    low = 0
    high = n
    while high -low > 0.001:
        mid = (low + high)/2
        if mid * mid == n:
            return mid
        elif mid * mid > n:
            high = mid
        else:
            low = mid
    return low,high

#牛顿法：
def newton_sqrt(n):
    x0 = n

    while True:
        x1 = 0.5 * (x0 + n / x0)
        if x0 - x1 < 0.001:
            return x0
        x0 = x1




a,c =  sqrt_binary(5)
print(a,c)

d = newton_sqrt(5)
print(d)
import math
b = math.sqrt(5)
print(b)