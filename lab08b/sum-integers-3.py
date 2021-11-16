#!/usr/bin/env python3

import sys

total = 0

i = 1
while i < len(sys.argv):
   with open(sys.argv[i]) as f:
      s = f.readline()
      while s != "":
         total = total + int(s)
         s = f.readline()
   i = i + 1
print(total)
