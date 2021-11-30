#!/usr/bin/env python3

import sys

chunk_size = 4096 * 8
out_file = sys.argv[1]
in_files = sys.argv[2:]

with open(out_file, "w") as f_out:
   i = 0
   while i < len(in_files):
      with open(in_files[i]) as f_in:
         chunk = f_in.read(chunk_size)
         while 0 < len(chunk):
            f_out.write(chunk)
            chunk = f_in.read(chunk_size)
      i = i + 1
