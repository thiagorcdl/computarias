# Pilha

> 🇺🇸 _Stack_

O termo "pilha" no contexto de estrutura de dados é uma referência a coisas empilhadas, uma em cima da outra -- não tem a ver com pilhas de energa elétrica. Mais especificamente, uma pilha em que você só consiga acessar o objeto que está no topo. Pense em um tubo de Pringles ©. Ou melhor, pense em um tubo Stax ©, um trocadilho da equipe de publicidade com "_stacks_" (🇧🇷 _pilhas_).

Assim como a fila, a pilha é uma implementação mais específica de uma lista encadeada. A primeira diferença é semântica -- em vez de pensarmos em um elemento atrás de o outro, pensamos neles um em cima do outro -- mas a maior diferença está na ordem de manipulação.

Ao contrário da fila, uma pilha implementa o comportamento _LIFO_, sigla para _**Last**-In First-Out_ (🇧🇷 _**Último** a Entrar, Primeiro a Sair_). Isto significa que primeiro elemento a ser inserido será o último a ser consumido.

Voltando ao exemplo das batatinhas fritas, quando você abre o tubo, vai começar comendo a do topo e terminar comendo a que está no fundo (a não ser que haja algum defeito na "estrutura"). Só que na fábrica, a batatinha do fundo foi a primeira a ser inserida na embalagem e a do topo foi a última antes de a embalagem ser selada.


```python
minha_pilha = Pilha()

minha_pilha.adicionar("Dark Magician")
minha_pilha.adicionar("M Charizard EX")
minha_pilha.adicionar("+4")

minha_pilha.consumir() # +4 
minha_pilha.consumir() # M Charizard EX
minha_pilha.consumir() # Dark Magician
```


