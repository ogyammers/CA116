#!/usr/bin/env python3

import sys

args = sys.argv[1]
field_name = args.split("=")[0]
value = args.split("=")[1]

i = 0
commas = 0
header = input()
while i < len(header) and header[i:len(field_name) + i] != field_name:
   if header[i] == ",":
      commas = commas + 1
   i = i + 1

s = input()
while s != "end":
   p = 0
   i = 0
   while i < len(s):
      if s[i] == ",":
         p = p + 1
      if s[i:i + len(value)] == value and p == commas:
         print(s)
      i = i + 1
   s = input()
