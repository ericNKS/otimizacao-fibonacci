# %%
import timeit
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(levelname)s %(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
    force=True
)
# %%
def fib(n):
    nanterior = [0, 1]
    if n < 2:
        return n
    for i in range(2, n + 1):
        nanterior.append(nanterior[i - 2] + nanterior[i - 1])
    return nanterior[-1]

# %%
qtdRepeticao = 10000
tempoTotal = timeit.timeit(
    lambda: fib(20),
    number=qtdRepeticao
)

mediaTempoFib: float = (tempoTotal / qtdRepeticao)

logging.info(f"Tempo médio não otimizado: {mediaTempoFib:.8f}s")