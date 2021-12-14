#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
   j = 0
   while j < len(lines[i]):
      if lines[i][j] == "(":
         print((lines[i][j + 1:]).split(")")[0])
         j = len(lines[i])
      j = j + 1
   i = i + 1
