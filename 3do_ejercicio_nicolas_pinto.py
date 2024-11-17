import random

# Inicializar el número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 50)
intentos = 0
max_intentos = 5

print("¡Bienvenido al juego de adivinar el número!")
print(f"Tienes {max_intentos} intentos para adivinar un número entre 1 y 50.")

while intentos < max_intentos:
    # Solicitar al jugador que ingrese un número
    try:
        numero_jugador = int(input(f"Intento {intentos + 1}/{max_intentos}: Ingrese un número entre 1 y 50: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    # Verificar que el número ingresado esté dentro del rango
    if numero_jugador < 1 or numero_jugador > 50:
        print("El número debe estar entre 1 y 50. Inténtelo de nuevo.")
        continue
    
    # Incrementar el contador de intentos
    intentos += 1
    
    # Comparar el número del jugador con el número secreto
    if numero_jugador == numero_secreto:
        print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        break
    elif numero_jugador < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    # Verificar si se han alcanzado los intentos máximos
    if intentos == max_intentos:
        print(f"Lo siento, has alcanzado el límite de intentos. El número secreto era {numero_secreto}.")
