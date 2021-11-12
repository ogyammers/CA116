#!/usr/bin/env python3

a = []
b = []

n = input()
while n != "end":
   a.append(n)
   n = input()
n = input()
while n != "end":
   b.append(n)
   n = input()

i = 0
j = 0
while i < len(a) and j < len(b):
   if int(a[i]) < int(b[j]):
      print(a[i])
      i = i + 1
   else:
      print(b[j])
      j = j + 1

if i == len(a):
   while j < len(b):
      print(b[j])
      j = j + 1
else:
   while i < len(a):
      print(a[i])
      i = i + 1
