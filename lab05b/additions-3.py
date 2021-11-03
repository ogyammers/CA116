#!/usr/bin/env python3

x = 0
y = 0

i = 0
while (int(x) + int(y)) != 1000:
   j = 0
   s = input()
   while j < len(s) and not (s[j] == "+"):
      j = j + 1
   x = s[:j]
   y = s[j + 1:]
   print(int(x) + int(y))
   i = i + 1
