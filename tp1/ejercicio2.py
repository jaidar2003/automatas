import itertools

# Definición de los conjuntos A y B
A = ['a', 'b', 'c', 'd']
B = ['0', '1', '2', '3', '4']

# Operaciones requeridas
union_AB = set(A) | set(B)  # Unión de A y B
interseccion_AB = set(A) & set(B)  # Intersección de A y B

# Concatenación de A y B
concatenacion_AB = [(a, b) for a in A for b in B]

# Potencia de A (A3)
potencia_A3 = [(a1, a2, a3) for a1 in A for a2 in A for a3 in A]

# Potencia de B (B2)
potencia_B2 = [(b1, b2) for b1 in B for b2 in B]

# Potencia de B (B0)
potencia_B0 = ['']  # Cadena vacía

# Cerradura de Kleene de B (A ∩ B)*
cerradura_kleene_interseccion_AB = ['']  # Cadena vacía
temp = set(A) & set(B)
for i in range(1, 4):  # Suponiendo una longitud máxima de 3 para la cadena
    for subset in itertools.product(temp, repeat=i):
        cerradura_kleene_interseccion_AB.append(''.join(subset))

# Mostrar resultados
# Unión de A y B
print("Unión de A y B:", union_AB)

# Intersección de A y B
print("Intersección de A y B:", interseccion_AB)

# Concatenación de A y B
print("Concatenación de A y B:")
for pair in concatenacion_AB:
    print(pair)

# Potencia de A (A3)
print("Potencia de A (A3):")
for triple in potencia_A3:
    print(triple)

# Potencia de B (B2)
print("Potencia de B (B2):")
for pair in potencia_B2:
    print(pair)

# Potencia de B (B0)
print("Potencia de B (B0):", potencia_B0)

# Cerradura de Kleene de B (A ∩ B)*
print("Cerradura de Kleene de B (A ∩ B)*:", cerradura_kleene_interseccion_AB)
