'''
	Unit Tests for Schoogle API
	Created by Muyang Shi and Johnny Reichman, 10/16/18
'''

import sys
import json
import urllib.request
import ssl
import csv
import unittest

BASE_URL = "http://whatever.com/"

class SchoogleTests(unittest.TestCase):

	def test_name(self):
		test_url = BASE_URL + "schools?name=carleto&fields=name,city"
		ata_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])	


	def test_admission(self):
		test_url = BASE_URL + "schools?admission_rate=0.2..0.5&name=carleto&fields=name,city"
		ata_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])


	def test_major(self):
		test_url = BASE_URL + "schools?history=true&name=carleto&fields=name,city"
		ata_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])


	def test_state_id_invalid(self):
		test_url = BASE_URL + "schools?id=-1"
		self.assertRaises(ValueError, urllib.request.urlopen, test_url)


	def test_no_results(self):
		test_url = BASE_URL + "schools?enrollment=999999"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [])


if __name__ == '__main__':
    unittest.main()

