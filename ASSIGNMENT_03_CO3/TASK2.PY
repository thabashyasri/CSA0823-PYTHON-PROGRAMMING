import sys, timeit

values = list(range(1_000_000))
tuple_values = tuple(values)
print("List container bytes:", sys.getsizeof(values))
print("Tuple container bytes:", sys.getsizeof(tuple_values))

list_create = timeit.timeit("list(range(10000))", number=100)
tuple_create = timeit.timeit("tuple(range(10000))", number=100)
list_index = timeit.timeit("values[5000]", globals={"values": values}, number=1_000_000)
tuple_index = timeit.timeit("values[5000]", globals={"values": tuple_values}, number=1_000_000)
print("Create list:", list_create)
print("Create tuple:", tuple_create)
print("Index list:", list_index)
print("Index tuple:", tuple_index)
