#!/usr/bin/env python3

import sys

p = sys.stdin.read().split()

i = 1
while i < len(p):
   j = i
   while j < len(p):
      if int(p[j]) < int(p[i]):
         tmp = p[j]
         p[j] = p[i]
         p[i] = tmp
      j = j + 1
   i = i + 1

output = []
output.append("|")
i = 0
while i < int(p[0]):
   if str(i) in p:
      output.append("*")
   else:
      output.append(" ")
   i = i + 1
output.append("|")
print("".join(output))
