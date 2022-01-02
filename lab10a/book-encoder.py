#!/usr/bin/env python3

import sys

message = sys.stdin.read()
output = []
b = []

i = 0
while i < len(message):
   j = 0
   while j < 10:
      page = "page-" + str(j) + ".txt"
      with open(page) as f:
         a = f.readlines()
         k = 0
         while k < len(a):
            if message[i] in a[k]:
               char = 0
               while char < len(a[k]) and i not in b:
                  if message[i] == a[k][char]:
                     triplet = str(j) + " " + str(k) + " " + str(char)
                     output.append(triplet)
                     b.append(i)
                     if i + 1 < len(message):
                        i = i + 1
                  char = char + 1
            k = k + 1
      j = j + 1
   i = i + 1

print("\n".join(output))
