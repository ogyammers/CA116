#!/usr/bin/env python3

n = int(input())
m = n % 100

if m == 11 or m == 12 or m == 13:
   print("th")
elif n % 10 == 1:
   print("st")
elif n % 10 == 2:
   print("nd")
elif n % 10 == 3:
   print("rd")
else:
   print("th")
