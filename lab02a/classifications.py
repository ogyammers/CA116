#!/usr/bin/env python3

grade = int(input())

print("first:", grade >= 70)
print("second:", 50 <= grade < 70)
print("third:", 40 <= grade <= 49)
print("fail:", grade < 40)
