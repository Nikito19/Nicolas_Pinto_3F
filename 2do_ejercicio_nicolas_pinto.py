print("//// 1er Ejercicio ////")
numero= int(input("Decime un numero: "))

if numero % 2 == 0:
     print(f"El Numero {numero} es PAR")
else:
    print(f"El Numero {numero} es IMPAR")

print(" ")
print("//// 2do Ejercicio ////")
numero2 = int(input("Ahora Dame un número y te genero su tabla de multiplicar: "))
contador = 1

while contador <= 10:
    resultado = numero2 * contador
    print(f"{numero2} x {contador} = {resultado}")
    contador += 1

print(" ")
print("//// 3er Ejercicio ////")
nombre = input( "Decime tu Nombre:" )
numero= int(input("Decime tu edad: "))

if numero >= 18:

     print(f"{nombre} sos Mayor de edad")
else:
    print(f"{nombre} sos Menor de edad")


print(" ")
print("//// 4to Ejercicio ////")
text = input( "Decime una palabra:" )
contador= 0

corte = int(input("Decime cuantas veces qeueres que la repita: "))

while contador < corte:
    print(text) 
    contador += 1 



print(" ")
print("//// 5to Ejercicio ////")
numero3 = int(input("Ingresa un numero: "))
suma = 0

while numero3 != 0:
    suma += numero3  
    numero3 = int(input("ingresa otro numero para sumarle o si queres finalizar 0: "))

print(f"La suma total de los números ingresados es: {suma}")

