#!/usr/bin/python
"""
  equal.py
  by David Weinman
  8/29/14, 6:19p

---
prints true if the two given arguments
are equal to the precision given and
false if not.
"""

import sys

def equal_precise(n1, n2, p):
	return abs(n1 - n2) < 10 ** (-p)

if __name__ == "__main__": print("%s" % str(equal_precise(float(sys.argv[1]), float(sys.argv[2]), 6)))

