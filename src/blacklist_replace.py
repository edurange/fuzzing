#!/usr/bin/python
"""
  blacklist_replace.py
  by David Weinman
  9/4/14, 1:11a

---
prints the string given but with all
hex bytes in blacklist replaced with tags
to differentiate.
"""

"""
This file is licensed under The DO WHAT THE FUCK YOU WANT TO License, see LICENSE for details.
"""

import sys

# , '': '<>'

blacklist = {'00': '<NUL>', '01': '<SOH>', '02': '<STX>', '03': '<ETX>', '04': '<EOT>', '05': '<ENQ>', '06': '<ACK>', '07': '<BEL>', '08': '<BS>', '09': '<HT>', '0a': '<NL>', '0b': '<VT>', '0c': '<NP>', '0d': '<CR>', '0e': '<SO>', '0f': '<SI>', '10': '<DLE>', '11': '<DC1>', '12': '<DC2>', '13': '<DC3>', '14': '<DC4>', '15': '<NAK>', '16': '<SYN>', '17': '<ETB>', '18': '<CAN>', '19': '<EM>', '1a': '<SUB>', '1b': '<ESC>', '1c': '<FS>', '1d': '<GS>', '1e': '<RS>', '1f': '<US>', '20': '<SP>', '7f': '<DEL>'}

def listify_hexstr(hexbuf):
	newbuf = hexbuf
	newbufbytes = []
	while len(newbuf) > 0:
		newbufbytes.append(newbuf[:2])
		newbuf = newbuf[2:]
	return newbufbytes

def revealhex(buf):
	bufhex = buf.encode("hex")
	l_bufhex = listify_hexstr( bufhex )
	for i in blacklist:
		if i in l_bufhex:
			while i in l_bufhex:
				l_bufhex[l_bufhex.index(i):l_bufhex.index(i) + 1] = listify_hexstr( blacklist[i].encode("hex") )
	bufhex = "".join(l_bufhex)
	return bufhex.decode("hex")

if __name__ == "__main__": print(revealhex(sys.argv[1]))

