import getpass
import oracledb
from dotenv import load_dotenv
import os

#pw = getpass.getpass("Enter password: ") #Para que no se vea la contraseña
load_dotenv(override=True)
usrbd = os.getenv('DBORA_USR')
pwdbd = os.getenv('DBORA_PWD')
hostbd = os.getenv('DBORA_HOST')
portbd = os.getenv('DBORA_PORT')
snamebd = os.getenv('DBORA_SNAME')

connection = oracledb.connect(
    user=usrbd,
    password=pwdbd,
    host=hostbd, port=portbd, service_name=snamebd)

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

"""with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """"select sysdate from dual"""" #son 3 comillas dobles solamente
        for r in cursor.execute(sql):
            print(r)"""

# Create a table
cursor.execute("""
    create table todoitem (
        id number generated always as identity,
        description varchar2(4000),
        creation_ts timestamp with time zone default current_timestamp,
        done number(1,0),
        primary key (id))""")

# Insert some data

rows = [ ("Task 1", 0 ),
         ("Task 2", 0 ),
         ("Task 3", 1 ),
         ("Task 4", 0 ),
         ("Task 5", 1 ) ]

cursor.executemany("insert into todoitem (description, done) values(:1, :2)", rows)
print(cursor.rowcount, "Rows Inserted")

connection.commit()

# Now query the rows back
for row in cursor.execute('select description, done from todoitem'):
    if (row[1]):
        print(row[0], "is done")
    else:
        print(row[0], "is NOT done")

connection.close()