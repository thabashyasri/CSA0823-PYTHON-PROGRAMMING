readings = [4.0, 7.5, 9.2, 55.0, -60.0, 3.5, 1.0, 6.0]

# Version 1: For loop
valid_loop = []

for celsius in readings:
    if -50 <= celsius <= 50:
        valid_loop.append(celsius)

fahrenheit_loop = [
    (c * 9 / 5) + 32 for c in valid_loop
]

# Version 2: List comprehension
valid_comp = [
    c for c in readings if -50 <= c <= 50
]

fahrenheit_comp = [
    (c * 9 / 5) + 32 for c in valid_comp
]

# Version 3: Filter and map
valid_map_filter = list(
    filter(lambda c: -50 <= c <= 50, readings)
)

fahrenheit_map = list(
    map(lambda c: c * 9 / 5 + 32, valid_map_filter)
)

# Find alarm minutes
alarm_minutes = [
    minute
    for minute, c in enumerate(readings, start=1)
    if -50 <= c <= 50 and not (2 <= c <= 8)
]

print("Valid Celsius:", valid_comp)
print("Valid Fahrenheit:", [round(x, 2) for x in fahrenheit_comp])
print("Alarm minutes:", alarm_minutes)

assert valid_loop == valid_comp == valid_map_filter

# Dictionary comprehension
valid_by_minute = {
    minute: c
    for minute, c in enumerate(readings, start=1)
    if -50 <= c <= 50
}

print("Dictionary:", valid_by_minute)

# Set comprehension
valid_temperature_set = {
    c for c in readings if -50 <= c <= 50
}

print("Set:", valid_temperature_set)

# Generator expression
valid_generator = (
    c for c in readings if -50 <= c <= 50
)

print("Generator values:", list(valid_generator))

# Sum using generator
valid_values = (
    c for c in readings if -50 <= c <= 50
)

valid_sum = sum(valid_values)

print("Sum of valid readings:", valid_sum)