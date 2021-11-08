#!/usr/bin/env python3

a = []
n = input()

while n != "end":
   a.append(n)
   n = input()

i = int(input())
p = i
while i < len(a):
   if int(a[i]) < int(a[p]):
      p = i
   i = i + 1

print(p)
