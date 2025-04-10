def segundos_a_horas (segundos):
    return segundos / 3600

segundos = (float(input("Ingresa la cantidad de segundos: ")))

horas = segundos_a_horas(segundos)

print(f"{segundos} segundos es igual a esta cantidad de {horas} horas.")
