import random, time, sys

def loop_clean(data):
    out = []
    for x in data:
        if -50 <= x <= 50:
            out.append(x)
    return out

def comp_clean(data):
    return [x for x in data if -50 <= x <= 50]

def map_filter_clean(data):
    return list(filter(lambda x: -50 <= x <= 50, data))

for n in (10_000, 100_000, 1_000_000):
    data = [random.uniform(-60, 60) for _ in range(n)]
    for name, fn in (("loop", loop_clean),
                     ("comprehension", comp_clean),
                     ("map/filter", map_filter_clean)):
        start = time.perf_counter()
        result = fn(data)
        elapsed = time.perf_counter() - start
        print(n, name, round(elapsed, 6), "items:", len(result))

gen = (x for x in readings if -50 <= x <= 50)
lst = [x for x in readings if -50 <= x <= 50]
print("Generator object bytes:", sys.getsizeof(gen))
print("List object bytes:", sys.getsizeof(lst))
