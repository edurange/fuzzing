#!/usr/bin/python

import os

for i in range(1, 5):
	print("[*] sending char with the value: " + str(hex(i)) + "");
	cmd = 'send_fuzz_data "' + chr(i) + '"'
	error = os.system(cmd)
	if error != 0:
		print("[!] char not sent, error code: " + str(error) + ".")
#	else:
#		print('[DBG] OK: `' + cmd + '`')


