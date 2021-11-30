#!/usr/bin/env python3

import sys

lines = sys.stdin.read().split()
ends = ["!", ".", "?"]
output = []

i = 0
k = 0
while i < len(lines):
   j = 0
   while j < len(lines[i]):
      if lines[i][j] in ends and j == len(lines[i]) - 1:
         output.append(lines[k:i + 1])
         k = i + 1
      j = j + 1
   i = i + 1

i = 0
while i < len(output):
   if "A" < output[i][0][0] and output[i][0][0] > "Z":
      output[i][0] = output[i][0].capitalize()
   if output[i] != []:
      print(" ".join(output[i]))
   i = i + 1
