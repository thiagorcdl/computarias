"""Implementação de Pilha em Python."""


class Nodo:
    """Elemento de uma pilha, guardando um valor e referenciando outro
    Nodo.
    """

    def __init__(self, valor):
        """Constrói um nodo com o valor indicado.

        Por padrão, não há um próximo elemento.
        """
        self.valor = valor
        self.debaixo = None

    def __repr__(self) -> str:
        """Representa a estrutura de uma maneira amigável para imprimir no terminal."""
        return f"<{self.valor}>"


class Pilha:
    """Estrutura de dados dinâmica composta de nodos empilhados um em cima do outro."""

    def __init__(self):
        """Constrói uma pilha vazia."""
        self._topo = None

    @property
    def topo(self) -> Nodo:
        """Retorna o nodo inicial da pilha, de forma que só possa ser lido."""
        return self._topo

    def adicionar(self, valor) -> Nodo:
        """Inclui um nodo no topo da pilha com o valor indicado.

        O novo nodo aponta para o antigo "topo".
        """
        novo_nodo = Nodo(valor)
        novo_nodo.debaixo = self._topo
        self._topo = novo_nodo
        return novo_nodo

    def consumir(self) -> Nodo:
        """Retira o nodo do topo da pilha e promove o debaixo."""
        nodo_removido = self._topo
        if self._topo is not None:
            self._topo = nodo_removido.debaixo

        return nodo_removido

    def imprimir(self):
        """Imprime todos os nodos da pilha."""
        texto = "<<< "
        nodo = self._topo
        while nodo:
            texto += f"{nodo} |"
            nodo = nodo.debaixo
        return texto

    def __repr__(self) -> str:
        """Representa a estrutura de uma maneira amigável para imprimir no terminal."""
        conteudo = f"Topo: {self._topo} " if self._topo else "VAZIA"
        return f"[{self.__class__.__name__} | {conteudo}]"
