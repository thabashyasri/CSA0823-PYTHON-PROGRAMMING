readings = [
    ("Adyar", "2026-10-01", 48),
    ("Adyar", "2026-10-01", 60),
    ("Guindy", "2026-10-01", 95),
    ("Guindy", "2026-10-01", 105)
]

groups = defaultdict(list)
for station, day, pm25 in readings:
    groups[(station, day)].append(pm25)

for key, vals in sorted(groups.items()):
    print(key, "min =", min(vals),
          "max =", max(vals),
          "mean =", round(sum(vals) / len(vals), 2),
          "count =", len(vals))
