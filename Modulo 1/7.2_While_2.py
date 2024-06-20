num_sec = 2
adivinado = False
num1 = int(input("Introduce el primer número: "))

while not adivinado:
    if num_sec == num1:
        print('FELICIDADES')     
    adivinado = True
    
else:
    print('INTENTA DENUEVO')



