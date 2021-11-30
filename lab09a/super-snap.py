#!/usr/bin/env python3

import sys

words = {}
snap = []
word = sys.stdin.readline().strip()
while 0 < len(word):
   if word in words:
      snap.append(word)
   else:
      words[word] = "true"
   word = sys.stdin.readline().strip()

if snap != []:
   print("snap:", snap[0])
