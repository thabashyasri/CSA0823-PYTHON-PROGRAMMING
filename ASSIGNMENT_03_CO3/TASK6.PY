from collections import defaultdict

timetable = {
    "12601": {
        "name": "Chennai Mail",
        "stops": [
            ("Chennai", "06:00", "06:10"),
            ("Arakkonam", "07:20", "07:22"),
            ("Katpadi", "08:30", "08:35")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
    },

    "12602": {
        "name": "Southern Express",
        "stops": [
            ("Chennai", "07:00", "07:10"),
            ("Villupuram", "09:00", "09:05"),
            ("Tiruchirappalli", "12:00", "12:10")
        ],
        "days": {"Mon", "Wed", "Fri"}
    },

    "12603": {
        "name": "Coastal Passenger",
        "stops": [
            ("Chennai", "08:00", "08:05"),
            ("Tambaram", "08:30", "08:32"),
            ("Chengalpattu", "09:15", "09:20")
        ],
        "days": {"Tue", "Thu", "Sat"}
    },

    "12604": {
        "name": "Hill Route",
        "stops": [
            ("Katpadi", "10:00", "10:05"),
            ("Jolarpettai", "11:20", "11:25"),
            ("Bengaluru", "14:00", "14:10")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri"}
    },

    "12605": {
        "name": "Delta Intercity",
        "stops": [
            ("Chennai", "16:00", "16:10"),
            ("Villupuram", "18:00", "18:05"),
            ("Thanjavur", "21:00", "21:05")
        ],
        "days": {"Sat", "Sun"}
    }
}


# Find trains by station and day
def find_trains(station, day):
    matches = []

    for number, info in timetable.items():
        if day not in info["days"]:
            continue

        for stop, arrival, departure in info["stops"]:
            if stop.lower() == station.lower():
                matches.append(
                    (number, info["name"], departure)
                )
                break

    return sorted(matches, key=lambda item: item[2])


print(find_trains("Chennai", "Mon"))
print(find_trains("Villupuram", "Sat"))


# Print timetable
for number, info in timetable.items():
    print("\nTrain:", number, "-", info["name"])
    print("Running days:", ", ".join(sorted(info["days"])))

    for station, arrival, departure in info["stops"]:
        print(
            f"{station:18} Arrival {arrival:5} "
            f"Departure {departure:5}"
        )

# Build station index
station_index = defaultdict(list)

for train_no, info in timetable.items():
    for station, arrival, departure in info["stops"]:
        station_index[station].append(
            (train_no, info["name"], arrival, departure, info["days"])
        )


# Indexed query
def indexed_query(station, day):
    result = [
        (train_no, name, departure)
        for train_no, name, arrival, departure, days
        in station_index.get(station, [])
        if day in days
    ]

    return sorted(result, key=lambda item: item[2])


print(indexed_query("Chennai", "Mon"))
print(indexed_query("Unknown Station", "Mon"))