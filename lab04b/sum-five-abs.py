#!/usr/bin/env python3

n = 5
total = 0

i = 0
while i < n:
   m = int(input())
   if m > 0:
      total = total + m
   else:
      total = total + (m * -1)
   i = i + 1

print(total)
