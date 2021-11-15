#!/usr/bin/env python3

time = input()
servers = 0
tmp = time
while time != "end":
   if int(time) < (int(tmp) + 1000):
      servers = servers + 1
   tmp = time
   time = input()

print(servers)
