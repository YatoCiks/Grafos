INF = 99999

class Vertice:
    def __init__(self, id) -> None:
        self.id = id
        self.estimativa = INF
        self.predecessor = -1
        self.aberto = True

class Grafo:
    def __init__(self, vertices, adjacencias) -> None:
        self.vertices = vertices
        self.adjacencias = adjacencias

# Inicialiacao
vertices = []

for i in range(6):
    v = Vertice(i)
    vertices.append(v)

# Lista de adjacencia com pesos
# Formato [V0, V1, Peso]
adjacencias = []
def add_adjacencia(va, vb, peso):
    adjacencias.append([va, vb, peso])
    adjacencias.append([vb, va, peso])

add_adjacencia(0, 1, 10)
add_adjacencia(0, 2, 5)
add_adjacencia(1, 3, 1)
add_adjacencia(1, 2, 3)
add_adjacencia(2, 3, 8)
add_adjacencia(2, 4, 2)
add_adjacencia(3, 4, 4)
add_adjacencia(3, 5, 4)
add_adjacencia(4, 5, 6)

grafo = Grafo(vertices, adjacencias)

grafo.vertices[0].estimativa = 0

abertos = 0
for i in grafo.vertices:
    abertos += 1

# Algoritmo
''' Passo a passo
    1 - Verificar se existem vertices abertos
    2 - Achar vertice com a menor estimativa
    3 - Fechar ele
    4 - Atualizar as estimativas dos vertices adjacentes ao vertice fechado
    4 - Repete os passos anteriores
'''

while(abertos > 0):
    menor_estimativa = INF
    vertice_estimativa = -1
# Vertice a ser fechado
    for i in grafo.vertices:
        if i.estimativa < menor_estimativa and i.aberto == True:
            menor_estimativa = i.estimativa
            vertice_estimativa = i.id
            print(F"vertice: {i.id}, estimativa: {i.estimativa}")
    
    print(F"vertice fechado: {grafo.vertices[vertice_estimativa].id}")

    grafo.vertices[vertice_estimativa].aberto = False
    abertos -= 1
# Atualizacao das estimativas
    for i in grafo.adjacencias:
        if i[0] == vertice_estimativa and grafo.vertices[i[1]].aberto == True: 
            vertice = i[1]
            peso = i[2]
            if peso < grafo.vertices[vertice].estimativa:
                grafo.vertices[vertice].estimativa = grafo.vertices[vertice_estimativa].estimativa + peso
                grafo.vertices[vertice].predecessor = vertice_estimativa
# Exibicao    
for i in grafo.vertices:
    print(F"vertice: {i.id}, estimativa: {i.estimativa}, predecessor: {i.predecessor}")

print(abertos)