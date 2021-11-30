#!/usr/bin/env python3

import sys

eng = "one two three four five six seven eight nine ten"
ger = "eins zwei drei vier funf sechs sieben acht neun zehn"

trans = {}
eng = eng.split()
ger = ger.split()

i = 0
while i < len(eng):
   trans[eng[i]] = ger[i]
   i = i + 1

word = sys.stdin.readline().strip()
while 0 < len(word):
   if word in trans:
      print(trans[word])
   word = sys.stdin.readline().strip()
