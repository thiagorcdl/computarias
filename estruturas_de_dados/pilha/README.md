# Pilha

> 🇺🇸 _Stack_

O termo "pilha" no contexto de estrutura de dados é uma referência a coisas empilhadas, uma em cima da outra -- não tem a ver com pilhas de energa elétrica. Mais especificamente, uma pilha em que você só consiga acessar o objeto que está no topo. Pense em um tubo de Pringles ©. Ou melhor, pense em um tubo Stax ©, um trocadilho da equipe de publicidade com "_stacks_" (🇧🇷 _pilhas_).

Assim como a [fila](/estruturas_de_dados/fila/), a pilha é uma implementação mais específica de uma [lista encadeada](/estruturas_de_dados/lista_encadeada/), mas com algumas diferenças. A primeira é semântica -- em vez de pensarmos em um elemento atrás de o outro, pensamos neles um em cima do outro -- mas a maior diferença está na ordem de manipulação.

A pilha implementa o comportamento _LIFO_, sigla para _**Last**-In First-Out_ (🇧🇷 _**Último** a Entrar, Primeiro a Sair_). Isto significa que primeiro elemento a ser inserido será o último a ser consumido.

Voltando ao exemplo das batatinhas fritas, após o consumidor abrir o tubo, começará comendo a batatinha do topo e terminará com a que está no fundo (a não ser que haja algum defeito na "estrutura"). Só que na fábrica, a batatinha do fundo foi a primeira a ser inserida no tubo e a do topo foi a última antes de a embalagem ser selada.


```python
minha_pilha = Pilha()

minha_pilha.adicionar("Dark Magician")
minha_pilha.adicionar("M Charizard EX")
minha_pilha.adicionar("+4")

minha_pilha.consumir() # +4 
minha_pilha.consumir() # M Charizard EX
minha_pilha.consumir() # Dark Magician
```

Em termos de aplicação real, pilhas são extremamente úteis quando se quer colocar algo temporariamente em memória e muito utilizadas por compiladores e interpretadores. Toda vez que uma função é chamada, um novo escopo de execução é criado, com referências à função e parâmetros sendo empilhados na memória, mantendo um isolamento com o escopo anterior (que chamou a função). Quando esta acaba sua execução, tudo o que estava em seu escopo é desempilhado e basicamente perdido; por isso você não consegue acessar a variável de uma função A dentro de outra função B. No máximo, em alguns casos pode-se acessar uma variável de um escopo anterior que ainda esteja na pilha (ex: variáveis globais).

Também existem diversos algoritmos que utilizam essa estrutura, como a _Busca em Profundidade_ que é um dos mais importantes a se aprender. A pilha, nesse caso, mantém um histórico do trajeto a se percorrer para encontrar o nodo desejado em uma Árvore. Isso mesmo, a pilha é uma estrutura de dados que auxilia no algoritmo de outra estrutura de dados.

## Código

Veja a implementação em Python aqui:

* [pilha.py](pilha.py)
