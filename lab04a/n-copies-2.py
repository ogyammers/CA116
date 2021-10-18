#!/usr/bin/env python3

s = input()
n = int(input())

print((s * ((n + 2) % (n + 1)) + (("-" + s) * (n - 1))))
