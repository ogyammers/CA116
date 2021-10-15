#!/usr/bin/env python3

n = 10

m = int(input())
largest = m

i = 0
while i < n - 1:
   m = int(input())
   if m > largest:
      largest = m
   i = i + 1

print(largest)
