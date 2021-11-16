#!/usr/bin/env python3

s = input()
total = 0

while s != "end":
   tokens = s.split()
   total = total + int(tokens[2])
   s = input()

print(total)
