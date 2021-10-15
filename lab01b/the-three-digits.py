#!/usr/bin/env python3

number = int(input())
first_digit = (number // 100)
second_digit = ((number - (first_digit * 100)) // 10)
third_digit = (number - (first_digit * 100) - (second_digit * 10))

print(first_digit)
print(second_digit)
print(third_digit)
