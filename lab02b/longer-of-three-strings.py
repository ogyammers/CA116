#!/usr/bin/env python3

string_1 = input()
string_2 = input()
string_3 = input()

if len(string_1) > len(string_2) and len(string_1) > len(string_3):
   print(string_1)
elif len(string_2) > len(string_1) and len(string_2) > len(string_3):
   print(string_2)
elif len(string_3) > len(string_1) and len(string_3) > len(string_2):
   print(string_3)
