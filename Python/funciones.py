def myFunction(nombre):
    print("Hola " + nombre)

myFunction("Luis")

def suma(num1 , num2):
    resultado = num1 + num2
    return resultado

print(suma(4, 8))

print("------------------")

def printColores(*colores):
    print("Tu color es: " + colores[1] + ", "+ colores[2])

printColores("red", "blue", "green")

print("------------------")

def miNombre(nombre = "Luis"):
    print("Mi nombre es: " + nombre)

miNombre("Manuel")
miNombre("Carmen")
miNombre()