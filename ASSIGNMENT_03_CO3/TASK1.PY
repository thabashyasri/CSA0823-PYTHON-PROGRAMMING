import random

random.seed(42)
readings = [round(random.uniform(0, 35), 1) for _ in range(365)]

# Weekly totals (the final group may contain fewer than 7 days)
weekly_totals = [
    sum(readings[i:i + 7])
    for i in range(0, len(readings), 7)
]

wettest_index = weekly_totals.index(max(weekly_totals))
driest_index = weekly_totals.index(min(weekly_totals))

# A 7-day moving average; no result is produced if fewer than 7 days exist
moving_average = [
    round(sum(readings[i:i + 7]) / 7, 2)
    for i in range(len(readings) - 6)
]

dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]

print("Number of readings:", len(readings))
print("Number of weekly totals:", len(weekly_totals))
print("Wettest week:", wettest_index + 1, "Total:", weekly_totals[wettest_index])
print("Driest week:", driest_index + 1, "Total:", weekly_totals[driest_index])
print("Number of 7-day averages:", len(moving_average))
print("Dry days:", dry_days)
