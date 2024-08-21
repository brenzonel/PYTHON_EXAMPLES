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

def imp_isr(opcion, sueldo):
    try:
        connection = oracledb.connect(
            user=usrbd,
            password=pwdbd,
            host=hostbd, port=portbd, service_name=snamebd)
        #print("Successfully connected to Oracle Database")
        cursor = connection.cursor()
        if opcion ==1 :
            result = cursor.callfunc("FUN_IMPUESTO_SUELDO", float, [opcion, sueldo])
            print("Sueldo Semanal: ", sueldo)
            print("El impuesto a pagar es: ", result)

        elif opcion ==2 :
            result = cursor.callfunc("FUN_IMPUESTO_SUELDO", float, [opcion, sueldo])
            print("Sueldo Quincenal: ", sueldo)
            print("El impuesto a pagar es: ", result)

        elif opcion ==3 :
            result = cursor.callfunc("FUN_IMPUESTO_SUELDO", float, [opcion, sueldo])
            print("Sueldo Mensual: ", sueldo)
            print("El impuesto a pagar es: ", result)

        connection.close()

    except Exception as e:
        print(f'Other Error: {e}')
        connection.close()

    except oracledb.DatabaseError as e:
        print(f"Database error occurred: {e}")
        connection.close()

    except oracledb.Error as e:
        print(f"Oracle error occurred: {e}")
        connection.close()

if __name__ == '__main__':
    print("Calculo de ISR 2023/2024")
    opcion = int(input("Seleccione una opcion: \n1.- Sueldo Semanal \n2.- Sueldo Quincenal \n3.- Sueldo Mensual \n"))
    sueldo = float(input("Ingrese el sueldo: "))
    imp_isr(opcion, sueldo)