def tabla_multiplicar (numero):
    for num in range(1, 11):     
       print (f"{numero} * {num} la tabla de multiplicar de este numero es {numero * num}")
numero = int(input("Ingresa un numero para multiplicar: "))
tabla_multiplicar (numero)
