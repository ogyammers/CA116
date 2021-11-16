#!/usr/bin/env python3

import sys

args = sys.argv[1]
header = args.split("=")[1]

s = input()
while s != "end":
   i = 0
   while i < len(s):
      if s[0:2] == header:
         print(s)
         i = len(s)
      elif s[i:i + len(header)] == header:
         print(s)
      i = i + 1
   s = input()
