import random

alfabeto = ['a', 'b', 'c', 'd', '0', '1', '2', '3', '4']

def generar_cadena(longitud):
    return ''.join(random.choice(alfabeto) for _ in range(longitud))

x = generar_cadena(random.randint(1, 10))
y = generar_cadena(random.randint(1, 10))

print("Cadena x:", x)
print("Longitud de x:", len(x))
print("Cadena y:", y)
print("Longitud de y:", len(y))

xy = x + y
print("Concatenación de x e y:", xy)

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


