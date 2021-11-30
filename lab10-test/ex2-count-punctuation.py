#!/usr/bin/env python3

import sys

lines = sys.stdin.read()
punctuation = [".", ",", "!", "?", ";", ":"]
count = 0

i = 0
while i < len(lines):
   if lines[i] in punctuation:
      count = count + 1
   i = i + 1

print(count)
