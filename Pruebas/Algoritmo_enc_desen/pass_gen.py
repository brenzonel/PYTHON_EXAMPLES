import random

letras_min = "abcdefghijklmnopqrstuvwxyz"
letras_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
simbolos = "!#@()."

def crea_pass (longuitud):
    lenguaje = letras_min + letras_may + simbolos
    passw = ""
    for _ in range(longuitud):
        passw += random.choice(lenguaje)
    return passw

new_pass = crea_pass(7)
print(new_pass)