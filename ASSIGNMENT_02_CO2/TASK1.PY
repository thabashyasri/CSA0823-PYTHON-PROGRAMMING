import timeit
import bisect

def separate_ifs(units, ration, elder):
    result = []

    if units <= 100:
        result.append("FULL")

    if units <= 200 and ration:
        result.append("PARTIAL")

    if units > 200 and elder:
        result.append("ELDER")

    if not result:
        result.append("NONE")

    return result


def elif_chain(units, ration, elder):
    if units <= 100:
        return "FULL"
    elif 101 <= units <= 200 and ration:
        return "PARTIAL"
    elif units > 200 and elder:
        return "ELDER"
    else:
        return "NONE"


SLABS = [
    (100, "FULL"),
    (200, "RATION"),
    (float("inf"), "ELDER")
]


def slab_loop(units, ration, elder):
    for limit, rule in SLABS:
        if units <= limit:
            if rule == "FULL":
                return "FULL"
            if rule == "RATION":
                return "PARTIAL" if ration else "NONE"
            return "ELDER" if elder else "NONE"


def match_case(units, ration, elder):
    match (units, ration, elder):
        case (u, _, _) if u <= 100:
            return "FULL"
        case (u, True, _) if 101 <= u <= 200:
            return "PARTIAL"
        case (u, _, True) if u > 200:
            return "ELDER"
        case _:
            return "NONE"


tests = [
    (50, True, False),
    (100, False, False),
    (101, True, False),
    (101, False, False),
    (200, True, False),
    (200, False, True),
    (201, True, False),
    (201, False, True)
]

print("Units  Ration  Elder  Separate IFs  IF-ELIF-ELSE")

for t in tests:
    print(t[0], t[1], t[2],
          separate_ifs(*t),
          elif_chain(*t))

assert all(
    elif_chain(*t) == slab_loop(*t) == match_case(*t)
    for t in tests
)

print("\nAll boundary tests passed.")

print("\nTiming 200000 decisions:")

for f in (elif_chain, slab_loop, match_case):
    t = min(timeit.repeat(
        lambda: f(250, False, True),
        number=200000,
        repeat=3
    ))
    print(f.__name__, t)

for k in (3, 100, 1000):
    limits = [10*i for i in range(1, k)] + [float("inf")]

    def lin(u):
        for i, l in enumerate(limits):
            if u <= l:
                return i

    t1 = min(timeit.repeat(
        lambda: lin(10*k), number=2000, repeat=3
    ))

    t2 = min(timeit.repeat(
        lambda: bisect.bisect_left(limits, 10*k),
        number=2000, repeat=3
    ))

    print("k =", k, "Linear =", t1, "Bisect =", t2)
