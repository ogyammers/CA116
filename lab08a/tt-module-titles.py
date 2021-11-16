#!/usr/bin/env python3

s = input()

while s != "end":
   tokens = s.split()
   print(" ".join(tokens[5:]))
   s = input()
