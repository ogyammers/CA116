#!/usr/bin/env python3

import sys

s = sys.argv[1]

n = sys.stdin.read().split()

i = 0
while i < len(n):
   if len(s) <= len(n[i]):
      if n[i][len(n[i]) - len(s):] == s:
         print(n[i])
   i = i + 1
