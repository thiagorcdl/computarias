"""Implementação de Vetor em Python."""


class Vetor:
    """Estrutura de dados básica para armazenar uma quantidade pré-definida
    de elementos.

    Utilização:
        meu_vetor = Vetor(3)
        print(meu_vetor) # [None, None, None]
        meu_vetor[0] = "A"
        print(meu_vetor) # ["A", None, None]
    """

    def __init__(self, comprimento):
        """Constrói um meu_vetor "vazio" com o tamanho desejado.

        Posições "vazias" são representadas com `None`.
        """
        self._elementos = [None for _ in range(comprimento)]
        self._comprimento = comprimento

    @property
    def comprimento(self) -> int:
        """Retorna o comprimento do vetor, de forma que só possa ser lido.

        Utilização:
            meu_vetor = Vetor(1, 2, 3)
            print(meu_vetor.comprimento) # 3
        """
        return self._comprimento

    def __getitem__(self, indice: int):
        """Retorna o elemento armazenado na posição do `indice` requisitado.

        Utilização:
            meu_vetor = Vetor(1, 2, 3)
            print(meu_vetor[0]) # 1
            dois = meu_vetor[1]
        """
        return self._elementos[indice]

    def __setitem__(self, indice: int, elemento):
        """Armazena um elemento qualquer na posição do `indice` desejado.

        Utilização:
            meu_vetor = Vetor(1, 2, 3)
            meu_vetor[0] = "a"
        """
        self._elementos[indice] = elemento
        return elemento

    def __repr__(self) -> str:
        """Representa a estrutura de uma maneira amigável para imprimir no terminal."""
        return self._elementos.__repr__()
