#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
   a = f.readlines()
with open(sys.argv[2]) as f:
   b = f.readlines()

if len(a) < len(b):
   print(len(b) - len(a), 0)
elif len(b) < len(a):
   print(len(a) - len(b), 0)

i = 0
while i < len(a) and i < len(b):
   j = 0
   while j < len(a[i]):
      if a[i][j] != b[i][j]:
         print(i, j)
      j = j + 1
   i = i + 1
