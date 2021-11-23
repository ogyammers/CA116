#!/usr/bin/env python3

import sys

with open("boys.txt") as f:
   boys = f.readlines()
with open("girls.txt") as f:
   girls = f.readlines()

name = sys.stdin.readline()
while 0 < len(name):
   if name in boys and name in girls:
      print(name.strip(), "either")
   elif name in boys:
      print(name.strip(), "boy")
   elif name in girls:
      print(name.strip(), "girl")
   name = sys.stdin.readline()
