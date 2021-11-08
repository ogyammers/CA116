#!/usr/bin/env python3

import sys
args = sys.argv[1:]
p = args[0]
a = []

s = input()

while s != "end":
   i = 0
   while i < len(s):
      j = i + 1
      if s[i:i + len(p)] == p:
         a.append(s)
         i = len(s)
      elif s[i:i + len(p)] == s[j:j + len(p)] and s[i:i + len(p)] == p:
         a.append(s)
      i = i + 1
   s = input()

j = i
while j < len(a):
   if a[j] == a[len(a) - j - 1]:
      j = j + 1

if j == len(a):
   print(a[0])

else:
   i = 0
   while i < len(a):
      print(a[i])
      i = i + 1
