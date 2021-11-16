#!/usr/bin/env python3

import sys

lines = sys.stdin.readline()
while lines != "":
   a = lines.split("/")
   a = a[len(a) - 1].split("\n")
   print(a[0])
   lines = sys.stdin.readline()
