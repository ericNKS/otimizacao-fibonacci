# Otimização de Algoritmos — Sequência de Fibonacci

Projeto acadêmico desenvolvido com o objetivo de analisar, implementar e comparar diferentes abordagens para o cálculo da sequência de Fibonacci, aplicando técnicas de otimização de algoritmos e avaliando seus impactos no desempenho computacional.

## 1. Objetivo

O objetivo deste projeto é identificar os problemas de desempenho presentes na implementação recursiva ingênua da sequência de Fibonacci e desenvolver versões otimizadas utilizando técnicas de **programação dinâmica**.

Serão realizadas análises de complexidade computacional, medições de tempo de execução e comparações entre diferentes implementações, buscando demonstrar quantitativamente os ganhos obtidos com as otimizações.

### Objetivos específicos

- Implementar o algoritmo de Fibonacci utilizando recursão ingênua.
- Identificar operações redundantes e gargalos de desempenho.
- Analisar a complexidade temporal e espacial dos algoritmos.
- Implementar versões otimizadas utilizando memoização e tabulação.
- Realizar testes de desempenho com diferentes valores de entrada.
- Comparar os resultados por meio de tabelas e gráficos.
- Avaliar os ganhos de desempenho e as limitações de cada abordagem.

## 2. Problema abordado

A sequência de Fibonacci é uma sequência matemática em que cada termo corresponde à soma dos dois termos anteriores, começando por 0 e 1.

Sua definição é:

\[
F(n) =
\begin{cases}
0, & n = 0 \\
1, & n = 1 \\
F(n-1) + F(n-2), & n \geq 2
\end{cases}
\]

