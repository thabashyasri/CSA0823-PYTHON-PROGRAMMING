import random, time

for n in (10_000, 100_000, 1_000_000):
    values = list(range(n))
    value_set = set(values)
    target = n - 1

    start = time.perf_counter()
    target in values
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    target in value_set
    set_time = time.perf_counter() - start

    print(n, "list:", round(list_time, 8),
          "set:", round(set_time, 8))

# Compare intersections
a = set(range(0, 20000, 2))
b = set(range(10000, 30000, 3))
start = time.perf_counter()
common = a & b
print("Set intersection time:", time.perf_counter() - start,
      "common count:", len(common))
