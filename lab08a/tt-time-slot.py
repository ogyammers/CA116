#!/usr/bin/env python3

s = input()

while s != "end":
   tokens = s.split()
   start = (s[0] + " " + str(int(tokens[1]) % 24)) + ":00"
   end = str(int(tokens[1]) + int(tokens[2]) - 1) + ":50"
   print(start, end, " ".join(tokens[3:]))
   s = input()
