#This is the api-test program
#on CollegeScoreCard API
#9/29/2018 Muyang Shi
import sys
import argparse
import json
import urllib.request

def get_list_info():
	result_list = []
	for page in range(0,72): #There are 72 pages of info
	    base_url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?_page={0}&_per_page=100&fields=id,school.name'\
	    '&api_key=ugcgsk286xURiOgj4l5I8Eej8M78cGHKPfa69L1s'
	    url = base_url.format(page)
	    data_from_server = urllib.request.urlopen(url).read()
	    string_from_server = data_from_server.decode('utf-8')
	    info_dict = json.loads(string_from_server)
	    list_of_school_dict = info_dict['results']	    
	    for dictionary in list_of_school_dict:
	        school_id = dictionary['id']
	        school_name = dictionary['school.name']
	        result_list.append({'id': school_id, 'name': school_name})
	return result_list

def get_detail_info(identifier, school):
    base_url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json?{0}={1}'\
    '&fields=id,school.name,latest.admissions.admission_rate.overall,latest.student.size,school.degrees_awarded.highest'\
    '&api_key=ugcgsk286xURiOgj4l5I8Eej8M78cGHKPfa69L1s'
    url = base_url.format(identifier, school)
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    info_dict = json.loads(string_from_server)
    school_info_dict = info_dict['results']
    result_list = []
    for school in school_info_dict:
        school_id = school['id']
        school_name = school['school.name']
        school_size = school['latest.student.size']
        school_admission_rate = school['latest.admissions.admission_rate.overall']
        school_highest_degree_offered = _in_English(school['school.degrees_awarded.highest'])
        result_list.append({'id': school_id, 'name': school_name, 
            'size': school_size, 'admission_rate': school_admission_rate,
            'highest_degree': school_highest_degree_offered})
    return result_list
def _in_English(degree):
    if degree == 4:
        return 'Graduate degree'
    elif degree == 3:
        return "Bachelor's degree"
    elif degree == 2:
        return 'Associate degree'
    elif degree == 1:
        return 'Certificate degree'


def check_identifier_id_or_name(identifier):
    if identifier == 'id':
        return 'id'
    elif identifier == 'name':
        return 'school.name'
def main(args):
    if args.action == 'list':
        list_info = get_list_info()
        for school in list_info:
            school_id = school['id']
            school_name = school['name']
            print('{0} {1}'.format(school_id, school_name))

    elif args.action == 'detail':
        identifier = check_identifier_id_or_name(args.identifier)
        detail_info = get_detail_info(identifier, args.the_school)
        for info in detail_info:
            school_id = info['id']
            school_name = info['name']
            student_size = info['size']
            admission_rate = info['admission_rate']
            highest_degree = info['highest_degree']
            print('school id: {0} \nschool name: {1} \nstudent size: {2} \
                \nadmission rate: {3} \nhighest degree: {4}'.format(school_id, school_name,
                student_size, admission_rate, highest_degree))


if __name__ == '__main__':
    # When I use argparse to parse my command line, I usually
    # put the argparse setup here in the global code, and then
    # call a function called main to do the actual work of
    # the program.
    parser = argparse.ArgumentParser(description='Get school info from the government education collegescorecard API')

    parser.add_argument('action',
                        metavar='action',
                        help='action to perform the search("list" or "detail")',
                        choices=['list','detail'])

    parser.add_argument('identifier',
                        metavar='identifier',
                        help='choose whether you are looking for a specific school \
                         through its id or name; if not looking for detail information, \
                         please type None',
                        choices=['id','name', 'None'])

    parser.add_argument('the_school',
                        metavar='the_school',
                        help='the id of the school, or the name of the school; \
                        if not looking for detail information, please type None')

    args = parser.parse_args()
    main(args)