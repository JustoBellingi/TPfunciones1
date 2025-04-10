import math


def calcularArea_circulo(radio):
    return math.pi * radio**2


def calcularPerimetro_circulo(radio):
    return math.pi * radio


radio = float(input("Ingresa la medida del radio: "))

area = calcularArea_circulo (radio)
perimetro = calcularPerimetro_circulo (radio)


print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")
