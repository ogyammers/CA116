#!/usr/bin/env python3

a = []

s = input()
while s != "end":
   a.append(int(s))
   s = input()

i = 0
while i < len(a):
   if a[i] % 2 == 0:
      print(a[i])
   i = i + 1

i = 0
while i < len(a):
   if a[i] % 2 != 0:
      print(a[i])
   i = i + 1
