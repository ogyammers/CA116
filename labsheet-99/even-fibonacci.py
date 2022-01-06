#!/usr/bin/env python3

import sys

n = sys.argv[1]

xn = 0
xn_1 = 1
xn_2 = 0
sum_even = 0

i = 0
while xn_2 < int(n):
   if xn_2 % 2 == 0:
      sum_even = sum_even + xn_2
   xn = xn_1
   xn_1 = xn_2
   xn_2 = xn_1 + xn
   i = i + 1

print(sum_even)
