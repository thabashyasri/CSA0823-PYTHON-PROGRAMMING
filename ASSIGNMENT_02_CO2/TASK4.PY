import time, io, statistics
 
def make(n): return [f"Item{i}:Rs{i % 50}" for i in range(n)]
 
def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text
 
def build_join(parts):
    return ";".join(parts) + ";"            # TODO 1 (single join call)
 
def build_fstring_join(parts):
    return "".join([f"{p};" for p in parts])  # (c) f-string per line, then join
 
def build_stringio(parts):
    buf = io.StringIO()
    for p in parts: buf.write(p); buf.write(";")
    return buf.getvalue()
 
def timeit_once(f, x):
    s = time.perf_counter(); r = f(x); return time.perf_counter() - s, r
 
print("== Assignment program (200,000 items), three runs ==")
items = make(200_000)
tp, tj = [], []
for run in range(3):
    t1, a = timeit_once(build_plus, items); t2, b = timeit_once(build_join, items)
    tp.append(t1); tj.append(t2)
    print(f"run {run+1}: same text: {a == b} | length: {len(b)} | += {t1:.4f} s  join {t2:.4f} s")
print(f"average: += {statistics.mean(tp):.4f} s   join {statistics.mean(tj):.4f} s   ratio {statistics.mean(tp)/statistics.mean(tj):.1f}x")
 
print("\n== Three implementations x three sizes (best of 3, seconds) ==")
print(f"{'lines':>8} {'+=':>9} {'join':>9} {'fstr+join':>10} {'StringIO':>9}")
for n in (1000, 10000, 200000):
    it = make(n); row = []
    for f in (build_plus, build_join, build_fstring_join, build_stringio):
        row.append(min(timeit_once(f, it)[0] for _ in range(3)))
    print(f"{n:>8} " + " ".join(f"{v:>9.5f}" for v in row))
 
print("\n== Defeating CPython's in-place += optimisation (text kept referenced twice) ==")
def build_plus_alias(parts):
    text = ""; keep = None
    for p in parts:
        keep = text              # extra reference -> refcount > 1 -> real copy
        text = text + p + ";"
    return text
for n in (1000, 5000, 20000):
    it = make(n)
    print(f"{n:>6} lines  alias-+ {timeit_once(build_plus_alias, it)[0]:.4f} s  join {timeit_once(build_join, it)[0]:.5f} s")
