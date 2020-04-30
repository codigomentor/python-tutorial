colores = ["red", "blue", "green", "yellow", "red123"]
print(len(colores))
print(colores[2])
print(colores[-1]) # red
print(colores[1:4]) # "blue", "green", "yellow"

colores[1] = "WHITE"
print(colores)

colores.append("brown")
print(colores)

colores.insert(1, "NUEVO")
print(colores)

colores.remove("red")
print(colores)

colores.pop()
print(colores)

colores.clear()
print(colores)
print(len(colores))

print("----------------------")
# tuples

animales = ("perro", "gato", "conejo")
print(len(animales)) # 3
print(animales[0])
print(animales[1])
print(animales[2])

#animales[0] = "NUEVO" # error
#print(animales)

print(type(animales))

for animal in animales:
    print(animal)

if "perro" in animales:
    print("El animal perro se encuentra en el tuple")

print("----------------------")
numeros = ("uno",)
print(type(numeros)) 

print("----------------------")
#diccionarios

persona = {
     "nombre" : "Luis",
     "edad"   : 20,
     "hobby"  : "cantar"
    }

print(persona)
print(persona["nombre"]) # Luis
print(persona.get("nombre")) # Luis
print(persona.values()) 

for a , b in persona.items():
    print(a , b)