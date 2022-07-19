# Lista Encadeada

> 🇺🇸 _Linked List_

Uma lista encadeada é uma estrutura de dados formada por uma série de elementos 
(ou nodos), cada um contendo um valor e uma referência para o próximo elemento da 
lista. A lista encadeada tem um comprimento dinâmico à medida que elementos são 
adicionados ou removidos, o que significa que ela que pode armazenar uma quantidade 
qualquer de valores. 

Uma variável que guarda uma lista encadeada é, na verdade, apenas uma referência para 
o primeiro nodo da lista. Este possui uma referência para o segundo; o segundo para o terceiro; e assim sucessivamente até que o último nodo, que não referencia nenhum outro elemento existente.

```python
minha_lista = ListaEncadeada()
minha_lista.primeiro == None
```

É possível adicionar elementos tanto no final, quanto no início da lista.
Quando se insere no final, o atual último nodo simplesmente receberá a referência para o novo nodo sendo inserido. Por outro lado (literalmente), quando se insere no início, o novo nodo recebe a referência do antigo início da lista.


```python
# Inicia a lista vazia
minha_lista = ListaEncadeada()

# Cria primeiro nodo, valor "ABC"
minha_lista.adicionar_primeiro("ABC")
minha_lista.primeiro.valor == "ABC"

# Insere novo nodo na primeira posição, valor "XYZ"
minha_lista.adicionar_primeiro("XYZ")
minha_lista.primeiro.valor == "XYZ"
minha_lista.primeiro.proximo.valor == "ABC"
```

## Código

Veja a implementação em Python aqui:

* [lista_encadeada.py](lista_encadeada.py)

## Observações

* A lista encadeada mais simples é também conhecida como "lista _unicamente_ encadeada", apenas uma referência, que é para o próximo elemento da lista; não para o anterior. Logo, **a lista só pode ser percorrida em uma única direção**.
* Alternativamente, é possível ter elementos referenciando tanto o próximo nodo quanto o nodo anterior, permitindo a lista ser percorrida em ambas as direções. Nesse caso, é uma "lista _duplamente_ encadeada".
* Também é possível guardar uma referência direto para o último nodo da lista (assim como há para o primeiro), facilitando a inclusão de novos nodos no final.
