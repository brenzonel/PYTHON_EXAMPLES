#Python prueba de IFs
x = int(input("Please enter an integer: "))

while x > 0 :
    if x == 0:
        print('Var is Zero')
    elif x == 1:
        print('Var is One')
    else:
        print('Var is more than 1')

    x = int(input("Please enter an integer: "))
    if x <= 0:
        print('Adios')