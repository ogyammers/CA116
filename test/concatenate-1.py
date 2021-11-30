#!/usr/bin/env python3

import sys

out_file = sys.argv[1]               # The output file.
in_files = sys.argv[2:]              # The input files.

with open(out_file, "w") as f_out:
   i = 0
   while i < len(in_files):
      with open(in_files[i]) as f_in:
         f_out.write(f_in.read())    # Copy the entire input file to the output file.
      i = i + 1
