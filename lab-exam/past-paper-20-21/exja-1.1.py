#!/usr/bin/env python3
a = [1, 233, 123, 23, 544, -653, 43, 334, 554, 344]
i = 0
while i < len(a):
   if a[i] < 0:
      digit = 3  # 3 is wrong here
      a[i] = -a[i]
   else:
      digit = 3
   if a[i] % 10 == digit:
      print(a[i])
   i = i + 1
