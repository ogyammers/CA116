#!/usr/bin/env python3

s = input()
n = int(input())

print((s * (0 < n) + (("-" + s) * (n - 1))))
#print((s * ((n + 2) % (n + 1)) + (("-" + s) * (n - 1))))
