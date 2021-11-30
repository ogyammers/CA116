#!/usr/bin/env python3

import sys

n = 100

lines = sys.stdin.read().split()

i = 0
while i < len(lines) and int(lines[i]) < n:
   i = i + 1

if i == len(lines):
   print("none")
else:
   print(lines[i])
