#!/usr/bin/env python3

x = 2 * (x < 0) - x - 1

#1 x = int((x + ((-1) ** x)) * (-1))

#2 x = -x + 2 * (x % 2) - 1

#3 x = (x + (0 < x) + (0 > x) * -1) * -1
