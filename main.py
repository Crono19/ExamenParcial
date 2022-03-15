# Mensajes de bienvenida

print("Este progama mostrará la cantidad de veces 'Hola mundo', que usted desee")
print("")

# Solicito número de veces
numero = int(input("Ingrese la cantidad de veces que desea ver el mensaje: "))

cont = 0

# Inicio ciclo
while cont < numero:
    print(f"Hola mundo número {cont + 1}")
    cont += 1
