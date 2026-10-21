entries = [
    {"farmer_id": "F001", "litres": 10, "fat": 3.5, "snf": 8.5},
    {"farmer_id": "F001", "litres": 8.5, "fat": 4.2, "snf": 8.7},
]
total = 0.00
for entry in entries:
    amount = payout(entry["litres"], entry["fat"], entry["snf"])
    total += amount
print(f"Farmer F001 total: Rs {total:.2f}")
