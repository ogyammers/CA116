#!/usr/bin/env python3

number = int(input())
digit1 = ((number % 10000) - (number % 1000)) // 1000
digit2 = ((number % 1000) - (number % 100)) // 100

print((digit2 * 10) + digit1)
