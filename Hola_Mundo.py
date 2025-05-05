print('Hola Mundo')

edad = 15

if edad >= 18:
   print ("Eres mayor de edad.")

else:
   print ("eres menor de edad.")

calificacion = 90

if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")


frutas = ["manzana", "banana", "naranja"]


for fruta in frutas:
    print(fruta)


contador = 0

while contador < 5:

    print(contador)
    contador += 1

contador = 0


while True:

    print(contador)
    contador +=1 


    if contador == 5:
      break

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

for i in range(5):
    pass

print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"

print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"frutas = ["manzana", "banana", "naranja"]


frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]


fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"


frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]
