def calcular_promedio(a, b, c):
    return (a + b + c) / 3


a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))


promedio = calcular_promedio(a, b, c)

print(f"El promedio es: {promedio}")
