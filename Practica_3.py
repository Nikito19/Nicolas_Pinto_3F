# Cree una funcion que calcule el promedio de N notas
def calcular_promedio_notas(*notas):
    if len(notas) == 0:
        print("No se ingresaron notas.")
        return 0
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas es: {promedio}")
    return promedio


# Cree una funcion que determine si un color es primario o no, se debe imprimir por pantalla la leyenda “ el X primero no primario” 

def es_color_primario(color):
    colores_primarios = ["rojo", "azul", "amarillo"]
    
    if color.lower() in colores_primarios:
        print(f"El color {color} es primario.")
    else:
        print(f"El color {color} no es primario.")


# Cree una funcion que determine numero de una serie N numeros es mayor 

def calcular_mayor_numero(*numeros):
    if len(numeros) == 0:
        print("No se ingresaron números.")
        return None
    mayor = max(numeros)
    print(f"El número mayor es: {mayor}")
    return mayor

# Cree una funcion que dibuje un rectangulo de X filas y columnas determinadas por el usuario

def dibujar_rectangulo(filas, columnas):
    for i in range(filas):
        print('x' * columnas)
    print(f"Rectángulo de {filas} filas y {columnas} columnas")

# Cree una funcion que calcule el Factorial de un numero entero positivo

def calcular_factorial(n):
    if  n < 0:
        print("El número debe ser un entero positivo.")
        return
    elif n == 0 or n == 1:
        print(f"El factorial de {n} es: 1")
        return
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        print(f"El factorial de {n} es: {factorial}")
        return


print("Ejercicio 1 ")
calcular_promedio_notas(5, 4, 10)
print()

print("Ejercicio 2 ")
es_color_primario("rojo") 
es_color_primario("Negro") 
print()

print("Ejercicio 3 ")
calcular_mayor_numero(5, 4, 10)
print()

print("Ejercicio 4 ")
dibujar_rectangulo(5, 5)
print()

print("Ejercicio 5 ")
calcular_factorial(3)
