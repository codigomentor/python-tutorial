contador = 0

while contador <= 10:
    contador += 1
    if contador == 5:
        continue
    print(contador) # 1 2 ... 9 10 11

# for
print("---------------------------")
colores = ["red", "blue", "green"]

for color in colores:
    if color == "blue":
        continue
    print(color)

texto = "computadora"

for n in texto:
    print(n)

#range

for numero in range(5):
    print(numero)