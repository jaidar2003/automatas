import itertools

A = ['a', 'b', 'c', 'd']
B = ['0', '1', '2', '3', '4']

union_AB = set(A) | set(B)
interseccion_AB = set(A) & set(B)

concatenacion_AB = [(a, b) for a in A for b in B]

potencia_A3 = [(a1, a2, a3) for a1 in A for a2 in A for a3 in A]

potencia_B2 = [(b1, b2) for b1 in B for b2 in B]

potencia_B0 = ['']

cerradura_kleene_interseccion_AB = ['']
temp = set(A) & set(B)
for i in range(1, 4):
    for subset in itertools.product(temp, repeat=i):
        cerradura_kleene_interseccion_AB.append(''.join(subset))

print("Unión de A y B:", union_AB)
print("Intersección de A y B:", interseccion_AB)

print("Concatenación de A y B:")
for pair in concatenacion_AB:
    print(pair)

print("Potencia de A (A3):")
for triple in potencia_A3:
    print(triple)

print("Potencia de B (B2):")
for pair in potencia_B2:
    print(pair)

print("Potencia de B (B0):", potencia_B0)

print("Cerradura de Kleene de B (A ∩ B)*:", cerradura_kleene_interseccion_AB)

