#!/usr/bin/env python3

n = int(input())
s = ""

map = [
   "0", "1", "2", "3", "4", "5", "6", "7",
   "8", "9", "a", "b", "c", "d", "e", "f"]

while n != 0:
   s = map[(n % 16)] + s
   n = n // 16

print(s)
