Edad = float(input("Introduce un número: "))

if Edad <= 0:
    print('edad invalida')
elif Edad < 13:
    print('nino')
elif Edad < 18:
    print('adolecente')
elif Edad < 65:
    print('Adulto')
else:
    print('Adulto Mayor')