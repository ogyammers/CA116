#!/usr/bin/env python3

import sys

fruit = {
   "apple": True,
   "pear": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}

word = sys.stdin.readline().strip()
while 0 < len(word):
   if word in fruit:
      print(word)
   word = sys.stdin.readline().strip()
