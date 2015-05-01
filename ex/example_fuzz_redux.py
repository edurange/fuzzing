#!/usr/bin/python

import os
import random

stock_expr = [
		'23 - 345',
		'3 / 422',
		'002 * 9',
		'56 + 67',
		'13 ^ 0',
		'221 + 0012 + 23'
		]

# insert a string (c) into a
# string (s) at some random
# place and return the result
def rinsert(s, c):
	random_place = random.randrange(0, len(s))
	return s[0:random_place + 1] + c + s[random_place + 1:len(s)]

for i in range(1, 5):
	print("[*] sending char with the value: " + str(hex(i)) + "");
	cmd = 'send_fuzz_data "' + rinsert(stock_expr[ random.randrange(0, len(stock_expr)) ], chr(i)) + '"'
	error = os.system(cmd)
	if error != 0:
		print("[!] char not sent, error code: " + str(error) + ".")
#	else:
#		print('[DBG] OK: `' + cmd + '`')


