import random

random.seed(42)

readings = [round(random.uniform(0, 35), 1) for _ in range(365)]

# Weekly totals
weekly_totals = [
    sum(readings[i:i + 7])
    for i in range(0, len(readings), 7)
]

wettest_index = weekly_totals.index(max(weekly_totals))
driest_index = weekly_totals.index(min(weekly_totals))

# 7-day moving average
moving_average = [
    round(sum(readings[i:i + 7]) / 7, 2)
    for i in range(len(readings) - 6)
]

# Find dry days
dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]

print("Number of readings:", len(readings))
print("Number of weekly totals:", len(weekly_totals))
print("Wettest week:", wettest_index + 1,
      "Total:", weekly_totals[wettest_index])
print("Driest week:", driest_index + 1,
      "Total:", weekly_totals[driest_index])
print("Number of 7-day averages:", len(moving_average))
print("Dry days:", dry_days)

# Slicing examples
print("Second week:", readings[7:14])
print("Last seven readings:", readings[-7:])
print("Every seventh reading:", readings[::7])


# Moving average using running sum
def moving_average_running(values, window=7):
    if len(values) < window:
        return []

    current = sum(values[:window])
    result = [current / window]

    for i in range(window, len(values)):
        current += values[i] - values[i - window]
        result.append(current / window)

    return result


print("Running average:", moving_average_running(readings))