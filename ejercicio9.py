def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = float(input("Ingresa la temperatura en grado celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C es igual a {fahrenheit}°F")
