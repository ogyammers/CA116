#!/usr/bin/env python3

import sys

n = 20

lines = sys.stdin.readlines()
plot = []

i = 0
while i < n:
   plot.append([" "] * n)
   i = i + 1

i = 0
while i < len(lines):
   tokens = lines[i].split()
   y = int(tokens[1])
   x = int(tokens[0])
   plot[y][x] = "*"
   i = i + 1

print(" " + "-" * n)

y = 0
while y < n:
   print("|" + "".join(plot[n - y - 1]) + "|")
   y = y + 1

print(" " + "-" * n)
