import mysql.connector 
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(emp_id, name, photo, biodataFile):
    print("Inserting BLOB into TEST.PHOTO_TEST table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='test',
                                            user='root',
                                            password='28Extencion..')
        if connection.is_connected():
            cursor = connection.cursor()
            sql_insert_blob_query = """ INSERT INTO TEST.PHOTO_TEST
                            (ID, NAME, PHOTO, PERSON_DETAIL) VALUES (%s,%s,%s,%s)"""

            empPicture = convertToBinaryData(photo)
            file = convertToBinaryData(biodataFile)

            # Convert data into tuple format
            insert_blob_tuple = (emp_id, name, empPicture, file)
            result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
            connection.commit()
            print("Image and file inserted successfully as a BLOB into python_employee table", result)


    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "BRANDON", "C:\\Users\\brana\\Desktop\\Python\\Pruebas\\PatricioEstrella.png",
           "C:\\Users\\brana\\Desktop\\Python\\Pruebas\\PRUEBA1.txt") 
#se agregaron \\ porque \b es un comando de lectura en la url de la direccion del directorio