Os primeiros termos são:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
```

Embora sua implementação recursiva seja simples, ela apresenta um problema significativo: **a repetição desnecessária de cálculos já realizados**.

Conforme o valor de entrada aumenta, a quantidade de chamadas recursivas cresce exponencialmente, tornando o algoritmo progressivamente mais lento.

O desafio consiste em eliminar esses cálculos redundantes e reduzir a complexidade computacional.

## 3. Abordagens de implementação

Serão desenvolvidas e analisadas três implementações principais.

### 3.1. Recursão ingênua (baseline)

Implementação inicial sem otimizações, utilizando chamadas recursivas para calcular cada termo da sequência.

**Características:**
- Implementação simples e direta.
- Repetição de cálculos intermediários.
- Crescimento exponencial do número de operações.
- Complexidade temporal: `O(2ⁿ)` (limite superior).
- Complexidade espacial: `O(n)` devido à pilha de recursão.

Essa implementação será utilizada como referência para a comparação dos resultados.

### 3.2. Programação dinâmica — Memoização

A memoização consiste em armazenar os resultados dos cálculos anteriores para evitar que sejam realizados novamente.

**Características:**
- Utilização de cache para armazenar valores calculados.
- Eliminação de chamadas recursivas redundantes.
- Complexidade temporal: `O(n)`.
- Complexidade espacial: `O(n)`.

### 3.3. Programação dinâmica — Tabulação

A tabulação utiliza uma abordagem iterativa, calculando os termos da sequência a partir dos casos iniciais.

**Características:**
- Cálculo iterativo dos resultados.
- Ausência de recursão.
- Possibilidade de armazenar apenas os dois últimos termos.
- Complexidade temporal: `O(n)`.
- Complexidade espacial: `O(1)` na versão com memória otimizada.

## 4. Metodologia de análise

A avaliação será realizada em etapas, permitindo comparar o comportamento de cada implementação de maneira controlada.

### 4.1. Análise de complexidade

Será realizada uma análise teórica dos algoritmos, considerando:

- Complexidade temporal (Big O).
- Complexidade espacial.
- Quantidade de operações redundantes.
- Impacto do crescimento da entrada no desempenho.

### 4.2. Benchmark de desempenho

Serão realizados testes com diferentes valores de `n`, medindo o tempo necessário para executar cada implementação.

As medições serão feitas utilizando ferramentas nativas do Python, como:

- `timeit`: medição do tempo de execução.
- `time.perf_counter()`: medição de intervalos com alta resolução.
- `functools.lru_cache`: suporte à memoização.

Os experimentos considerarão múltiplas execuções, condições equivalentes de teste e validação dos resultados calculados.

Para entradas maiores, a versão recursiva ingênua poderá ser excluída dos testes quando seu tempo de execução se tornar impraticável.

### 4.3. Visualização dos resultados

Os dados obtidos serão apresentados por meio de tabelas e gráficos, permitindo observar:

- Tempo de execução por algoritmo.
- Crescimento do tempo conforme a entrada aumenta.
- Diferença de desempenho entre as implementações.
- Fator de aceleração (*speedup*) após as otimizações.

O speedup será calculado pela relação:

\[
Speedup = \frac{T_{\text{original}}}{T_{\text{otimizado}}}
\]

Em que:

- `T_original`: tempo da implementação recursiva ingênua.
- `T_otimizado`: tempo da implementação otimizada.

## 5. Tecnologias utilizadas

- **Python 3** — Linguagem de programação.
- **timeit** — Benchmark e medição de desempenho.
- **functools** — Implementação de cache e memoização.
- **Matplotlib** — Geração de gráficos comparativos.
- **Git e GitHub** — Versionamento e colaboração.

## 6. Resultados esperados

Espera-se demonstrar que a aplicação de programação dinâmica proporciona ganhos expressivos em relação à implementação recursiva ingênua.

| Implementação | Complexidade temporal | Complexidade espacial |
|---|---|---|
| Recursão ingênua | O(2ⁿ) | O(n) |
| Memoização | O(n) | O(n) |
| Tabulação otimizada | O(n) | O(1) |

Além da redução do tempo de execução, o projeto pretende demonstrar como a escolha adequada de um algoritmo pode influenciar diretamente o consumo de recursos computacionais e a escalabilidade de uma solução.

Os resultados efetivos serão apresentados após a realização dos experimentos.

### Comparação realizada

O script `comparacao.py` compara as implementações recursiva e iterativa
existentes para n = 5, 10, 15, 20, 25 e 30. Ele verifica se os resultados
coincidem e mede cada algoritmo separadamente com `timeit`: a quantidade de
execuções é calibrada automaticamente e o tempo apresentado é a mediana de
cinco séries, dividido pelo número de chamadas de cada série.

Para executar novamente com Python 3, sem dependências adicionais:

```bash
python comparacao.py
```

Os resultados são salvos na pasta `resultados/`:

- `comparacao.csv`: valores calculados, tempos em segundos e aceleração.
- `tempos.svg`: comparação dos tempos por chamada.
- `aceleracao.svg`: razão entre o tempo recursivo e o iterativo.

Os gráficos usam escala vertical logarítmica. Os tempos e a aceleração podem
variar conforme o computador e a carga do sistema. A versão iterativa atual
armazena todos os valores em uma lista, portanto usa espaço O(n); a versão
com apenas dois valores descrita acima é uma alternativa ainda não implementada.

## 7. Etapas do projeto

O projeto será organizado em duas entregas.

### Primeira entrega — Diagnóstico e análise inicial

- Implementação do algoritmo recursivo ingênuo.
- Análise da complexidade computacional.
- Identificação dos principais gargalos.
- Realização dos benchmarks iniciais.
- Elaboração do relatório de diagnóstico.
- Apresentação dos resultados iniciais.

### Segunda entrega — Otimização e comparação

- Implementação das versões com memoização e tabulação.
- Realização dos benchmarks comparativos.
- Análise dos ganhos de desempenho.
- Geração de gráficos e tabelas.
- Elaboração do relatório final.
- Apresentação das conclusões.
