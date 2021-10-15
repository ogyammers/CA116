#!/usr/bin/env python3

n = 10
m = 0

i = 0
while i < n:
   m = (m + int(input())) * 10
   i = i + 1

i = 0
while i < n:
   m = m // 10
   print(m % 10)
   i = i + 1
