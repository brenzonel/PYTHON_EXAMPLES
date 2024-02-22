#Pruebas con range
#list = ['Prueba', "Prueba 2", 'Prueba', 'Extraño', "Extraño"]
#for i in range (len(list)):
#    print(i, list[i])

for n in range (2, 20):
    for i in range (2, n):
        if n % i == 0:
            print(n, 'igual', i, '*', n//i)
            break
    else:
        print(n, 'Es numero primo')