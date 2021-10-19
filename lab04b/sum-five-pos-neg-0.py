#!/usr/bin/env python3

pos = 0
neg = 0

n = int(input())
while n != 0:
   if n > 0:
      pos = pos + n
   else:
      neg = neg + n
   n = int(input())

print(neg, pos)
