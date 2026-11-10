import sys, time, tracemalloc
from functools import lru_cache
calls = 0; depth = 0; maxdepth = 0; from collections import Counter; seen = Counter()
 
def original(n):
    global calls, depth, maxdepth
    calls += 1; seen[n] += 1; depth += 1; maxdepth = max(maxdepth, depth)
    r = 1 if n <= 1 else original(n - 1) + original(n - 2)
    depth -= 1; return r
 
def redesigned(n):
    """Bottom-up: ways(n) depends only on the previous two values."""
    ops = 0; a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b; ops += 1          # one addition per step
    return b, ops
 
print("A. DIAGNOSIS of original for n = 25")
calls = 0; seen.clear(); maxdepth = 0; original(25)
print(f"  calls={calls}, distinct arguments={len(seen)}, repeated calls={calls-len(seen)}, max depth={maxdepth}")
print(f"  ways(1) evaluated {seen[1]} times, ways(2) {seen[2]} times, ways(25) {seen[25]} time")
print(f"  share of calls that were repeats: {100*(calls-len(seen))/calls:.4f}%")
 
print("\nE. ORIGINAL vs REDESIGNED (same inputs)")
print(f"{'n':>5} | {'orig calls':>10} {'orig time s':>12} | {'new additions':>13} {'new time s':>11} | speed-up | equal")
for n in (10, 20, 25, 30, 32):
    calls = 0; s = time.perf_counter(); r1 = original(n); t1 = time.perf_counter() - s
    s = time.perf_counter(); r2, ops = redesigned(n); t2 = time.perf_counter() - s
    print(f"{n:>5} | {calls:>10} {t1:>12.5f} | {ops:>13} {t2:>11.7f} | {t1/t2:>8.0f}x | {r1 == r2}")
 
print("\nLarge n (original impossible):")
for n in (1000, 5000, 20000):
    s = time.perf_counter(); r, ops = redesigned(n); t = time.perf_counter() - s
    print(f"  n={n:<6} additions={ops:<6} time={t:.5f} s  digits={len(str(r))}")
 
print("\nMemory for n=1000 (tracemalloc peak, bytes):")
@lru_cache(maxsize=None)
def memo(n): return 1 if n <= 1 else memo(n-1) + memo(n-2)
tracemalloc.start(); memo.cache_clear()
for k in range(0, 1001, 100): memo(k)
m_peak = tracemalloc.get_traced_memory()[1]; tracemalloc.stop()
tracemalloc.start(); redesigned(1000); l_peak = tracemalloc.get_traced_memory()[1]; tracemalloc.stop()
print(f"  lru_cache (warm-up) peak {m_peak}   redesigned loop peak {l_peak}")
print("  recursion limit", sys.getrecursionlimit(), "- redesigned loop uses no recursion") 