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

# Who needs a database when you can just hard-code some actors and movies?
# actors = [
#     {'last_name': 'Pickford', 'first_name': 'Mary'},
#     {'last_name': 'Rains', 'first_name': 'Claude'},
#     {'last_name': 'Lorre', 'first_name': 'Peter'},
#     {'last_name': 'Greenstreet', 'first_name': 'Sydney'},
#     {'last_name': 'Bergman', 'first_name': 'Ingrid'},
#     {'last_name': 'Grant', 'first_name': 'Cary'},
#     {'last_name': 'Colbert', 'first_name': 'Claudette'},
#     {'last_name': 'McDormand', 'first_name': 'Frances'},
#     {'last_name': 'Wiig', 'first_name': 'Kristen'},
#     {'last_name': 'Adams', 'first_name': 'Amy'}
# ]

# movies = [
#     {'title': 'Casablanca', 'year': 1942, 'genre': 'drama'},
#     {'title': 'North By Northwest', 'year': 1959, 'genre': 'thriller'},
#     {'title': 'Alien', 'year': 1979, 'genre': 'scifi'},
#     {'title': 'Bridesmaids', 'year': 2011, 'genre': 'comedy'},
#     {'title': 'Arrival', 'year': 2016, 'genre': 'scifi'},
#     {'title': 'It Happened One Night', 'year': 1934, 'genre': 'comedy'},
#     {'title': 'Fargo', 'year': 1996, 'genre': 'thriller'},
#     {'title': 'Clueless', 'year': 1995, 'genre': 'comedy'}
# ]

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
    #Returns a list of all schools:
    connection = get_connection()
    try:
        cursor = connection.cursor()
        query = 'SELECT schools.school_name, states.state_name FROM schools, states WHERE schools.state_id = states.state_id'
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    schools = []
    for row in cursor:
        schools.append({ 'state name': row[1], 'school name': row[0]})
    return json.dumps(schools)








if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
