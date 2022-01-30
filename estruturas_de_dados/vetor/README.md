# Vetor

> 🇺🇸 _Array_

Um vetor é uma lista de valores unidimensional, geralmente com um comprimento 
pré-definido. 

O comprimento de um vetor refere-se à quantidade de posições que ele possui para
armazenar algum dado. Por exemplo, pode-se armazenar os nomes dos países do G7 em
vetor de sete posições:

```python
paises_g7 = Vetor(7)
paises_g7.comprimento == 7
```

Um vetor permite que o conteúdo de uma posição sua seja acessado (tanto para leitura quanto para armazenamento) passando o índice da
da posição desejada. As posições de um vetor são _indexadas_ a partir do número 0. Ou seja, o primeiro país 
da lista acima será encontrado na posição de índice `0`; o segundo país, na posíção de índice `1`; o terceiro no `2`; e assim por diante.

```python
paises_g7[0] = "França"
paises_g7[1] = "Alemanha"
paises_g7[2] = "Itália"
paises_g7[3] = "Japão"
paises_g7[4] = "Reino Unido"
paises_g7[5] = "Estados Unidos"
paises_g7[6] = "Canadá"
```

Isso significa também que, apesar de o vetor ter tamanho `7` (sete posições), o último
índice é `6`. O último índice de um vetor é sempre um a menos que seu comprimento.

```python
ultimo_indice = meu_vetor.comprimento - 1
```

É importante manter isso em mente na hora de percorrer todos as posições de um vetor
para evitar erros.

### Observações

* Estou usando o termo "comprimento" em vez de "tamanho" para evitar confusão com o 
espaço que a estrutura pode ocupar em memória, mas no dia a dia ambas as palavras são
válidas para se referir a quantos ítens existem/cabem em um vetor.

* A implementação específica e o real espaço utilizado em bits dependerão da linguagem e como cada tipo é tratado, mas de maneira geral, se uma variável ocupa `X` de espaço em memória, então um vetor de comprimento `N` ocupará
`N * X`. 

