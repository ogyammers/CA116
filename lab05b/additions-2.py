#!/usr/bin/env python3

s = input()
sum = 0

k = 0
i = 0
while i < len(s):
   j = i
   while s[j] == "+":
      if s[j] == "+":
            sum = sum + int(s[k:j])
            k = j + 1
      j = j + 1
   i = i + 1
print(sum + int(s[k:]))
