#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

cypher = {}

i = 0
while i < len(src):
   cypher[src[i]] = dst[i]
   i = i + 1

output = []
text = sys.stdin.readline().strip()
while 0 < len(text):
   i = 0
   while i < len(text):
      if text[i] in cypher:
         output.append(cypher[text[i]])
      else:
         output.append(text[i])
      i = i + 1
   print("".join(output))
   output = []
   text = sys.stdin.readline().strip()
