import time
from functools import cache

def fib_no_cache(n):
    if n < 2:
        return n
    return fib_no_cache(n - 1) + fib_no_cache(n - 2)

# Cached Fibonacci
@cache
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n - 1) + fib_with_cache(n - 2)

n = 35

# Test without cache
start = time.time()
result_no_cache = fib_no_cache(n)
end = time.time()
print(f"Without cache: fib({n}) = {result_no_cache}, Time taken = {end - start:.4f} seconds")

# Test with cache
start = time.time()
result_with_cache = fib_with_cache(n)
end = time.time()
print(f"With cache   : fib({n}) = {result_with_cache}, Time taken = {end - start:.4f} seconds")
