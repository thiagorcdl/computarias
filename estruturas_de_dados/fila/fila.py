"""Implementação de Fila em Python."""


class Nodo:
    """Elemento de uma fila, guardando um valor e referenciando outro
    Nodo.
    """

    def __init__(self, valor):
        """Constrói um nodo com o valor indicado.

        Por padrão, não há um próximo elemento.
        """
        self.valor = valor
        self.proximo = None

    def __repr__(self) -> str:
        """Representa a estrutura de uma maneira amigável para imprimir no terminal."""
        return f"<{self.valor}>"


class Fila:
    """Estrutura de dados caracterizada pela manipulação First In First Out.

    Nodos são adicionados sempre no final da fila, mas consumidos pelo começo.
    """

    def __init__(self):
        """Constrói uma fila vazia."""
        self._primeiro = None
        self._comprimento = 0

    @property
    def primeiro(self) -> Nodo:
        """Retorna o nodo inicial da fila, de forma que só possa ser lido."""
        return self._primeiro

    @property
    def comprimento(self) -> int:
        """Retorna o comprimento da fila, de forma que só possa ser lido."""
        return self._comprimento

    def adicionar(self, valor) -> Nodo:
        """Inclui um nodo no final da fila com o valor indicado.

        Percorre até o final (nodo existente não tem um próximo) e faz o
        atual "último" apontar para o novo nodo.
        """
        novo_nodo = Nodo(valor)
        if self._primeiro is None:
            self._primeiro = novo_nodo
        else:
            nodo_existente = self._primeiro
            while nodo_existente.proximo:
                nodo_existente = nodo_existente.proximo

            nodo_existente.proximo = novo_nodo

        self._comprimento += 1
        return novo_nodo

    def consumir(self) -> Nodo:
        """Retira o primeiro nodo da fila e promove o próximo."""
        nodo_removido = self._primeiro
        if self._primeiro is not None:
            self._primeiro = nodo_removido.proximo
            self._comprimento -= 1

        return nodo_removido

