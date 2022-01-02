#!/usr/bin/env python3

import sys

numbers = sys.argv[1:]

tickets = sys.stdin.readlines()


prizes = {
   0: 0,
   1: 1,
   2: 5,
   3: 100,
}

i = 0
while i < len(tickets) and len(numbers) == 3:
   tickets[i] = tickets[i].split()
   j = 0
   count = 0
   while j < len(tickets[i]):
      if tickets[i][j] in numbers:
         count = count + 1
      j = j + 1
   print(prizes[count])
   i = i + 1
