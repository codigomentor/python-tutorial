texto1 = "Hola, mundo"
texto2 = "   Hola, mundo  "
# print(len(texto))
# print(texto[1:3]) # ol
# print(texto[-4:-2]) # un

print(len(texto1))
print(len(texto2.strip()))

print(texto1.lower())
print(texto1.upper())

print(texto1.replace("H", "X"))

print(texto1.split(","))
print(type(texto1.split(",")))
print("----------------")

isPresent = "mun" not in texto1
print(isPresent) # True

print("Tu eres el \"mejor\"")

#Boolean
print(10 > 5) # True
print(10 > 20) # False
