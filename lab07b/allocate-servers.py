#!/usr/bin/env python3

a = []
job = input()
servers = 0

while job != "end":
   a.append(job)
   job = input()

i = 0
while i < len(a):
   j = 0
   while i + j < len(a) and (int(a[i + j]) - int(a[i]) < 1001):
      j = j + 1
   if j > servers:
      servers = j
   i = i + 1

print(servers)
