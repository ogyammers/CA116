#!/usr/bin/env python3

n = 10

total = 0

i = 0
while i < n:
   m = int(input())
   if m > 0:
      total = total + (m % 10)
   if m < 1:
      total = total + ((m * -1) % 10)
   i = i + 1

print(total)
