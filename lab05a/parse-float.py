#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] != ".":
   i = i + 1

if i < len(s):
   j = 0
   j = i + 1

print(s[:i])
print(s[j:])
