values = ["48", "NA", "", "-5", "95", "121", "1500"]

cleaned = []
for item in values:
    if item == "" or item.upper() == "NA":
        continue
    number = float(item)
    if 0 <= number <= 999:
        cleaned.append(number)

low, high = min(cleaned), max(cleaned)
normalised = [
    round((x - low) / (high - low), 3) if high != low else 0.0
    for x in cleaned
]

print("Cleaned values:", cleaned)
print("Min-max values:", normalised)
