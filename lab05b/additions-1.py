#!/usr/bin/env python3

n = 10

i = 0
while i < n:
   j = 0
   s = input()
   while j < len(s) and not (s[j] == "+"):
      j = j + 1
   x = s[:j]
   y = s[j + 1:]
   print(int(x) + int(y))
   i = i + 1
