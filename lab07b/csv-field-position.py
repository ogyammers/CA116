#!/usr/bin/env python3

import sys

name = sys.argv[1]

s = input()

p = 0
i = 0
while i < len(s) and s[i:i + len(name)] != name:
   if s[i] == ",":
      p = p + 1
   i = i + 1

print(p)
