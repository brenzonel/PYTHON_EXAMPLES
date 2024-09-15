import time
import pyotp
import qrcode

key = "CosasChidas"
#login 
#select name from user where name = p_name and pwd = p_pwd
#Primero
#Haciendo QR para validacion en APP de Autenticacion
uri = pyotp.totp.TOTP(key).provisioning_uri(name="Brenzon",
                                            issuer_name="Prueba_Casa")
print(uri)
#qrcode.make(uri).save("TIMEOTP.png") #Solo para guardar el QR una vez

timeotp = pyotp.TOTP(key)

while True:
    print(timeotp.verify(input("Ingrese Codigo Chido: ")))