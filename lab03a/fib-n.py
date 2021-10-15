#!/usr/bin/env python3

n = int(input())

xn = 0
xn_1 = 1
xn_2 = 0

i = 0
while i < n:
   print(xn_2)
   xn = xn_1
   xn_1 = xn_2
   xn_2 = xn_1 + xn
   i = i + 1
