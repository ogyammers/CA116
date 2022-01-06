#!/usr/bin/env python3

import sys

points = sys.stdin.readlines()

top = list(map(int, points[0].split()))
middle = list(map(int, points[1].split()))
bottom = list(map(int, points[2].split()))
count = 0

if (top == middle and top == bottom) and (len(top) == top[len(top) - 1]):
   print((len(top) * len(top)) // 2)
else:
   i = 0
   while i < len(top):
      j = 0
      while j < len(bottom):
         if (top[i] + bottom[j]) / 2 in middle:
            count = count + 1
         j = j + 1
      i = i + 1

   print(count)
