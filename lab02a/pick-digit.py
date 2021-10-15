#!/usr/bin/env python3

n = int(input())
m = int(input()) + 1

print(((n % 10 ** m) - (n % 10 ** (m - 1))) // (10 ** (m - 1)))
