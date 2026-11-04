# %%
import timeit

# %%
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# %%

tempo = timeit.timeit(
    lambda: fib(20),
    number=10000
)

print(f"Tempo médio não otimizado: {tempo / 10000:.8f}s")
