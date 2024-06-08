def obtener_col(simbolo_entrada):
    if simbolo_entrada == 'i':
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
    if (no_terminal == "E"):
        return 0
    else:
        if (no_terminal == "E!"):
            return 1
        else:
            if (no_terminal == "T"):
                return 2
            else:
                if (no_terminal == "T!"):
                    return 3
                else:
                    if (no_terminal == "F"):
                        return 4
                    else:
                        return 5


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


def analisis_sintactico(expresion):
    entrada = []
    tabla = [
        ["E->TE!", "", "", "", "E->TE!", "", ""],
        ["", "E!->+TE!", "E'->-TE!", "", "", "E!->e", "E!->e"],
        ["T->FT!", "", "", "", "T->FT!", "", ""],
        ["", "T!->e", "T!->e", "T!->%FT!", "", "T!->e", "T!->e"],
        ["F->i", "", "", "", "F->(E)", "", ""],
    ]

    for j in expresion:
        if j == ' ':
            pass
        else:
            entrada.append(j)
    entrada.append('$')
    for i in entrada:
        if i.isdigit():
            entrada[entrada.index(i)] = 'i'

    p = Pila()
    p.insertar('$')
    p.insertar('E')
    iter = 0
    entr = 0
    flag = False
    flag1 = False

    while p.inspeccionar() != '$':
        iter += 1

        if obtener_fila(p.inspeccionar()) != 5:

            print("Pila: ", p.contenido())
            print("Entrada: ", entrada)
            print("Salida: ", tabla[obtener_fila(p.inspeccionar())][obtener_col(entrada[0])])
            print("--------------------------------------------------")

            if p.inspeccionar() == "!":
                flag1 = True
                pass
            if p.inspeccionar() != entrada[0]:
                if flag1 == True:
                    salida = tabla[obtener_fila(str(p.inspeccionar() + "!"))][obtener_col(entrada[0])]
                    flag1 = False
                else:
                    salida = tabla[obtener_fila(p.inspeccionar())][obtener_col(entrada[0])]
                p.extraer()
                for ii in (salida[::-1]):
                    if ii == ">":
                        break
                    elif flag == True:
                        nuevo = str(ii + "!")
                        if ii != "e":
                            p.insertar(nuevo)
                            flag = False
                    elif ii == "!":
                        flag = True
                        pass
                    else:
                        if ii != "e":
                            p.insertar(ii)
        else:
            p.extraer()
            entr += 1
            entrada.pop(0)


def calculadora(expresion):
    print(f"El resultado de la expresión es = {eval(expresion)}")
    pass

analisis_sintactico("6 + ( 5 % 2 ) - 3")
calculadora("6  + ( 5 % 2 ) - 3")
