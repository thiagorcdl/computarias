"""Funções de suporte para Árvore Binária."""


def gerar_nova_sub_arvore(esquerda, direita):
    """Combina ambos os galhos para formar uma nova sub-árvore, se necessário.

    Se o nodo a ser removido possui dois filhos, um será ser promovido ao espaço
    do que está sendo removido, mas o outro galho não pode ser perdido, então deve
    ser adicionado de volta à árvore.
    """
    if not esquerda:
        # Esquerda está vazia, nova sub-árvore é simplesmente a da direita
        esquerda.nivel -= 1
        return direita
    elif not direita:
        # Direita está vazia, nova sub-árvore é simplesmente a da esquerda
        direita.nivel -= 1
        return esquerda

    # Ambos os lados possuem nodos, insere direita na esquerda e retorna esquerda
    # como sendo a nova raiz.
    esquerda.nivel -= 1
    esquerda.adicionar(direita)
    return esquerda
