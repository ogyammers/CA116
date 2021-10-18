#!/usr/bin/env python3

n = int(input())

print(n * "*")
i = 0
while i < n - 2:
   print("*" + ((n - 2) * " ") + "*")
   i = i + 1

if n != 1:
   print(n * "*")
