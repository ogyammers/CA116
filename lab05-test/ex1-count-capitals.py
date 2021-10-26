#!/usr/bin/env python3

s = input()
count = 0

i = 0
while i < len(s):
   if "A" <= s[i] and s[i] <= "Z":
      count = count + 1
   i = i + 1

print(count)
