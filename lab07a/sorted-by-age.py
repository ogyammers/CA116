#!/usr/bin/env python3

a = []
n = input()

while n != "end":
   n = n[6:8] + n[3:5] + n[0:2] + n[8:]
   a.append(n)
   n = input()

i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp[7:]
   p = i
   i = i + 1


i = 0
while i < len(a):
   print(a[i])
   i = i + 1
