class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
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
        return 7


def obtener_fila(no_terminal):
    if no_terminal == 'E':
        return 0
    elif no_terminal == 'E\'':
        return 1
    elif no_terminal == 'T':
        return 2
    elif no_terminal == 'F':
        return 3
    else:
        return 4


tabla = [
    ["TE'", "", "", "", "TE'", "", ""],
    ["", "+TE'", "-TE'", "%TE'", "", "ε", "ε"],
    ["F", "", "", "", "F", "", ""],
    ["id", "", "", "", "(E)", "", ""]
]


def tokenizar(expresion):
    tokens = []
    i = 0
    while i < len(expresion):
        if expresion[i].isdigit():
            num = ""
            while i < len(expresion) and expresion[i].isdigit():
                num += expresion[i]
                i += 1
            tokens.append('id')
        elif expresion[i] in "+-%()":
            tokens.append(expresion[i])
            i += 1
        else:
            i += 1
    tokens.append('$')
    return tokens


def analizar_entrada(entrada):
    p = Pila()
    p.insertar('$')
    p.insertar('E')
    idx = 0
    while not p.estaVacia():
        cima_pila = p.inspeccionar()
        simbolo_entrada = entrada[idx]
        if cima_pila in ['E', 'E\'', 'T', 'F']:
            fila = obtener_fila(cima_pila)
            col = obtener_col(simbolo_entrada)
            produccion = tabla[fila][col]
            if produccion != '':
                p.extraer()
                if produccion != 'ε':
                    for simbolo in reversed(produccion):
                        p.insertar(simbolo)
            else:
                print("Error en la entrada.")
                return False
        elif cima_pila == simbolo_entrada:
            p.extraer()
            idx += 1
        else:
            print("Error en la entrada.")
            return False
    return True


def evaluar_expresion(expresion):
    def evaluar(tokens):
        def siguiente():
            return tokens.pop(0)

        def factor():
            token = siguiente()
            if token == '(':
                resultado = expresion()
                siguiente()  # consumir ')'
                return resultado
            else:  # es un número
                return int(token)

        def termino():
            resultado = factor()
            while tokens and tokens[0] == '%':
                siguiente()  # consumir '%'
                resultado = resultado % factor()
            return resultado

        def expresion():
            resultado = termino()
            while tokens and tokens[0] in ('+', '-'):
                if tokens[0] == '+':
                    siguiente()  # consumir '+'
                    resultado += termino()
                elif tokens[0] == '-':
                    siguiente()  # consumir '-'
                    resultado -= termino()
            return resultado

        return expresion()

    tokens = []
    num = ""
    for char in expresion:
        if char.isdigit():
            num += char
        else:
            if num:
                tokens.append(num)
                num = ""
            tokens.append(char)
    if num:
        tokens.append(num)

    return evaluar(tokens)


# Probar la calculadora
expresion = "10+5-2"
resultado = evaluar_expresion(expresion)
print("Resultado:", resultado)  # Resultado: 13

entrada = tokenizar(expresion)
if analizar_entrada(entrada):
    print("Entrada aceptada.")
else:
    print("Error en la entrada.")

# Evaluar la expresión
resultado = evaluar_expresion(expresion)
print("Resultado:", resultado)
