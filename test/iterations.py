#!/usr/bin/env python3

a = [15, 9, 7, 12, 10, 11, 5, 6]

print(a)

i = 0
while i < 4:
   j = i
   while j < len(a):
      if a[j] < a[i]:
         tmp = a[j]
         a[j] = a[i]
         a[i] = tmp
      j = j + 1
   i = i + 1

print(a)
