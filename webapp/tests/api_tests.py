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
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])	


	def test_admission(self):
		test_url = BASE_URL + "schools?admission_rate=0.2..0.5&name=carleto&fields=name,city"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])
	def test_admission_2(self):
		test_url = BASE_URL + "schools?admission_rate=0.8..1.0&name=carleto&fields=name,city"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{}])	

	def test_highest_degree(self):
		test_url = BASE_URL + "schools?name=carleto&fields=name,city,highest_degree"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield','highest degree': "Bachelor's Degree"}])
	def test_highest_degree_2(self):
		test_url = BASE_URL + "schools?name=carleto&highest_degree=4&fields=name,city"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])
	def test_highest_degree_3(self):
		test_url = BASE_URL + "schools?name=carleto&highest_degree=1&fields=name,city"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{}])

	def test_major_searched(self):
		test_url = BASE_URL + "schools?history=true&name=carleto&fields=name,city"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])
	def test_major_in_fields(self):
		test_url = BASE_URL + "schools?name=carleto&fields=name,city,Agriculture"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield','Agriculture':'Not Offered'}])


	def test_school_id_invalid(self):
		#test_url = BASE_URL + "schools?id=-1"
		self.assertRaises(ValueError, school_searched_by_id, -1)
		#test_url_2 = BASE_URL + "schools?id=1.5"
		self.assertRaises(TypeError, school_searched_by_id, 1.5)
	def test_state_id_invalid(self):
		#test_url = BASE_URL + "states?id=-1"
		self.assertRaises(ValueError, state_searched_by_id, -1)
		#test_url_2 = BASE_URL + "states?id=1.5"
		self.assertRaises(TypeError, state_searched_by_id, 1.5)


	def test_school_id_no_results(self):
		test_url = BASE_URL + "schools?id=999999"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{}])
	def test_enrollment_no_results(self):
		test_url = BASE_URL + "schools?enrollment=999999"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{}])


if __name__ == '__main__':
    unittest.main()

