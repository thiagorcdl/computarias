"""Implementação de Árvore Binária em Python."""
from ferramentas import gerar_nova_sub_arvore


class Nodo:
    """Elemento de uma árvore, guardando um valor e referenciando outros dois Nodos.

    O nodo da esquerda possui valor menor do que o pai; o da direita, maior.
    """

    def __init__(self, valor):
        """Constrói um nodo com o valor indicado.

        Por padrão, não há filhos.
        """
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.nivel = 0

    def __repr__(self) -> str:
        """Representa a estrutura de uma maneira amigável para imprimir no terminal."""
        return f"<{self.valor}>"

    def buscar(self, valor):
        """Executa uma busca binária para encontrar um nodo que possua o valor
        desejado.
        """
        if valor == self.valor:
            # Valor encontrado
            return self
        elif valor < self.valor and self.esquerda is not None:
            # Valor é menor que o atual, então deve estar no galho à esquerda
            return self.esquerda.buscar(valor)
        elif valor > self.valor and self.direita is not None:
            # Valor é maior que o atual, então deve estar no galho à direita
            return self.direita.buscar(valor)
        else:
            # Valor não existe na árvore
            return None

    def adicionar(self, nodo_filho):
        """Inclui um nodo com valor desejado entre seus filhos.

        A busca é recursiva, até achar um lugar apropriado.
        """
        if nodo_filho.valor < self.valor:
            # Se o novo valor for menor, ele vai para a esquerda
            if self.esquerda is None:
                # Se não tiver nenhum filho à esquerda, ele é colocado ali
                self.esquerda = nodo_filho
                self.esquerda.nivel = self.nivel + 1
            else:
                # Caso exista um filho na esquerda, busca um espaço nesse galho
                self.esquerda.adicionar(nodo_filho)
        elif nodo_filho.valor > self.valor:
            # Se o novo valor for maior, ele vai para a direita
            if self.direita is None:
                # Se não tiver nenhum filho à direita, ele é colocado ali
                self.direita = nodo_filho
                self.direita.nivel = self.nivel + 1
            else:
                # Caso exista um filho na direita, busca um espaço nesse galho
                self.direita.adicionar(nodo_filho)
        else:
            # Novo valor é igual ao atual, ou seja já está na árvore
            nodo_filho = self
        return nodo_filho

    def remover(self, valor):
        """Busca recursivamente até achar o pai do valor a ser removido."""
        nodo_removido = None
        if valor < self.valor and self.esquerda:
            if self.esquerda.valor == valor:
                # Removendo nodo da esquerda, promove algum dos respectivos filhos
                nodo_removido = self.esquerda
                self.esquerda = gerar_nova_sub_arvore(
                    self.esquerda.esquerda, self.esquerda.direita
                )
            else:
                # Continua procurando na esquerda
                nodo_removido = self.esquerda.remover(valor)
        elif valor > self.valor and self.direita:
            if self.direita.valor == valor:
                # Removendo nodo da direita, promove algum dos respectivos filhos
                nodo_removido = self.direita
                self.direita = gerar_nova_sub_arvore(
                    self.direita.esquerda, self.direita.direita
                )
            else:
                # Continua procurando na direita
                nodo_removido = self.direita.remover(valor)

        return nodo_removido


class ArvoreBinaria:
    """Estrutura hieráriquica com um nodo raiz e cada nodo tendo dois subnodos.

    A sub-árvore à esquerda sempre possui valores menores e a sub-árvore à direita
    sempre possui valores maiores que o da raíz (e assim recursivamente).
    """

    def __init__(self):
        """Constrói uma árvore binária vazia."""
        self._raiz = None

    def __repr__(self) -> str:
        """Representa a estrutura de uma maneira amigável para imprimir no terminal."""
        conteudo = f"Raiz: {self._raiz} " if self._raiz else "VAZIA"
        return f"[{self.__class__.__name__} | {conteudo}]"

    @property
    def raiz(self) -> Nodo:
        """Retorna o nodo inicial da árvore, de forma que só possa ser lido."""
        return self._raiz

    def buscar(self, valor) -> Nodo:
        """Retorna o primeiro nodo encontrado com o valor desejado."""
        if self.raiz is not None:
            return self.raiz.buscar(valor)

    def adicionar(self, valor) -> Nodo:
        """Inclui um nodo com valor desejado como uma folha da árvore, mantendo os
        requisitos de uma árvore binária.

        Se o valor não for uma instância de Nodo, um novo `nodo_filho` será criado.
        Se não houver um nodo raiz ainda, este será adicionado.
        Retorna o `nodo_filho`.
        """
        if isinstance(valor, Nodo):
            nodo_filho = valor
        else:
            nodo_filho = Nodo(valor)

        if self._raiz is None:
            self._raiz = nodo_filho
        else:
            self._raiz.adicionar(nodo_filho)

        return nodo_filho

    def remover(self, valor) -> Nodo:
        """Retira um nodo com valor indicado, se existir."""
        if valor == self._raiz.valor:
            # Removendo nodo da raiz, promove algum dos filhos
            nodo_removido = self._raiz
            self._raiz = gerar_nova_sub_arvore(self._raiz.esquerda, self._raiz.direita)
        else:
            nodo_removido = self._raiz.remover(valor)

        return nodo_removido

    def imprimir(self):
        """Imprime todos os nodos da árvore.

        Utiliza uma fila para imprimir os nodos de cada nível antes de seus filhos.
        A impressão não é perfeita para manter a simplicidade do algoritmo por ora.
        É o suficiente para ter uma noção dos nodos sendo inseridos.
        """
        texto = ""
        nivel = 0
        fila = list()
        fila.append(self._raiz)

        while fila:
            nodo = fila.pop(0)
            if not nodo:
                continue

            if nodo.nivel > nivel:
                # Começa a imprimir novo nível da árvore em nova linha
                texto += "\n"
                nivel = nodo.nivel

            texto += f"{nodo}\t\t"
            fila.append(nodo.esquerda)
            fila.append(nodo.direita)
        print(texto)
