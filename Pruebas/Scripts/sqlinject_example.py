import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(override=True)
usrbd = os.getenv('DBPOST_USR')
pwdbd = os.getenv('DBPOST_PWD')
hostbd = os.getenv('DBPOST_HOST')
postgrebd = os.getenv('DBPOST_DB')
portbd = os.getenv('DBPOST_PORT')

# Connect to an existing database
connection = psycopg2.connect(user=usrbd, password=pwdbd, host=hostbd, port=portbd, database=postgrebd)

# Open a cursor to test the connection
#with connection.cursor() as cursor:
#    cursor.execute('SELECT COUNT(*) FROM users')
#    result = cursor.fetchone()
#print(result)

'''Creación de parámetros de query seguros'''
# BAD EXAMPLE. DON'T DO THIS!
'''def is_admin(username: str) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                admin
            FROM
                users
            WHERE
                username = '%s'
        """ % username)
        result = cursor.fetchone()

    if result == None: 
        return False
    
    admin, = result
    return admin
    '''
# GOOD EXAMPLE
def is_admin(username: str) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                admin
            FROM
                users
            WHERE
                username = %(username)s
        """, {
            'username': username
        })
        result = cursor.fetchone()

    if result == None:
        return False

    admin, = result
    return admin

#print(is_admin('haki'))
#print(is_admin('ran'))
#print(is_admin('brenzon'))
#print(is_admin("'; select true; --")) #manipulacion del query en los parametros de la funcion
print(is_admin('haki'))
is_admin("'; update users set admin = 'true' where username = 'haki'; commit; select true; --") #Manipulacion usando el query para cambiar el valor de admin
print(is_admin('haki'))

#Close the connection
connection.close()

'''Passing Safe Query Parameters'''

#cursor = connection.cursor()

# BAD EXAMPLEs. DON'T DO THIS!
#cursor.execute("SELECT admin FROM users WHERE username = '" + username + "'")
#cursor.execute("SELECT admin FROM users WHERE username = '%s', %username")
#cursor.execute("SELECT admin FROM users WHERE username = '{}'".format(username))
#cursor.execute(f"SELECT admin FROM users WHERE username = '{username}'")

# SAFE EXAMPLES. DO THIS!
#cursor.execute("SELECT admin FROM users WHERE username = %s'", (username, ))
#cursor.execute("SELECT admin FROM users WHERE username = %(username)s", {'username': username});