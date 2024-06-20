contador=0

while contador < 3 :
    contador += 1
    print(f'invernadero {contador}')
    Temp = int(input("Introduce Temperatura del invernadero: "))
    Hum = int(input("Introduce humedad del invernadero: "))
    
    if Temp> 30:
        if Hum < 30:
            print('recomiendo riego y ventilacion')
        else:
            print('recomiendo ventilacion')
    else:
        if Hum> 30:
            print('recomiendo riego')
        else:
            print('No requiere acciones')







