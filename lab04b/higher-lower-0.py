#!/usr/bin/env python3

prev = int(input())
curr = 0
if prev > 0:
   curr = int(input())


while curr != 0:
   if prev < curr:
      print("higher")
   elif prev > curr:
      print("lower")
   else:
      print("equal")
   prev = curr
   curr = int(input())
