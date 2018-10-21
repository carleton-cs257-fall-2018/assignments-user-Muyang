#!/usr/bin/env python3
'''
    example_flask_app.py
    Jeff Ondich, 22 April 2016

    A slightly more complicated Flask sample app than the
    "hello world" app found at http://flask.pocoo.org/.
'''
import sys
import flask
import json
import config
import psycopg2

app = flask.Flask(__name__)
basic_list = ['school_id' ,'school_name', 'city','state_name','school_url','highest_degree','locale','ownership']
stats_list = [
    'school_id',
    'year',
    'admission_rate',

    'SAT_average',
    'SAT_cr_MID',
    'SAT_cr_25_percentile',
    'SAT_cr_75_percentile',
    'SAT_math_MID',
    'SAT_math_25_percentile',
    'SAT_math_75_percentile',
    'SAT_wr_MID',
    'SAT_wr_25_percentile',
    'SAT_wr_75_percentile',

    'ACT_cumulative_MID',
    'ACT_cumulative_25_percentile',
    'ACT_cumulative_75_percentile',
    'ACT_eng_MID',
    'ACT_eng_25_percentile',
    'ACT_eng_75_percentile',
    'ACT_math_MID',
    'ACT_math_25_percentile',
    'ACT_math_75_percentile',
    'ACT_writing_MID',
    'ACT_writing_25_percentile',
    'ACT_writing_75_percentile',

    'Agriculture',
    'Natural_Resource',
    'Architecture',
    'Area_Ethnic_Cultural_Gender_Group_Studies',
    'Communication_Journalism',
    'Communication_Technologies',
    'Computer_Information_Sciences',
    'Personal_Culinary_Services',
    'Education',
    'Engineering',
    'Engineering_Technologies',
    'Foreign_Languages_Literatures_Linguistics',
    'Human_Sciences',
    'Legal_Professions_Studies',
    'English_Language_And_Literature',
    'General_Studies_And_Humanities',
    'Library_Science',
    'Biological_and_Biomedical_Sciences',
    'Mathematics_and_Statistics',
    'Military_Technologies_and_Applied_Sciences',
    'Interdiciplinary_Studies',
    'Parks_Recreation_Leisure_Fitness_Studies',
    'Philosophy_and_Religious_Studies',
    'Theology_and_Religious_Vocations',
    'Physical_Sciences',
    'Science_Technologies',
    'Psychology',
    'Homeland_Security_Law_Enforcement_Firefighting',
    'Public_Administration_and_Social_Service',
    'Social_Sciences',
    'Construction_Trade',
    'Mechanic_and_Repair_Technology',
    'Precision_Production',
    'Transportation_and_Materials_Moving',
    'Visual_and_Performing_Arts',
    'Health_Professions',
    'Business_Management_Marketing',
    'History',

    'enrollment',
    'percent_white',
    'percent_black',
    'percent_Hispanic',
    'percent_Asian',
    'percent_American_Indian',
    'percent_Native_Hawaiian',
    'percent_nonresident_aliens',

    'average_net_price_public_institutions',
    'average_net_price_private_institutions',

    'percent_student_of_Pell_Grant',
    'percent_student_of_Federal_Loan',

    'average_faculty_earnings']
state_list = [
    'state_id',
    'state_name',
    'state_abbreviation'
]

def _create_dictionary(keys, values):
    #assert len(keys) == len(values)
    returned_dict = {}
    for i in range (len(keys)):
        returned_dict[keys[i]] = values[i]
    return returned_dict

def get_connection():
    '''
    Returns a connection to the database described
    in the config module. Returns None if the
    connection attempt fails.
    '''
    connection = None
    try:
        connection = psycopg2.connect(database=config.database,
                                      user=config.user,
                                      password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
    return connection


@app.route('/')
def hello():
    return 'Hello, Citizen of CS257.'

# @app.route('/actor/<last_name>')
# def get_actor(last_name):
#     ''' Returns the first matching actor, or an empty dictionary if there's no match. '''
#     actor_dictionary = {}
#     lower_last_name = last_name.lower()
#     for actor in actors:
#         if actor['last_name'].lower().startswith(lower_last_name):
#             actor_dictionary = actor
#             break
#     return json.dumps(actor_dictionary)

@app.route('/schools')
def get_schools():
    #Returns a list of all schools with basic information:
    school_id = flask.request.args.get('school_id', default=None)
    school_name = flask.request.args.get('school_name', default=None)
    city = flask.request.args.get('school_name', default=None)
    state_id = flask.request.args.get('school_name', default=None)
    school_url = flask.request.args.get('school_name', default=None)
    highest_degree = flask.request.args.get('school_name', default=None)
    locale = flask.request.args.get('school_name', default=None)
    ownership = flask.request.args.get('school_name', default=None)
    

    school_list = _get_all_school_stats()
    if school_id is not None:
        school_list = _filter_school_by_id(school_list, school_id)
    if school_name is not None:
        school_list = _filter_school_by_name(school_list, school_name)
    
    return json.dumps(school_list)









def _filter_school_by_name(school_list, school_name):
    school_index = 0    
    while school_index < len(school_list):
        if(school_name.lower() not in school_list[school_index]['school_name'].lower()):
            school_list.remove(school_list[school_index])
            school_index -= 1
        school_index += 1
    return school_list



def _filter_school_by_id(school_list, school_id):
    school_index = 0
    while school_index < len(school_list):
        if(school_id != str(school_list[school_index]['school_id'])):
            school_list.remove(school_list[school_index])
            school_index -= 1
        school_index += 1
    return school_list

def _get_all_schools_basics():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        query = '''SELECT school_id ,school_name, city,state_name,school_url,highest_degree,locale,ownership 
                    FROM schools, states 
                    WHERE schools.state_id = states.state_id'''
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    schools = []
    for row in cursor:
        schools.append(_create_dictionary(basic_list,row))
    connection.close()
    return schools


def _get_all_school_stats():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        query = '''SELECT * 
                    FROM schools, school_stats, states 
                    WHERE schools.state_id = states.state_id
                    AND schools.school_id = school_stats.school_id'''
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    school_stats = []
    for row in cursor:
        school_stats.append(_create_dictionary(basic_list+stats_list+state_list,row))
    connection.close()
    return school_stats




if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
