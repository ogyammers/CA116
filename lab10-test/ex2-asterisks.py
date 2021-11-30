#!/usr/bin/env python3

import sys

alpha = "abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ"

output = []

with open("input.txt") as f:
   a = f.read()

i = 0
while i < len(a):
   if a[i] in alpha:
      output.append("*")
   else:
      output.append(a[i])
   i = i + 1

output = "".join(output)

with open("output.txt", "w") as f_out:
   f_out.write(output)
