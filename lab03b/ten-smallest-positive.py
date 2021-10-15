#!/usr/bin/env python3

n = 10

m = int(input())
smallest = m

i = 0
while i < n - 1:
   m = int(input())
   if m < smallest and m > 0:
      smallest = m
   i = i + 1

print(smallest)
