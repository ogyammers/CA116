#!/usr/bin/env python3

a = []
b = []
c = []

s = input()

while s != "end":
   i = 0
   while i < len(s):
      if s[i] == ",":
         j = i + 1
         while j < len(s):
            if s[j] == ",":
               a.append(s[:i])
               b.append(s[i + 1:j])
               c.append(s[j + 1:])
            j = j + 1
      i = i + 1
   s = input()

n = int(input())
i = 0
while i < len(b):
   if n == 0:
      print(a[i])
   elif n == 1:
      print(b[i])
   else:
      print(c[i])
   i = i + 1
