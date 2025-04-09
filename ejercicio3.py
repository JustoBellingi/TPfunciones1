def saludar_usuario(nombre):
    return f'Soy {nombreUsuario} {apellidoUsuario}, tengo {edadUsuario} y vivo en {vivenciaUsuario}'

nombreUsuario = input("ingresa un nombre: ")
apellidoUsuario = input("ingresa un apellido: ")
edadUsuario = input("ingresa una edad: ")
vivenciaUsuario = input("ingresa una vivienda: ")
saludar = saludar_usuario(nombreUsuario)
print (saludar)
