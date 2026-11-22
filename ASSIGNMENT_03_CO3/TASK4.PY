ai_elective = {
    "192311001", "192311004",
    "192311007", "192311009"
}

iot_elective = {
    "192311002", "192311004",
    "192311009", "192311010"
}

all_students = {
    f"1923110{i:02d}" for i in range(1, 11)
}

# Set operators
both = ai_elective & iot_elective
exactly_one = ai_elective ^ iot_elective
neither = all_students - (ai_elective | iot_elective)

print("Clash:", sorted(both))
print("Exactly one:", sorted(exactly_one))
print("Neither:", sorted(neither))

# Set methods
both_method = ai_elective.intersection(iot_elective)

exactly_one_method = ai_elective.symmetric_difference(
    iot_elective
)

registered = ai_elective.union(iot_elective)

neither_method = all_students.difference(registered)

assert both == both_method
assert exactly_one == exactly_one_method
assert neither == neither_method

print("Set methods verified successfully")

# Membership comparison
import time

for n in (10000, 100000, 1000000):
    values = list(range(n))
    value_set = set(values)
    target = n - 1

    start = time.perf_counter()
    target in values
    list_time = time.perf_counter() - start

    start = time.perf_counter()
    target in value_set
    set_time = time.perf_counter() - start

    print(n, "List:", round(list_time, 8),
          "Set:", round(set_time, 8))

# Set intersection
a = set(range(0, 20000, 2))
b = set(range(10000, 30000, 3))

start = time.perf_counter()
common = a & b

print("Intersection time:", time.perf_counter() - start)
print("Common count:", len(common))