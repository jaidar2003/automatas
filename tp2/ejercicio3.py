from collections import defaultdict, deque

nfa = {
    1: {'ε': [2]},
    2: {'a': [3]},
    3: {'ε': [2, 4]},
    4: {}
}

nfa_estado_inicial = 1
nfa_estados_aceptacion = {4}


def cierre_epsilon(nfa, estados):
    pila = list(estados)
    cierre = set(estados)
    while pila:
        estado = pila.pop()
        for siguiente_estado in nfa.get(estado, {}).get('ε', []):
            if siguiente_estado not in cierre:
                cierre.add(siguiente_estado)
                pila.append(siguiente_estado)
    return cierre


def mover(nfa, estados, simbolo):
    siguientes_estados = set()
    for estado in estados:
        for siguiente_estado in nfa.get(estado, {}).get(simbolo, []):
            siguientes_estados.add(siguiente_estado)
    return siguientes_estados


def nfa_a_dfa(nfa, estado_inicial, estados_aceptacion):
    dfa = {}
    dfa_estados_aceptacion = set()
    cierre_inicial = frozenset(cierre_epsilon(nfa, {estado_inicial}))
    dfa_estados = {cierre_inicial: 0}
    dfa_cola = deque([cierre_inicial])
    dfa_estado_inicial = 0
    contador_estados = 1

    while dfa_cola:
        actual = dfa_cola.popleft()
        dfa[dfa_estados[actual]] = {}
        for simbolo in ['a']:
            siguiente_cierre = frozenset(cierre_epsilon(nfa, mover(nfa, actual, simbolo)))
            if siguiente_cierre:
                if siguiente_cierre not in dfa_estados:
                    dfa_estados[siguiente_cierre] = contador_estados
                    dfa_cola.append(siguiente_cierre)
                    contador_estados += 1
                dfa[dfa_estados[actual]][simbolo] = dfa_estados[siguiente_cierre]
                if siguiente_cierre & estados_aceptacion:
                    dfa_estados_aceptacion.add(dfa_estados[siguiente_cierre])

    return dfa, dfa_estado_inicial, dfa_estados_aceptacion


dfa, dfa_estado_inicial, dfa_estados_aceptacion = nfa_a_dfa(nfa, nfa_estado_inicial, nfa_estados_aceptacion)
print("DFA:", dfa)
print("Estado inicial del DFA:", dfa_estado_inicial)
print("Estados de aceptación del DFA:", dfa_estados_aceptacion)


def validar_dfa(dfa, estado_inicial, estados_aceptacion, cadena):
    estado_actual = estado_inicial
    for caracter in cadena:
        if caracter in dfa[estado_actual]:
            estado_actual = dfa[estado_actual][caracter]
        else:
            return False
    return estado_actual in estados_aceptacion


cadenas_prueba = ["", "a", "aa", "aaa", "b"]
for cadena_prueba in cadenas_prueba:
    es_valida = validar_dfa(dfa, dfa_estado_inicial, dfa_estados_aceptacion, cadena_prueba)
    print(f'La cadena "{cadena_prueba}" es {"válida" if es_valida else "inválida"} según el DFA.')
