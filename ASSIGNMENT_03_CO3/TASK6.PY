import random, time

stations = ["Chennai", "Tambaram", "Villupuram", "Katpadi",
            "Salem", "Madurai", "Coimbatore", "Erode"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def make_timetable(count):
    data = {}
    for i in range(count):
        chosen = random.sample(stations, 5)
        data[str(10000 + i)] = {
            "name": "Train " + str(i),
            "stops": [(s, "08:00", "08:05") for s in chosen],
            "days": set(random.sample(days, 5))
        }
    return data

def build_index(data):
    idx = {}
    for no, info in data.items():
        for station, arr, dep in info["stops"]:
            idx.setdefault(station, []).append((no, dep, info["days"]))
    return idx

for count in (100, 1000, 10000):
    data = make_timetable(count)
    idx = build_index(data)
    start = time.perf_counter()
    slow_result = [(no, info["name"]) for no, info in data.items()
                   if "Mon" in info["days"] and
                   any(s == "Chennai" for s, a, d in info["stops"])]
    scan_time = time.perf_counter() - start

    start = time.perf_counter()
    fast_result = [(no, dep) for no, dep, run_days in idx.get("Chennai", [])
                   if "Mon" in run_days]
    index_time = time.perf_counter() - start
    print(count, "scan:", round(scan_time, 6),
          "index:", round(index_time, 6))
    print("Index entries:", sum(len(v) for v in idx.values()))
