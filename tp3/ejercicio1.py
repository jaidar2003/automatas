class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def insertar(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[-1]

    def tamano(self):
        return len(self.items)

    def contenido(self):
        return self.items


def obtener_col(simbolo_entrada):
    if simbolo_entrada == 'id':
        return 0
    elif simbolo_entrada == '+':
        return 1
    elif simbolo_entrada == '-':
        return 2
    elif simbolo_entrada == '%':
        return 3
    elif simbolo_entrada == '(':
        return 4
    elif simbolo_entrada == ')':
        return 5
    elif simbolo_entrada == '$':
        return 6
    else:
        return -1


def obtener_fila(no_terminal):
    if no_terminal == 'E':
        return 0
    elif no_terminal == "E'":
        return 1
    elif no_terminal == 'T':
        return 2
    elif no_terminal == 'F':
        return 3
    else:
        return -1


# Tabla de análisis sintáctico
tabla = [
    ["E→TE'", "", "", "", "E→TE'", "", ""],
    ["", "E'→+TE'", "E'→-TE'", "E'→%TE'", "", "E'→ε", "E'→ε"],
    ["T→F", "", "", "", "T→F", "", ""],
    ["F→id", "", "", "", "F→(E)", "", ""]
]


def evaluar_expresion(expr):
    def parse_term(index):
        term, index = parse_factor(index)
        while index < len(expr) and expr[index] in ['+', '-', '%']:
            op = expr[index]
            next_term, next_index = parse_factor(index + 1)
            if op == '+':
                term += next_term
            elif op == '-':
                term -= next_term
            elif op == '%':
                term %= next_term
            index = next_index
        return term, index

    def parse_factor(index):
        if expr[index].isdigit():
            start_index = index
            while index < len(expr) and expr[index].isdigit():
                index += 1
            return int(expr[start_index:index]), index
        elif expr[index] == '(':
            term, index = parse_term(index + 1)
            if expr[index] == ')':
                return term, index + 1
        raise ValueError(f"Unexpected character {expr[index]} at index {index}")

    result, _ = parse_term(0)
    return result


# Proceso de análisis
def analizador_entrada(entrada):
    p = Pila()
    p.insertar('$')
    p.insertar('E')

    entrada_2 = entrada + ['$']
    salida = ''

    print('PILA \t\t\t\t ENTRADA \t\t\t\t SALIDA')
    print(f"{str(p.contenido())}\t\t\t{str(entrada_2)}\t\t\t{str(salida)}")

    simbolo_entrada = entrada_2.pop(0)
    while simbolo_entrada:
        cima_pila = p.inspeccionar()
        while cima_pila != simbolo_entrada:
            col = obtener_col(simbolo_entrada)
            fil = obtener_fila(cima_pila)
            if col == -1 or fil == -1:
                print("Error: Símbolo inesperado")
                return False

            salida = tabla[fil][col]
            if salida:
                p.extraer()
                produccion = salida.split('→')[1]
                produccion_pila = []
                i = 0
                while i < len(produccion):
                    if i + 1 < len(produccion) and produccion[i + 1] == "'":
                        produccion_pila.append(produccion[i:i + 2])
                        i += 2
                    else:
                        produccion_pila.append(produccion[i])
                        i += 1
                for simbolo in reversed(produccion_pila):
                    if simbolo != 'ε':
                        p.insertar(simbolo)
            else:
                print("Error: Producción vacía")
                return False  # Error de sintaxis
            print(f"{str(p.contenido())}\t\t\t{str(entrada_2)}\t\t\t{str(salida)}")
            cima_pila = p.inspeccionar()

        if simbolo_entrada == '$' and p.inspeccionar() == '$':
            print("Árbol sintáctico construido!")
            return True

        p.extraer()
        if entrada_2:
            simbolo_entrada = entrada_2.pop(0)
        else:
            simbolo_entrada = None

        print(f"{str(p.contenido())}\t\t\t{str(entrada_2)}\t\t\t")

    return False


# Ejemplo de uso
input_str = "10+5-2"
tokens = []
i = 0
while i < len(input_str):
    if input_str[i].isdigit():
        num = ""
        while i < len(input_str) and input_str[i].isdigit():
            num += input_str[i]
            i += 1
        tokens.append("id")
    else:
        tokens.append(input_str[i])
        i += 1

if analizador_entrada(tokens):
    result = evaluar_expresion(input_str)
    print(f"Resultado: {result}")
else:
    print("Error de sintaxis")
