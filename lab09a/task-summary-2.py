#!/usr/bin/env python3

import sys

status = {}
count = {}
lines = sys.stdin.read().split()

i = 0
while i < len(lines):
   tokens = lines[i].split(".")
   task = ".".join(tokens[:2])
   result = tokens[2]

   status[task] = result == "correct"
   i = i + 1

for task in status:
   if task.split("/")[0] not in count:
      count[task.split("/")[0]] = 0
   if status[task]:
      count[task.split("/")[0]] = count[task.split("/")[0]] + 1

for task in count:
   print(task, count[task])
