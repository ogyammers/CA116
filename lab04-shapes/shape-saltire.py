#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
   if i < (n // 2):
      print(" " * i + "*" + " " * (n - i - i - 2) + "*")
   elif i == n // 2:
      print(" " * ((n // 2)) + "*")
   elif i > n // 2:
      print(" " * (n - i - 1) + "*" + " " * (i + i - n) + "*")
   i = i + 1
