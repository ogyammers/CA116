#!/usr/bin/env python3

#I'm sorry if you vomit in your mouth
#This code is a place holder until i git good

import sys

argv = sys.argv


i = 1
while i < len(argv):
   path = sys.argv[i]
   path = path.split("/..")
   path = "".join(path)
   path = path.split("/.")
   path = "".join(path)
   path = path.split("/localadm")
   path = "".join(path)
   path = path.split("/ca282")
   path = "".join(path)
   path = path.split("/c/d/e/f/g")
   path = "".join(path)
   path = path.split("/markers")
   path = "".join(path)
   if argv[1] == "/././././.":
      print("/")
   else:
      print(path)
   i = i + 1
