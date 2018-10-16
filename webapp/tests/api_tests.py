'''
	Phase 2 of the Books homework assignment for CS 257, Jeff Ondich
	This program runs a variety of unit tests for booksdatasource.py
	Created by Eric Stadelman and Johnny Reichman, 9/21/18
'''

import sys
import json
import urllib.request
import ssl
import csv
import unittest

BASE_URL = "http://whatever.com/"

class SchoogleTests(unittest.TestCase):
	def test_state_id_invalid(self):
		test_url = BASE_URL + "schools?id=-1"
		self.assertRaises(ValueError, urllib.request.urlopen, test_url)


if __name__ == '__main__':
    unittest.main()

