import time
import pyotp
#Generacion de palabra clave aleatoria

#key = pyotp.random_base32() #
#print(key)


#Palabra clave secreta super top vip
key = "CosasChidas"
print(key)

#Generacion de codigo cada 30 seg

timeotp = pyotp.TOTP(key)   
print(timeotp.now())

#Prueba con tiempo
print(timeotp.now()) #Primero
time.sleep(30)              #Segundo Esperamos 30 seg
print(timeotp.now())
input_llave = input("Ingrese Codigo Verificador:  ")
print(timeotp.verify(input_llave))
input_llave = input("Ingrese nuevamente Codigo Verificador:  ")
print(timeotp.verify(input_llave))


#Tercero
#Generacion de codigo por contador
"""
hotp = pyotp.HOTP(key)
print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))
print(hotp.at(4))
print(hotp.at(5))

contador = 0
for _ in range (5):
    print(hotp.verify(input("Ingrese Codigo: "), contador))
    contador += 1
"""