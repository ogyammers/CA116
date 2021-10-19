#!/usr/bin/env python3

a = int(input())
b = int(input())

tmp = 0

while b != 0:
   tmp = b
   b = a % b
   a = tmp

print(a)
