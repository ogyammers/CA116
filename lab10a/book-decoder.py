#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
output = []

i = 0
while i < len(lines):
   a = lines[i].split()

   line = int(a[1])
   letter = int(a[2])
   page = "page-" + a[0] + ".txt"

   with open(page) as f:
      b = f.readlines()
      output.append((b[line][letter]))

   i = i + 1

print("".join(output).strip("\n"))
