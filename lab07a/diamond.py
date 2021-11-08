#!/usr/bin/env python3

import sys

args = sys.argv[1:]

n = int(args[0])

i = 0
while i < (n // 2):
   print(" " * ((n // 2) - i) + "*" * (i + i + 1))
   i = i + 1
while 0 < i + 1:
   print(" " * ((n // 2) - i) + "*" * (i + i + 1))
   i = i - 1
