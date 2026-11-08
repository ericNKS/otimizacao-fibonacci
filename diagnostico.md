# Diagnóstico e primeiro ganho de desempenho

## O problema

O projeto calcula termos da sequência de Fibonacci. Ela começa em 0 e 1, e
cada termo seguinte é a soma dos dois anteriores: 0, 1, 1, 2, 3, 5, 8...
Por exemplo, para a entrada `n = 5`, o resultado é `F(5) = 5`.

O objetivo é comparar o tempo necessário para obter o mesmo resultado com
duas abordagens: a recursiva original, em `main.py`, e a iterativa com
tabulação, em `otimizacao.py`.

## Gargalo encontrado

A versão recursiva calcula `F(n)` chamando novamente a função para
`F(n - 1)` e `F(n - 2)`. O problema é que essas chamadas voltam a
calcular os mesmos termos. Por exemplo, ao calcular `F(5)`, tanto o cálculo
de `F(4)` quanto o de `F(3)` precisam de `F(2)`; esse valor é calculado
mais de uma vez.

Essa repetição cresce rapidamente com a entrada e faz a versão recursiva
ingênua ter tempo exponencial. A versão iterativa evita a repetição: começa
com 0 e 1 e guarda os valores já calculados em uma lista. Ela realiza um
número linear de etapas e, na implementação atual, usa espaço proporcional
a `n` para a lista.

## Primeiro ganho medido

Na primeira entrada testada, `n = 5`, as duas versões retornaram 5:

| Versão | Tempo médio por chamada |
|---|---:|
| Recursiva | 0,000000364 s |
| Iterativa | 0,000000233 s |

Dividindo o tempo recursivo pelo iterativo, a versão iterativa foi cerca de
**1,56 vez mais rápida** nessa medição, com redução de aproximadamente
**36% no tempo**. Como os tempos são muito pequenos, essa diferença pode
variar entre execuções.

Para uma entrada maior, `n = 20`, ambas retornaram 6.765. A versão
recursiva levou aproximadamente 0,000570656 s por chamada, e a iterativa,
0,000000695 s: uma aceleração de cerca de **821 vezes** na medição realizada.
Isso ilustra como os cálculos repetidos afetam a versão recursiva conforme a
entrada cresce.

## Como a comparação foi feita

O script `comparacao.py` testou `n = 5, 10, 15, 20, 25 e 30` e verificou se
as duas funções produziam o mesmo resultado em cada entrada. Usou `timeit`
para calibrar separadamente o número de chamadas de cada algoritmo e
calculou a mediana de cinco séries, dividindo o tempo pelo número de chamadas.
Os resultados dependem do computador e das condições de execução.

- [Tabela completa de medições](resultados/comparacao.csv)
- [Gráfico de tempos em PNG](resultados/tempos.png)
- [Gráfico de aceleração em PNG](resultados/aceleracao.png)

Os gráficos usam escala vertical logarítmica para apresentar valores de
grandezas diferentes na mesma figura.
