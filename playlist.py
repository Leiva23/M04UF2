#!/usr/bin/python3

version = 0.5

app_title = "Playlist v"+str(version)

print(app_title)
print("-"* len(app_title))

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

contador = 10
while contador > 0:
    print(contador)
    contador-=1
print("--------")
for num in range(10): #range(INICIAL, FIN, PASOS)
    print(num)
