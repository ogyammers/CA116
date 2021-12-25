#!/usr/bin/env python3

import sys

n = sys.stdin.read()

xn = 0
xn_1 = 1
xn_2 = 0

i = 0
while xn_2 < int(n):
   xn = xn_1
   xn_1 = xn_2
   xn_2 = xn_1 + xn
   i = i + 1

if int(n) == xn_2:
   print("yes")
else:
   print("no")
