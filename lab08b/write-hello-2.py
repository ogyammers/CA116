#!/usr/bin/env python3

import sys

message = "Hello world.\n"
file_name = sys.argv[1]

with open(file_name, "w") as f:
   f.write(message)
