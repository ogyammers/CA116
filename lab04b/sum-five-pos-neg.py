#!/usr/bin/env python3

n = 5
pos = 0
neg = 0

i = 0
while i < n:
   m = int(input())
   if m > 0:
      pos = pos + m
   else:
      neg = neg + m
   i = i + 1

print(neg, pos)
