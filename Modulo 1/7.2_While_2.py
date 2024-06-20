num_sec = 2
adivinado = False

while not adivinado:
    num1 = int(input("Introduce el primer número: "))
    if num_sec == num1:
        print('FELICIDADES')     
        adivinado = True     
    else:
        print('INTENTA DENUEVO')
