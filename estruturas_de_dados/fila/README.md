# Fila

> 🇺🇸 _Queue_ (pronuncia-se igual _kill_)

A fila pode ser interpretada como uma versão da lista encadeada, mas com uma particularidade na sua manipulação: o primeiro elemento a ser inserido será o primeiro a ser removido. Este comportamento é chamado de _FIFO_, sigla para _First In First Out_ (🇧🇷 _Primeiro a Entrar, Primeiro a Sair_).

Ela dispensa muita explicação por funcionar exatamente como uma fila comum na vida real. Os elementos são posicionados um atrás do outro; quem chega depois vai pro final da fila; quem está no ínicio da fila será o próximo a ser atendido.

```python
minha_fila = Fila()

minha_fila.adicionar("Zangief")
minha_fila.adicionar("Oreo")
minha_fila.adicionar("Flora")

minha_fila.consumir() # Zangief 
minha_fila.consumir() # Oreo
minha_fila.consumir() # Flora
```

Também é igualmente fácil pensar em aplicações práticas para essa estrutura de dados: basta considerar a digitalização de qualquer processo burocrático onde uma pessoa teria de aguardar numa fila.

### Observações

* Assim como em filas da "vida real", é possível adicionar lógicas de prioridades
