#!/usr/bin/env python3

import sys

p = int(sys.argv[1])

s = input()


k = 0
i = 0
while k < p + 1:
   j = i
   i = i + 1
   while i < len(s) and s[i] != ",":
      i = i + 1
   k = k + 1

if p == 0:
   print(s[:i])
else:
   print(s[j + 1:i])
