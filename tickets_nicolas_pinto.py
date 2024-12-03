import pickle
import sys
import os
import random


ARCHIVO_TICKETS = "tickets.pkl"


def limpiar_pantalla():
    os.system("clear" if os.name == "posix" else "cls")


def cargar_tickets():
    if os.path.isfile(ARCHIVO_TICKETS):
        with open(ARCHIVO_TICKETS, "rb") as f:
            return pickle.load(f)
    return {}


def guardar_tickets():
    with open(ARCHIVO_TICKETS, "wb") as f:
        pickle.dump(tickets, f)


tickets = cargar_tickets()

def alta_ticket():
    while True:
        limpiar_pantalla()
        print("--- Alta de Ticket ---")
        nombre = input("Ingrese su nombre: ")
        sector = input("Ingrese el sector: ")
        asunto = input("Ingrese el asunto: ")
        problema = input("Describa el problema: ")
        
        
        numero_ticket = random.randrange(1000, 9999)
        
       
        tickets[numero_ticket] = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Problema": problema
        }
        
        
        guardar_tickets()
        
        
        print(f"\nTicket creado exitosamente. Número de ticket: {numero_ticket}")
        print("Detalles del ticket guardado:")
        print(f"Nombre: {nombre}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Problema: {problema}")
        print("\nPor favor, recuerde este número para futuras consultas.\n")
        
        
        continuar = input("¿Desea crear otro ticket? (s/n): ").strip().lower()
        if continuar != 's':
            break

def leer_ticket():
    while True:
        limpiar_pantalla()
        print("--- Leer Ticket ---")
        try:
            numero_ticket = int(input("Ingrese el número de ticket: "))
            if numero_ticket in tickets:
                ticket = tickets[numero_ticket]
                print("\n--- Detalles del Ticket ---")
                for key, value in ticket.items():
                    print(f"{key}: {value}")
            else:
                print("El número de ticket no existe.\n")
        except ValueError:
            print("Debe ingresar un número válido.\n")
        
        
        continuar = input("¿Desea leer otro ticket? (s/n): ").strip().lower()
        if continuar != 's':
            break

def salir():
    limpiar_pantalla()
    confirmacion = input("\n¿Está seguro que desea salir? (s/n): ").strip().lower()
    if confirmacion == 's':
        print("¡Gracias por usar el sistema de tickets!")
        sys.exit()


def menu():
    while True:
        limpiar_pantalla()
        print("   Hola bienvenido al sistema de tickets  ")
        print(" ")
        print("1. Generar Nuevo Ticket")
        print("2. Leer Ticket")
        print("3. Salir")
        
       
        try:
            opcion = int(input("Seleccione una opción: ").strip())
            if opcion == 1:
                alta_ticket()
            elif opcion == 2:
                leer_ticket()
            elif opcion == 3:
                salir()
            else:
                print("\nError: Opción no válida. Por favor, seleccione una opción entre 1 y 3.\n")
                input("Presione Enter para continuar...")
        except ValueError:
            print("\nError: Entrada inválida. Por favor, ingrese un número entre 1 y 3.\n")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    menu()
