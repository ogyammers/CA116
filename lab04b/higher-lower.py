#!/usr/bin/env python3

n = 5
curr = int(input())
prev = 0

i = 0
while i < n:
   prev = int(input())
   if prev > curr:
      print("higher")
   elif prev < curr:
      print("lower")
   else:
      print("equal")
   curr = prev
   i = i + 1
