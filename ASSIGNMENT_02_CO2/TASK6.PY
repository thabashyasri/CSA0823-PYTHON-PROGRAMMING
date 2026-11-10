import sys, time
from functools import lru_cache
calls = 0
 
def ways_naive(n):
    global calls
    calls += 1
    if n <= 1: return 1
    return ways_naive(n - 1) + ways_naive(n - 2)
 
@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1: return 1                         # TODO 1
    return ways_memo(n - 1) + ways_memo(n - 2)
 
def ways_loop(n):
    a, b = 1, 1
    for _ in range(n - 1): a, b = b, a + b
    return b if n >= 1 else 1
 
calls = 0; print("naive:", ways_naive(25), "calls =", calls)
ways_memo.cache_clear()
calls = 0; print("memo :", ways_memo(25), "calls =", calls)
 
print("\nHand check n=1..6 (1,2,3,5,8,13):", [ways_loop(n) for n in range(1, 7)],
      "| naive:", [ways_naive(n) for n in range(1, 7)], "| memo:", [ways_memo(n) for n in range(1, 7)])
 
print("\nCall counts (n, naive, memo, predicted naive 2*F(n+1)-1 = 2*ways(n)-1, predicted memo n+1):")
for n in (5, 10, 20, 25, 30):
    calls = 0; ways_naive(n); cn = calls
    ways_memo.cache_clear(); calls = 0; ways_memo(n); cm = calls
    print(f"n={n:<3} naive={cn:<8} memo={cm:<4} 2*ways-1={2*ways_loop(n)-1:<8} n+1={n+1}")
 
print("\nTime for n=30:")
s = time.perf_counter(); ways_naive(30); tn = time.perf_counter() - s
ways_memo.cache_clear(); s = time.perf_counter(); ways_memo(30); tm = time.perf_counter() - s
print(f"naive {tn:.4f} s   memo {tm:.6f} s")
 
print("\nrecursion limit =", sys.getrecursionlimit())
ways_memo.cache_clear()
try:
    print(ways_memo(1000))
except RecursionError as e:
    print("RecursionError:", e)
print("n=1000 loop digits:", len(str(ways_loop(1000))))
# memo works if we warm the cache bottom-up, or raise the limit
ways_memo.cache_clear()
for k in range(0, 1001, 100): ways_memo(k)
print("memo after warming in steps of 100 -> same as loop:", ways_memo(1000) == ways_loop(1000))
ways_memo.cache_clear(); sys.setrecursionlimit(5000)
s = time.perf_counter(); r = ways_memo(1000); tm = time.perf_counter() - s
s = time.perf_counter(); r2 = ways_loop(1000); tl = time.perf_counter() - s
print(f"limit 5000: memo {tm:.6f} s, loop {tl:.6f} s, equal: {r == r2}")
print("ways(1000) =", str(r)[:20] + "...", f"({len(str(r))} digits)")
