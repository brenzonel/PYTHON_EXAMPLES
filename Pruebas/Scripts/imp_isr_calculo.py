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

def imp_isr_calc(opcion, sueldo):
    try:
        connection = oracledb.connect(
            user=usrbd,
            password=pwdbd,
            host=hostbd, port=portbd, service_name=snamebd)
        #print("Successfully connected to Oracle Database")
        cursor = connection.cursor()
        
        if opcion == 1:
            query = "SELECT LIM_INF, CUOTA_FIJA, PORCENTAJE FROM ISR_QUINCENAL WHERE :SUELDO BETWEEN LIM_INF AND LIM_SUP"
        elif opcion == 2:
            query = "SELECT LIM_INF, CUOTA_FIJA, PORCENTAJE FROM ISR_QUINCENAL WHERE :SUELDO BETWEEN LIM_INF AND LIM_SUP"
        elif opcion == 3:
            query = "SELECT LIM_INF, CUOTA_FIJA, PORCENTAJE FROM ISR_QUINCENAL WHERE :SUELDO BETWEEN LIM_INF AND LIM_SUP"

        cursor.execute(query, SUELDO=sueldo)
        row = cursor.fetchone()
        limite_inf = float(row[0])
        cuota = float(row[1])
        porcentaje = float(row[2])

        resultado = (sueldo - limite_inf)
        impuesto = round(((resultado * (porcentaje/100)) + cuota), 2)

        print(f"Sueldo: {sueldo}")
        print(f"El impuesto a pagar es: {impuesto}")

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
    imp_isr_calc(opcion, sueldo)