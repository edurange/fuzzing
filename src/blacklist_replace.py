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

blacklist = {'00': '<NUL>', '01': '<SOH>', '02': '<STX>', '03': '<ETX>', '04': '<EOT>', '05': '<ENQ>', '06': '<ACK>', '07': '<BEL>', '08': '<BS>', '09': '<HT>', '0a': '<NL>', '0b': '<VT>', '0c': '<NP>', '0d': '<CR>', '0e': '<SO>', '0f': '<SI>', '10': '<DLE>', '11': '<DC1>', '12': '<DC2>', '13': '<DC3>', '14': '<DC4>', '15': '<NAK>', '16': '<SYN>', '17': '<ETB>', '18': '<CAN>', '19': '<EM>', '1a': '<SUB>', '1b': '<ESC>', '1c': '<FS>', '1d': '<GS>', '1e': '<RS>', '1f': '<US>', '7f': '<DEL>', '80': '<EURO>', '81': '<81>', '82': '<82>', '83': '<83>', '84': '<84>', '85': '<85>', '86': '<86>', '87': '<87>', '88': '<88>', '89': '<89>', '8a': '<8A>', '8b': '<8B>', '8c': '<8C>', '8d': '<8D>', '8e': '<8E>', '8f': '<8F>', '90': '<90>', '91': '<91>', '92': '<92>', '93': '<93>', '94': '<94>', '95': '<BULL>', '96': '<96>', '97': '<97>', '98': '<98>', '99': '<99>', '9a': '<9A>', '9b': '<9b>', '9c': '<L_OE>', '9d': '<9D>', '9e': '<9E>', '9f': '<9F>', 'a0': '<A0>', 'a1': '<A1>', 'a2': '<CENT>', 'a3': '<POUND>', 'a4': '<CURR>', 'a5': '<YEN>', 'a6': '<A6>', 'a7': '<SECT>', 'a8': '<UMLT>', 'a9': '<COPY>', 'aa': '<ORDF>', 'ab': '<AB>', 'ac': '<NOT>', 'ad': '<SHY>', 'ae': '<REG>', 'af': '<MACR>', 'b0': '<DEG>', 'b1': '<PLSMN>', 'b2': '<B2>', 'b3': '<B3>', 'b4': '<ACUTE>', 'b5': '<MICRO>', 'b6': '<PARA>', 'b7': '<MIDDOT>', 'b8': '<CEDIL>', 'b9': '<B9>', 'ba': '<ORDM>', 'bb': '<BB>', 'bc': '<BC>', 'bd': '<BD>', 'be': '<BE>', 'bf': '<BF>', 'c0': '<C0>', 'c1': '<C1>', 'c2': '<C2>', 'c3': '<C3>', 'c4': '<C4>', 'c5': '<C5>', 'c6': '<C6>', 'c7': '<C7>', 'c8': '<C8>', 'c9': '<C9>', 'ca': '<CA>', 'cb': '<CB>', 'cc': '<CC>', 'cd': '<CD>', 'ce': '<CE>', 'cf': '<CF>', 'd0': '<D0>', 'd1': '<D1>', 'd2': '<D2>', 'd3': '<D3>', 'd4': '<D4>', 'd5': '<D5>', 'd6': '<D6>', 'd7': '<MUL>', 'd8': '<D8>', 'd9': '<D9>', 'da': '<DA>', 'db': '<DB>', 'dc': '<DC>', 'dd': '<DD>', 'de': '<DE>', 'df': '<DF>', 'e0': '<E0>', 'e1': '<E1>', 'e2': '<E2>', 'e3': '<E3>', 'e4': '<E4>', 'e5': '<E5>', 'e6': '<E6>', 'e7': '<E7>', 'e8': '<E8>', 'e9': '<E9>', 'ea': '<EA>', 'eb': '<EB>', 'ec': '<EC>', 'ed': '<ED>', 'ee': '<EE>', 'ef': '<EF>', 'f0': '<F0>', 'f1': '<F1>', 'f2': '<F2>', 'f3': '<F3>', 'f4': '<F4>', 'f5': '<F5>', 'f6': '<F6>', 'f7': '<F7>', 'f8': '<F8>', 'f9': '<F9>', 'fa': '<FA>', 'fb': '<FB>', 'fc': '<FC>', 'fd': '<FD>', 'fe': '<FE>', 'ff': '<FF>'}

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

