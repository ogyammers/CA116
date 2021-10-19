#!/usr/bin/env python3

s = input()
n = 0
m = 1

i = 0
while i < len(s):
   n = int(s[len(s) -i - 1]) * m + n
   m = m * 2
   i = i + 1

print(n)
