#Python prueba FOR
#prueba de for en un una lista
#palabras = ['carro', 'ventana', 'diferencia de palabras']
colec_Palabras = {
    'Brandon': 'Activo',
    'Alan': 'Inactivo',
    'De Luna': 'Activo',
    'Almanza': 'Inactivo'
}
#for p in palabras:
#    print(p, len(p))

for user, status in colec_Palabras.copy().items():
    if (status) == 'Inactivo':
        print(user, status)

active_user = {}

for user, status in colec_Palabras.copy().items():
    if (status) == 'Activo':
        active_user [user] = status

print('Usarios Activos: ', active_user)

