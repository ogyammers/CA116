#!/usr/bin/env python3

a = []
b = []

n = input()

i = 0
while n != "end":
   if len(a) <= i:
      a.append(i)
      b.append(0)
   if int(n) == int(a[i]):
      b[i] = b[i] + 1
      n = input()
      i = 0
   i = i + 1

i = 0
while i < len(a):
   if b[i] != 0:
      print(a[i])
      b[i] = b[i] - 1
   else:
      i = i + 1
