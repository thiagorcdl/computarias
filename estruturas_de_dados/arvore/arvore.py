"""Implementação de Árvore em Python."""


class Nodo:
    """Elemento de uma árvore, guardando um valor e referenciando outros Nodos."""

    def __init__(self, valor):
        """Constrói um nodo com o valor indicado.

        Por padrão, o conjunto de filhos é vazio.
        """
        self.valor = valor
        self._filhos = set()

    def __repr__(self) -> str:
        """Representa a estrutura de uma maneira amigável para imprimir no terminal."""
        return f"<{self.valor}>"

    @property
    def filhos(self) -> set:
        """Retorna os filhos do nodo atual, apenas para leitura."""
        return self._filhos

    def adicionar(self, nodo_filho):
        """Adiciona um novo nodo aos filhos."""
        self._filhos.add(nodo_filho)
        return nodo_filho

    def remover(self, nodo_filho):
        """Remove um novo nodo dos filhos."""
        self._filhos.remove(nodo_filho)
        return nodo_filho


class Arvore:
    """Estrutura hieráriquica com um nodo raiz e cada nodo tendo subnodos."""

    def __init__(self):
        """Constrói uma árvore vazia."""
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
        nodo_encontrado = self.raiz

        if nodo_encontrado is None or nodo_encontrado.valor == valor:
            return nodo_encontrado

        for filho in nodo_encontrado.filhos:
            nodo_encontrado = filho.busca(valor)
            if nodo_encontrado:
                return nodo_encontrado

    def adicionar(self, valor, nodo_pai=None) -> Nodo:
        """Inclui um nodo com valor desejado nos filhos de `nodo_pai`.

        Se o valor não for uma instância de Nodo, um novo `nodo_filho` será criado.
        Se um `nodo_pai` não for especificado, assume o pai como sendo o nodo raiz.
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
            if nodo_pai is None:
                nodo_pai = self._raiz
            nodo_pai.adicionar(nodo_filho)
        return nodo_filho
