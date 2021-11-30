#!/usr/bin/env python3

import sys

trans = {}
eng = []
ger = []

with open("translation.txt") as f:
   lines = f.readlines()

i = 0
while i < len(lines):
   eng.append(lines[i].split()[0])
   ger.append(lines[i].split()[1])
   i = i + 1

i = 0
while i < len(eng):
   trans[eng[i]] = ger[i]
   i = i + 1

word = sys.stdin.readline().strip()
while 0 < len(word):
   if word in trans:
      print(trans[word])
   word = sys.stdin.readline().strip()
