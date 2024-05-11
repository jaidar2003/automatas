class AutomataNumero:

    def __init__(self):
        self.tabla = [
            [2, 1, 1, None, None, None],
            [2, None, None, None, None, None],
            ['acepta', 'acepta', 'acepta', 'acepta', 'acepta', 'acepta']
        ]
        self.estado_actual = 0

    def transicion(self, entrada):
        if entrada.isdigit():
            columna = 0
        elif entrada == '+' or entrada == '-':
            columna = 1
        elif entrada == '.':
            columna = 2
        elif entrada.lower() == 'e':
            columna = 3
        elif entrada == '':
            columna = 4
        else:
            columna = 5

        try:
            self.estado_actual = self.tabla[self.estado_actual][columna]
            if self.estado_actual == 'acepta':
                return  # No need to proceed if the final state is reached
        except (IndexError, TypeError):
            print(f"Entrada no válida: {entrada}")
            self.estado_actual = None

    def es_aceptado(self):
        return self.estado_actual == 'acepta'


def reconocer_numero(cadena):
    automata = AutomataNumero()
    for caracter in cadena:
        automata.transicion(caracter)
        if automata.estado_actual is None:
            return False  # If at any point the state becomes None, return False
    return automata.es_aceptado()


# Ejemplo de uso
numeros = ["123", "+123", "-123", "12.34", "+12.34", "-12.34", "1.2e3", "+1.2e3", "-1.2e3"]
for numero in numeros:
    if reconocer_numero(numero):
        print(f"'{numero}' es un número válido.")
    else:
        print(f"'{numero}' no es un número válido.")


#jma