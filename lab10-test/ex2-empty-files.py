#!/usr/bin/env python3

import sys

i = 1
while i < len(sys.argv):
   with open(sys.argv[i]) as f:
      a = f.readlines()
      if len(a) == 0:
         print(sys.argv[i])
   i = i + 1
