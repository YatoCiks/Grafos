#-----------------------------------------------------
class Matriz():
    """Matriz de Adjacencia"""
    def __init__(self, vertice):
        self.vertice = vertice
        self.grafo = []
        for i in range(self.vertice):
            nova_linha = []
            for j in range(self.vertice):
                nova_linha.append(0)
            self.grafo.append(nova_linha)
            
    def mostrar_grafo(self):
        print("#--------------------- Matriz de Adjacencia ---------------------#")
        for i in range(self.vertice):
            print(self.grafo[i])
            
    def adicionar_aresta(self, linha, coluna):
        self.grafo[linha - 1][coluna - 1] += 1
        self.grafo[coluna - 1][linha - 1] += 1
        
    def converter_lista(self):
        lista = Lista(self.vertice)
        for i in range(self.vertice):
            for j in range(self.vertice):
                if self.grafo[i][j] != 0:
                    lista.grafo[i].append(j+1)
        
        return lista


        

class Lista():
    """Lista de Adjacencia"""
    def __init__(self, vertice):
        self.vertice = vertice
        self.grafo = []
        for i in range(self.vertice):
            self.grafo.append([])
            
    def mostrar_grafo(self):
        print("#--------------------- Lista de Adjacencia ----------------------#")
        for i in range(self.vertice):
            print(self.grafo[i])



#-----------------------------------------------------

print("Questao 1")
matriz_q1 = Matriz(6)
matriz_q1.adicionar_aresta(1, 4)
matriz_q1.adicionar_aresta(1, 5)
matriz_q1.adicionar_aresta(1, 6)
matriz_q1.adicionar_aresta(2, 3)
matriz_q1.adicionar_aresta(2, 4)
matriz_q1.adicionar_aresta(2, 5)
matriz_q1.adicionar_aresta(3, 4)
matriz_q1.adicionar_aresta(3, 5)
matriz_q1.adicionar_aresta(4, 6)
matriz_q1.adicionar_aresta(5, 6)

matriz_q1.mostrar_grafo()
lista_q1 = matriz_q1.converter_lista()
print("")
lista_q1.mostrar_grafo()

print("")

print("Questao 2")
matriz_q2 = Matriz(4)
matriz_q2.adicionar_aresta(1, 2)
matriz_q2.adicionar_aresta(1, 3)
matriz_q2.adicionar_aresta(1, 4)
matriz_q2.adicionar_aresta(2, 3)
matriz_q2.adicionar_aresta(2, 4)
matriz_q2.adicionar_aresta(4, 3)


matriz_q2.mostrar_grafo()
lista_q2 = matriz_q2.converter_lista()
print("")
lista_q2.mostrar_grafo()

























