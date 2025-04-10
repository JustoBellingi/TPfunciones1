def calcular_imc(peso, altura):
    return peso / (altura**2)
peso = float(input('Ingresa tu peso en kilogramos: ' ))
altura = float(input('Ingresa tu altura en metros: ' ))
icm = calcular_imc(peso, altura)

print (f'Tu imc es: {icm} ')
