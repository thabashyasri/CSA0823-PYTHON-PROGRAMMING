import timeit, bisect
 
def separate_ifs(units, ration, elder):
    """Buggy: independent if statements -> more than one result possible."""
    result = []
    if units <= 100:
        result.append("FULL")
    if units <= 200 and ration:          # bug: also true when units <= 100
        result.append("PARTIAL")
    if units > 200 and elder:
        result.append("ELDER")
    if not result:
        result.append("NONE")
    return result
 
def elif_chain(units, ration, elder):
    """Correct: exactly one branch runs."""
    if units <= 100:
        return "FULL"
    elif 101 <= units <= 200 and ration:
        return "PARTIAL"
    elif units > 200 and elder:
        return "ELDER"
    else:
        return "NONE"
 
# Alternative 1: slab table searched in a loop (upper limit, rule)
SLABS = [(100, "FULL"), (200, "RATION"), (float("inf"), "ELDER")]
def slab_loop(units, ration, elder):
    for limit, rule in SLABS:
        if units <= limit:
            if rule == "FULL": return "FULL"
            if rule == "RATION": return "PARTIAL" if ration else "NONE"
            return "ELDER" if elder else "NONE"
 
# Alternative 2: match-case (Python 3.10+)
def match_case(units, ration, elder):
    match (units, ration, elder):
        case (u, _, _) if u <= 100: return "FULL"
        case (u, True, _) if 101 <= u <= 200: return "PARTIAL"
        case (u, _, True) if u > 200: return "ELDER"
        case _: return "NONE"
 
tests = [  # (units, ration card, member above 80)
    (50, True, False), (100, False, False), (101, True, False), (101, False, False),
    (200, True, False), (200, False, True), (201, True, False), (201, False, True)]
print(f"{'units':>5} {'ration':>6} {'elder80':>7} | {'separate ifs':<18} | {'if-elif-else':<12} | slab | match")
for t in tests:
    print(f"{t[0]:>5} {str(t[1]):>6} {str(t[2]):>7} | {str(separate_ifs(*t)):<18} | {elif_chain(*t):<12} | {slab_loop(*t):<4} | {match_case(*t)}")
assert all(elif_chain(*t) == slab_loop(*t) == match_case(*t) for t in tests)
 
print("\nTiming 200,000 decisions (units=250, last slab):")
for f in (elif_chain, slab_loop, match_case):
    t = min(timeit.repeat(lambda: f(250, False, True), number=200000, repeat=3))
    print(f"{f.__name__:<11} {t:.4f} s")
print()
for k in (3, 100, 1000):
    limits = [10*i for i in range(1, k)] + [float('inf')]
    def lin(u):
        for i, l in enumerate(limits):
            if u <= l: return i
    t1 = min(timeit.repeat(lambda: lin(10*k), number=2000, repeat=3))
    t2 = min(timeit.repeat(lambda: bisect.bisect_left(limits, 10*k), number=2000, repeat=3))
    print(f"k={k:<5} linear scan {t1:.5f} s   bisect {t2:.5f} s  (2000 decisions)")

