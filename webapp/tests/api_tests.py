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

	def test_school_by_ACT(self):
		test_url = BASE_URL + "schools?ACT_cumulative_MID=30..34&name=carleto&fields=name,city"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])

	def test_school_by_SAT(self):	
		test_url = BASE_URL + "schools?SAT_average=1400..1500&name=carleto&fields=name,city"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])

	def test_ownership(self):
		test_url = BASE_URL + "schools?name=carleto&fields=name,city,ownership"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield', 'ownership': 'private'}])
	def test_ownership_2(self):
		test_url = BASE_URL + "schools?ownership=private&name=carleto&fields=name,city"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])

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

	def test_percent_Asian(self):
		test_url = BASE_URL + "schools?name=carleto&percent_Asian=0.01..0.2&fields=name,city"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{'name':'Carleton College', 'city': 'Northfield'}])

	def test_school_searched_by_major(self):
		test_url = BASE_URL + "schools?History=true&Mathematics_and_Statistics=true&name=carleto&fields=name,city"
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


	#There should be errors
	def test_school_name_invalid(self):
		self.assertRaises(TypeError, school_searched_by_name, 3.1415926)
	def test_school_id_invalid(self):
		self.assertRaises(ValueError, school_searched_by_id, -1)
		self.assertRaises(TypeError, school_searched_by_id, 1.5)
	def test_school_major_invalid(self):
		self.assertRaises(TypeError, school_searched_by_major, 1)
	def test_ownership_invalid(self):
		self.assertRaises(TypeError, school_searched_by_ownership, -1)
		self.assertRaises(ValueError, school_searched_by_ownership, 'not private nor public')
	def test_score_invalid(self):
		self.assertRaises(ValueError, school_searched_by_SAT_MID, 3000)
		self.assertRaises(ValueError, school_searched_by_SAT_MID, -1500)
		self.assertRaises(TypeError, school_searched_by_ACT_cumulative_MID, 'not int')
	def test_school_faculty_earning_invalid(self):
		self.assertRaises(ValueError, school_searched_by_faculty_salary, -1)
		self.assertRaises(TypeError, school_searched_by_faculty_salary, "not int")
	def test_mean_earning_after_graduation_invalid(self):
		self.assertRaises(ValueError, school_searched_by_mean_earning_10_years_after_graduation, -1)
		self.assertRaises(TypeError, school_searched_by_mean_earning_10_years_after_graduation, "not int")
	def test_state_id_invalid(self):
		self.assertRaises(ValueError, state_searched_by_id, -1)
		self.assertRaises(TypeError, state_searched_by_id, 1.5)



	#There should be no results
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
	def test_major_no_results(self):
		test_url = BASE_URL + "schools?sleeping=true"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{}])	
	def test_MN_college_no_result(self):
		test_url = BASE_URL + "schools?state=MN&name=notcarleton college"
		data_from_server = urllib.request.urlopen(test_url).read()
		string_from_server = data_from_server.decode('utf-8')
		fetched_list = json.loads(string_from_server)
		self.assertEqual(fetched_list, [{}])	


if __name__ == '__main__':
    unittest.main()

