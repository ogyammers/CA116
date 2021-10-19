#!/usr/bin/env python3

n = int(input())
m = 0

i = 0
while 0 < n:
   m = m + ((n % 2) * (10 ** i))
   n = int(n / 2)
   i = i + 1

print(m)
