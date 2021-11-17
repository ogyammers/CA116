#!/usr/bin/env python3

import sys

with open("irish-dobs.txt") as f:
   a = f.readlines()

with open("american-dobs.txt", "w") as f:
   i = 0
   while i < len(a):
      line = a[i].rstrip("\n")
      day = a[i].split("/")[0]
      month = a[i].split("/")[1]
      rest = line.split("/")[2]
      f.write(month + "/" + day + "/" + rest + "\n")
      i = i + 1
