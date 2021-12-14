#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline()) #read number of buses to expect
m = sys.stdin.readline().split() # read the bus numbers

i = 0
while i < len(m): #loop converts all the bus numbers to type int
   m[i] = int(m[i])
   i = i + 1

i = 0
while i < n: #loop that sorts the bus numbers into order
   j = i
   while j < n:
      if m[j] < m[i]:
         tmp = m[j]
         m[j] = m[i]
         m[i] = tmp
      j = j + 1
   i = i + 1

i = 0
output = []
while i < n: 
   j = i
   while j < n - 1 and m[j] + 1 == m[j + 1]:  #loop which runs while numbers are consecutive
      j = j + 1
   if i < j - 1: # more than 2 consecutive numbers
      output.append(str(m[i]) + "-" + str(m[j])) # joins and appends the first number in the consecutive sequence to the last 
      i = j + 1
   else:
      output.append(str(m[i])) #appends the i'th number if it is not part of a consecutive sequence
      i = i + 1

print(" ".join(output)) #joins the numbers
