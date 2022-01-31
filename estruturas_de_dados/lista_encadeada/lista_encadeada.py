"""Implementação de Lista Encadeada em Python."""


class Nodo:
    """Elemento de uma lista encadeada, guardando um valor e referenciando outro
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


class ListaEncadeada:
    """Estrutura de dados dinâmica composta de uma série de nodos."""

    def __init__(self):
        """Constrói uma lista vazia."""
        self._primeiro = None
        self._comprimento = 0

    @property
    def primeiro(self) -> Nodo:
        """Retorna o nodo inicial da lista, de forma que só possa ser lido."""
        return self._primeiro

    @property
    def comprimento(self) -> int:
        """Retorna o comprimento da lista, de forma que só possa ser lido."""
        return self._comprimento

    def adicionar_primeiro(self, valor) -> Nodo:
        """Inclui um nodo no início da lista com o valor indicado.

        O novo nodo aponta para o antigo "primeiro".
        """
        novo_nodo = Nodo(valor)
        novo_nodo.proximo = self._primeiro
        self._primeiro = novo_nodo
        self._comprimento += 1
        return novo_nodo

    def adicionar_ultimo(self, valor) -> Nodo:
        """Inclui um nodo no final da lista com o valor indicado.

        Se a lista está vazia, adiciona o primeiro normalmente.
        Senão, percorre até o final (nodo existente não tem um próximo) e faz o
        atual "último" apontar para o novo nodo.
        """
        novo_nodo = Nodo(valor)
        if self._primeiro is None:
            self.adicionar_primeiro(valor)
        else:
            nodo_existente = self._primeiro
            while nodo_existente.proximo:
                nodo_existente = nodo_existente.proximo

            nodo_existente.proximo = novo_nodo
            self._comprimento += 1

        return novo_nodo

    def remover_primeiro(self) -> Nodo:
        """Retira o primeiro nodo da lista e promove o próximo."""
        nodo_removido = self._primeiro
        if self._primeiro is not None:
            self._primeiro = nodo_removido.proximo
            self._comprimento -= 1

        return nodo_removido

    def remover_ultimo(self) -> Nodo:
        """Retira o nodo que está no final da lista.

        Se a lista só tem um nodo, remove o primeiro normalmente.
        Senão, percorre até o penúltimo e faz este não ter mais um próximo.
        """
        if self._primeiro is None:
            # Lista vazia, nada a remover
            nodo_removido = None
        elif self._primeiro.proximo is None:
            # O primeiro é o único, reutiliza a lógica para removê-lo
            nodo_removido = self.remover_primeiro()
        else:
            # Lista possui mais de um nodo
            penultimo_nodo = self._primeiro
            ultimo_nodo = penultimo_nodo.proximo
            while ultimo_nodo.proximo:
                penultimo_nodo = ultimo_nodo
                ultimo_nodo = ultimo_nodo.proximo

            nodo_removido = ultimo_nodo
            penultimo_nodo.proximo = None
            self._comprimento -= 1

        return nodo_removido

    def __repr__(self) -> str:
        """Representa a estrutura de uma maneira amigável para imprimir no terminal."""
        texto = ""
        nodo = self._primeiro
        while nodo:
            texto += f"{nodo}--"
            nodo = nodo.proximo
        return texto
