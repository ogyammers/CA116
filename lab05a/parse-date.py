#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] != " ":
   i = i + 1

day = s[:i]
#print(day)

j = i + 1
while j < len(s) and s[j] != " ":
   j = j + 1

date = s[i + 1:j]
#print(date)

i = j + 1
while i < len(s) and s[i] != " ":
   i = i + 1

month = s[j + 1:i - 1]
#print(month)

j = i + 1
while j < len(s) and s[j] != " ":
   j = j + 1

year = s[i + 1:j]
#print(year)

print(month, date + ",", year, "(" + day + ")")
