#!/usr/bin/env python3

a = []
b = []

n = input()
while n != "end":
   a.append(n)
   n = input()

i = 0
while i < 10:
   count = 0
   j = 0
   while j < len(a):
      if i == int(a[j]):
         count = count + 1
      j = j + 1
   b.append(count)
   i = i + 1

i = 0
while i < 10:
   print(i, b[i] * "*")
   i = i + 1
