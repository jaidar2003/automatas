import random

# Definir el alfabeto
alfabeto = ['a', 'b', 'c', 'd', '0', '1', '2', '3', '4']

# Función para generar una cadena aleatoria de longitud dada
def generar_cadena(longitud):
    return ''.join(random.choice(alfabeto) for _ in range(longitud))

# Generar las dos cadenas x e y aleatorias
x = generar_cadena(random.randint(1, 10))  # Longitud de x aleatoria entre 1 y 10
y = generar_cadena(random.randint(1, 10))  # Longitud de y aleatoria entre 1 y 10

# Mostrar las cadenas generadas y sus longitudes
print("Cadena x:", x)
print("Longitud de x:", len(x))
print("Cadena y:", y)
print("Longitud de y:", len(y))

# Concatenación de x e y
xy = x + y
print("Concatenación de x e y:", xy)

# Potencias
x0 = ""
x1 = x
y2 = y + y
y3 = y + y + y
xx = x + x
yx = y + x

print("x^0:", x0)
print("x^1:", x1)
print("y^2:", y2)
print("y^3:", y3)
print("xx:", xx)
print("yx:", yx)
