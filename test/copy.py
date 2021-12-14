#!/usr/bin/env python3

import sys

in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file) as f_in:
   with open(out_file, "w") as f_out:
      f_out.write(f_in.read())
