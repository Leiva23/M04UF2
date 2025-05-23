#!/usr/bin/python3

version = 0.5

app_title = "Playlist v"+str(version)

print(app_title)
print("-"* len(app_title))


def saluda ():
    print("Hola!")

def suma (num1, num2):
    return num1+num2

def despide(quien="Jacinto"):
    print("Estas despedido", quien)

def retorna_multiple ():
    uno = 1
    dos = 3
    return uno,dos

if True:
    print("Cierto")
else:
    print("False")

primero = 5
segundo = 5

if primero>segundo:
    print("El primero es mayor que el segundo")
elif primero < segundo:
    print("El segundo es mayor que el primero")
else:
    print("Son iguales")

hora = 8
match hora:
    case 8:
        print("Desayuno")
    case 14:
        print("Comida")
    case 21:
        print("Cena")
    case _:
        print("No toca comer")
        
contador = 10
while contador > 0:
    print(contador)
    contador-=1
print("--------")
for num in range(10): #range(INICIAL, FIN, PASOS)
    print(num)
    pass

personas = ["jaimito", "Jacinto", "33", "0.9"]
for dato in personas:
    print(">", dato)

personaje = {
    "nombre": "Paquito",
    "edad": 33,
    "pelo": "marron"

}

print ("Personaje:", personaje["nombre"])
    
for clave in personaje:
    print(">>", personaje[clave])

for clave, valor in personaje.items():
    print(">>>", clave, valor)

saluda()

print(suma(3, 5))

despide("Ramiro")

valor1, valor2 = retorna_multiple()

print("Valores:", valor1, valor2)


nombre = input("¿Como te llamas?\n")

print(nombre)
