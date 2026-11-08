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
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# %%
if __name__ == "__main__":
    qtdRepeticao = 10000
    tempoTotal = timeit.timeit(lambda: fib(20), number=qtdRepeticao)
    mediaTempoFib = tempoTotal / qtdRepeticao
    logging.info(f"Tempo médio não otimizado: {mediaTempoFib:.8f}s")
    print(fib(8))
