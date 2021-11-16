#!/usr/bin/env python3

import sys

file_name = sys.argv[1]
print(file_name)

with open(file_name, "w") as f:
   print(f.read())
   
