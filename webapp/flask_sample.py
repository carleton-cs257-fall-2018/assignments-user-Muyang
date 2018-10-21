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
    return json.dumps(schools)
# def get_school():
#     #Returns a list of specs of a specific school:
#     connection = 








if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
