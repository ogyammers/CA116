#!/usr/bin/env python3

import sys

lines = sys.stdin.read().split()
a = []
b = []

i = 0
while i < len(lines) - 1:
   a.append(lines[i + 1] + " " + lines[i])
   i = i + 2

i = 0
while i < len(a):
   j = i
   while j < len(a):
      if a[j] < a[i]:
         tmp = a[j]
         a[j] = a[i]
         a[i] = tmp
      j = j + 1
   i = i + 1

i = 0
while i < len(a):
   print(a[i].split(" ")[1] + " " + a[i].split(" ")[0])
   i = i + 1
