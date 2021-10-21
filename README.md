# Escopos

Você sabe o que é um escopo? Um escopo diz respeito ao espaço que as variáveis habitam. Ela é criada dentro do escopo, e 
desalocada quando ele acaba; ou seja, ela deixa de existir tão logo o escopo termine.

No geral, existem dois tipos de escopo: local e global. O escopo local se refere a um pedaço bem definido de código-fonte
(por exemplo, uma função, ou um laço de repetição). Já o escopo gobal se refere geralmente a todo o corpo de um script em
Python.

## Exercícios

1. Abra o arquivo [escopo/experimento_1.py](escopo/experimento_1.py) e analise o código-fonte. Por que é possível imprimir
   o valor de `x` dentro da função `main`, mas não é possível imprimir o valor de `y` fora da função `main`? Qual o escopo
   destas duas variáveis?
   * O que significa a mensagem de erro apresentada no console?
   * Corrija o código de forma que tanto `x` quanto `y` possam ser impressas dentro e fora da função `main`
2. Abra o arquivo [escopo/experimento_2.py](escopo/experimento_2.py) e analise o código-fonte. Por que o código-fonte
   funciona dessa vez? Por que é possível imprimir o valor de `i` fora do `for`?
   * Se você estiver usando o Pycharm, repouse o mouse sobre o `i` de fora do laço. Por que o Pycharm está pintando ele
     de amarelo? O que significa a mensagem de erro?
3. Abra o arquivo [escopo/experimento_3.py](escopo/experimento_3.py) e analise o código-fonte. Contemple.
4. Abra o arquivo [escopo/experimento_4.py](escopo/experimento_4.py) e analise o código-fonte. Por que conseguimos 
   acessar a variável `x` de dentro da `minha_funcao`? Qual o escopo da função `minha_funcao`, e qual o escopo da variável
   `x`?
5. Abra o arquivo [escopo/experimento_5.py](escopo/experimento_5.py) e analise o código-fonte. Por que a função `main`
   não consegue acessar a variável `y` da função `minha_funcao`? Qual o escopo da variável `y`? A variável `y` persiste
   para além do seu escopo?
6. Abra o arquivo [escopo/experimento_6.py](escopo/experimento_6.py) e analise o código-fonte. Por que o código-fonte roda
   metade das vezes, e metade das vezes não roda? Qual o escopo da variável `texto`? 
   * Compare este código com o código do arquivo [escopo/experimento_2.py](escopo/experimento_2.py). Por que o resultado
     foi diferente desta vez?
   * Devemos confiar que uma variável irá "vazar" de um escopo para outro, ou devemos sempre desconfiar desse comportamento?