# Composite

## 1. Estudo e Material Explicativo 

## Nome do padrão: 
Composite (Árvore de Objetos)

## Categoria: 
Estrutural

## Intenção: 
Permitir que você componha objetos em uma estrutura de árvore e depois possa trabalhar com essas estruturas como se elas fossem objetos individuais. 

## Problema: 
Só faz sentido quando o modelo central da aplicação pode ser representado como uma árvore. Do contrário, será pesado para o sistema ler todas as diferentes aplicações uma por uma quando for necessário “desempacotar” os objetos. 

## Solução:
 Você pode trabalhar com mais de um tipo de objeto através de uma interface comum, assim, não precisando se preocupar com cada uma das classes concretas dos objetos que compõem uma árvore. 

## Estrutura UML:


## Exemplos no Mundo Real:

Compiste se assemelha a uma hierarquia de exército, onde a classe mais alta, comanda a de baixo, que comanda outras tantas classes, em diferentes batalhões em assim por diante. 

## Pontos Fracos
Se o modelo de projeto for ter uma grande variedade de características dentro das classes, pode se tornar um um modelo pesado e pouco eficiente. 

## Quando usar
Quando seu modelo central de projeto permitir uma estrutura hierarquica em árvore. 

## 2. Código com fonte com ou sem 
Com:
exemplo.py
Sem:
exemplo2.py

## 3. Conclusões 
Composite por ser útil quando o projeto pede hierarquia e padronização, utilizando-se de uma interface comum para todos os objetos e classes, mas pode ser problemático caso o projeto preveja mais variabilidade e individualidade. 
