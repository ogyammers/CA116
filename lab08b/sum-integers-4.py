#!/usr/bin/env python3

import sys

total = 0

i = 1
while i < len(sys.argv):
   with open(sys.argv[i]) as f:
      s = f.readline()
      while s != "":
         t = s.split()
         j = 0
         while j < len(t):
            total = total + int(t[j])
            j = j + 1
         s = f.readline()
   i = i + 1
print(total)
