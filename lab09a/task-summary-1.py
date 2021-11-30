#!/usr/bin/env python3

import sys

tasks = {}
a = []

task = sys.stdin.readline().split()
while 0 < len(task):
   if task not in a:
      a.append(task[0].split(".")[0] + "." + task[0].split(".")[1])

   if (task[0].split(".")[2]) == "correct":
      tasks[task[0].split(".")[0] + "." + task[0].split(".")[1]] = "true"

   if (task[0].split(".")[2]) == "incorrect":
      tasks[task[0].split(".")[0] + "." + task[0].split(".")[1]] = "false"

   task = sys.stdin.readline().split()

i = 0
seen = []
while i < len(a):
   if tasks[a[i]] == "true" and a[i] not in seen:
      print(a[i])
      seen.append(a[i])

   i = i + 1
