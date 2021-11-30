#!/usr/bin/env python3

import sys

animals = {}
seen = []

word = sys.stdin.readline().strip()
while 0 < len(word):
   if word in animals:
      animals[word] = animals[word] + 1
   if word not in animals:
      animals[word] = 0
      seen.append(word)
   word = sys.stdin.readline().strip()

i = 0
while i < len(seen):
   if seen[i] in animals and animals[seen[i]] == 0:
      print(seen[i])
   i = i + 1
