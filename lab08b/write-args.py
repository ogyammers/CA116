#!/usr/bin/env python3

import sys

file_name = sys.argv[1]

with open(file_name, "w") as f:
   i = 2
   while i < len(sys.argv):
      message = sys.argv[i]
      f.write(message + "\n")
      i = i + 1
