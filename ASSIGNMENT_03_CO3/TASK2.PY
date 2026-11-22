import copy

rows, cols = 3, 4

# Incorrect method
bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct method
good = [[0 for _ in range(cols)] for _ in range(rows)]
good[0][1] = 7

print("Bad:", bad)
print("Good:", good)
print(bad[0] is bad[1], good[0] is good[1])

# Tuples as dictionary keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print(stops[(13.0418, 80.2341)])

# List key error
try:
    locations = {}
    locations[[13.0418, 80.2341]] = "T. Nagar"
except TypeError as error:
    print(type(error).__name__ + ":", error)

# Shallow copy and deep copy
original = [[1, 2], [3, 4]]

alias = original
shallow_a = copy.copy(original)
shallow_b = original[:]
deep = copy.deepcopy(original)

print(alias is original)
print(shallow_a is original)
print(shallow_a[0] is original[0])
print(deep[0] is original[0])

original[0][0] = 99

print("Shallow copy:", shallow_a)
print("Deep copy:", deep)

# Tuple unpacking
stop = (13.0827, 80.2707)

latitude, longitude = stop
print(latitude, longitude)

for latitude, longitude in [
    (13.0827, 80.2707),
    (13.0418, 80.2341)
]:
    print("Lat:", latitude, "Lon:", longitude)

# Mutable object inside a tuple
record = ("bus stop", [10, 20])
record[1].append(30)

print(record)

# Sparse dictionary grid
rows, cols = 3, 4

passengers = {(0, 1): 7, (2, 3): 4}
passengers[(1, 2)] = passengers.get((1, 2), 0) + 5

print(passengers.get((0, 1), 0))