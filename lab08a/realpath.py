#!/usr/bin/env python3

import sys

argv = sys.argv


i = 1
while i < len(argv):
   path = sys.argv[i].split("..")
   print(("".join(path)).split("//"))
   i = i + 1
   