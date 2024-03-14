import bcrypt

txt = input("Clave a encriptar: ")
pass1 = txt.encode("utf-8")
sal = bcrypt.gensalt()
encript = bcrypt.hashpw(pass1, sal)
print (encript)

pass2 = b'$2b$12$bFGHunwKYM6nm9b7w32zrOtC.AsFmwErjYr.wGRZoIOQgONcSOhq2' #obtener el strig en byte
print (pass2)
txt = bytes(input("Clave de acceso: "), 'utf-8')
if bcrypt.checkpw(txt, encript):
    print ("Clave correcta")
else:
    print ("Clave incorrecta")
    