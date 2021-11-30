#!/usr/bin/env python3

with open("a.txt") as f:
   a = f.read().split()
with open("b.txt") as f:
   b = f.read().split()

d = {}

i = 0
while i < len(a) or i < len(b):
   if i < len(a) and a[i] not in d:
      d[a[i]] = "true"
   if i < len(b) and b[i] not in d:
      d[b[i]] = "true"
   i = i + 1

print("\n".join(d))
