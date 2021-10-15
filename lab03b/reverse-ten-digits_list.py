#!/usr/bin/env python3

n = 10
a = []

i = 0
while i < n:
   a.append(int(input()))
   i = i + 1

j = 0
while j < n:
   print(a[n - j - 1])
   j = j + 1
