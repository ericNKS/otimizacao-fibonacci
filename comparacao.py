"""Compara as implementações existentes e gera dados e gráficos reproduzíveis."""
import csv
import math
from pathlib import Path
from statistics import median
from timeit import Timer

from main import fib as recursivo
from otimizacao import fib as iterativo

SAIDA = Path(__file__).resolve().parent / "resultados"


def tempo_medio(funcao, n, repeticoes):
    timer = Timer(lambda: funcao(n))
    # Calibra cada algoritmo separadamente; a mediana reduz ruído do sistema.
    quantidade, _ = timer.autorange()
    return median(timer.repeat(repeat=repeticoes, number=quantidade)) / quantidade


def comparar(entradas, repeticoes=5):
    linhas = []
    for n in entradas:
        resultado = recursivo(n)
        if resultado != iterativo(n):
            raise ValueError(f"Resultados diferentes para n={n}")
        t_rec = tempo_medio(recursivo, n, repeticoes)
        t_iter = tempo_medio(iterativo, n, repeticoes)
        linhas.append(dict(n=n, resultado=resultado, recursivo_s=t_rec,
                           iterativo_s=t_iter, aceleracao=t_rec / t_iter))
    return linhas


def grafico(linhas, series, titulo, eixo_y, nome):
    # SVG é um formato gráfico vetorial que não exige bibliotecas externas.
    largura, altura = 900, 540
    esquerda, direita, topo, base = 100, 40, 90, 100
    w, h = largura - esquerda - direita, altura - topo - base
    valores = [linha[chave] for linha in linhas for chave, _, _ in series]
    minimo = math.floor(math.log10(min(valores)))
    maximo = math.ceil(math.log10(max(valores)))
    if minimo == maximo:
        maximo += 1
    def y(valor):
        return topo + h * (maximo - math.log10(valor)) / (maximo - minimo)
    def x(indice):
        return esquerda + w * indice / max(1, len(linhas) - 1)
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{largura}" height="{altura}" viewBox="0 0 {largura} {altura}">',
              '<rect width="100%" height="100%" fill="white"/>',
              f'<text x="{largura/2}" y="35" text-anchor="middle" font-family="Arial" font-size="23" font-weight="bold">{titulo}</text>',
              f'<text x="{largura/2}" y="60" text-anchor="middle" font-family="Arial" font-size="13" fill="#555">Mediana de 5 séries; escala vertical logarítmica</text>']
    for expoente in range(minimo, maximo + 1):
        yy = y(10 ** expoente)
        partes += [f'<line x1="{esquerda}" y1="{yy}" x2="{esquerda+w}" y2="{yy}" stroke="#ddd"/>',
                   f'<text x="{esquerda-10}" y="{yy+5}" text-anchor="end" font-family="Arial" font-size="13">10^{expoente}</text>']
    for i, linha in enumerate(linhas):
        partes.append(f'<text x="{x(i)}" y="{topo+h+25}" text-anchor="middle" font-family="Arial" font-size="13">{linha["n"]}</text>')
    partes += [f'<line x1="{esquerda}" y1="{topo+h}" x2="{esquerda+w}" y2="{topo+h}" stroke="#333"/>',
               f'<text x="{esquerda+w/2}" y="{altura-28}" text-anchor="middle" font-family="Arial" font-size="15">Entrada n</text>',
               f'<text transform="translate(22 {topo+h/2}) rotate(-90)" text-anchor="middle" font-family="Arial" font-size="15">{eixo_y}</text>']
    for indice, (chave, rotulo, cor) in enumerate(series):
        pontos = " ".join(f'{x(i):.1f},{y(linha[chave]):.1f}' for i, linha in enumerate(linhas))
        partes.append(f'<polyline points="{pontos}" fill="none" stroke="{cor}" stroke-width="3"/>')
        for i, linha in enumerate(linhas):
            partes.append(f'<circle cx="{x(i):.1f}" cy="{y(linha[chave]):.1f}" r="4" fill="{cor}"/>')
        partes.append(f'<text x="{esquerda + indice*220}" y="{altura-5}" font-family="Arial" font-size="13" fill="{cor}">● {rotulo}</text>')
    partes.append('</svg>')
    (SAIDA / nome).write_text("\n".join(partes), encoding="utf-8")


def main():
    SAIDA.mkdir(exist_ok=True)
    linhas = comparar([5, 10, 15, 20, 25, 30])
    with (SAIDA / "comparacao.csv").open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=linhas[0].keys())
        escritor.writeheader()
        escritor.writerows(linhas)
    grafico(linhas, [('recursivo_s', 'Recursivo', '#d1495b'),
                     ('iterativo_s', 'Iterativo', '#1768ac')],
            'Tempo de execução por algoritmo', 'Tempo médio por chamada (s)', 'tempos.svg')
    grafico(linhas, [('aceleracao', 'Recursivo / iterativo', '#287d52')],
            'Aceleração da versão iterativa', 'Fator de aceleração (vezes)', 'aceleracao.svg')
    for linha in linhas:
        print(f"n={linha['n']:2}: recursivo={linha['recursivo_s']:.9f}s  "
              f"iterativo={linha['iterativo_s']:.9f}s  aceleração={linha['aceleracao']:.1f}x")


if __name__ == "__main__":
    main()
