#!/usr/bin/env python3

number = int(input())
digit3 = (((number % 10000) - (number % 1000)) // 1000) * 100000
digit4 = (((number % 1000) - (number % 100)) // 100) * 10000
digit2 = (((number % 100000) - (number % 10000)) // 10000) * 100
digit1 = (((number % 1000000) - (number % 100000)) // 100000) * 1000
digit5 = (((number % 100) - (number % 10)) // 10) * 10
digit6 = (((number % 10) - (number % 1)) // 1)

print(digit1 + digit2 + digit3 + digit4 + digit5 + digit6)
