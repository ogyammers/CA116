#!/usr/bin/env python3

s = input()
n = 0

i = 0
while i < len(s):
   n = n + int(s[i]) * (2 ** (len(s) - i - 1))
   i = i + 1

print(n)
