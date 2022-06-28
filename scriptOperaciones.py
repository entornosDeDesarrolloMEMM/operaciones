from operacionesBasicas import *
from random import uniform
from math import pow

print("Bienvenid@ a la calculadora de Manu")

while True:
    continuar = "s"

    num1 = uniform(0, 10)
    num2 = uniform(0, 10)

    print(f"Operando 1: {num1:.2f}")
    print(f"Operando 2: {num2:.2f}")

    print("""Dispone de las siguientes opciones:
    [1] Suma
    [2] Resta
    [3] Multiplicación
    [4] División
    [5] Potencia""")

    while continuar == "s":
        opcion = input("Indique opción: ")
        while opcion not in ("1", "2", "3", "4", "5"):
            opcion = int(
                input("Opción incorrecta. Introduzca una opción correcta: "))

        if opcion == "1":
            print(f"{num1:.2f} + {num2:.2f} = {suma(num1, num2):.2f}")
        elif opcion == "2":
            print(f"{num1:.2f} - {num2:.2f} = {resta(num1, num2):.2f}")
        elif opcion == "3":
            print(f"{num1:.2f} * {num2:.2f} = {producto(num1, num2):.2f}")
        elif opcion == "4":
            print(f"{num1:.2f} : {num2:.2f} = {division(num1, num2):.2f}")
        elif opcion == "5":
            print(f"{num1:.2f} ^ {num2:.2f} = {pow(num1, num2):.2f}")

        continuar = input("¿Desea realizar más operaciones"
                          "con los mismos operandos (S/N)?").lower()

    salir = input("¿Desea salir del programa (S/N)?").lower()
    if salir == "s":
        print("Programa finalizado")
        break
