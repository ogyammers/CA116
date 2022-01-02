#!/usr/bin/env python3

import sys

points = sys.stdin.readlines()

top = points[0].split()
middle = points[1].split()
bottom = points[2].split()
count = []

i = 0
while i < 1000:
   j = 0
   while j < len(middle):
      if str(int(middle[j]) - i) in top and str(int(middle[j]) + i) in bottom:
         triplet = str(int(middle[j]) - i) + middle[j] + str(int(middle[j]) + i)
         if triplet not in count:
            count.append(triplet)
      if str(int(middle[j]) + i) in top and str(int(middle[j]) - i) in bottom:
         triplet = str(int(middle[j]) + i) + middle[j] + str(int(middle[j]) - i)
         if triplet not in count:
            count.append(triplet)
      j = j + 1
   i = i + 1
print(len(count))