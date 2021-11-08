#!/usr/bin/env python3

a = []
n = input()

while n != "end":
   a.append(n)
   n = input()

i = 0
while i < len(a):
   p = i
   j = i + 1
   while j < len(a):
      if int(a[j]) < int(a[p]):
         p = j
      j = j + 1
   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp
   p = i
   i = i + 1

print(a[len(a) // 2])
