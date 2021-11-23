#!/usr/bin/env python3

import sys

animals = {}
seen = []

word = sys.stdin.readline().strip()
while 0 < len(word):
   if word not in seen: 
      seen.append(word)

   word = sys.stdin.readline().strip()

print(seen)
