def calculate_entry(litres, fat, snf):
    fs = round((fat - 3.5) / 0.1)
    ss = round((snf - 8.5) / 0.1)
    rate = round(30 + fs * 0.40 + ss * 0.30, 2)
    return rate, round(litres * rate, 2)
 
entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
total = 0.00
for litres, fat, snf in entries:
    rate, amount = calculate_entry(litres, fat, snf)
    print(f"Rate Rs {rate:.2f}; payment Rs {amount:.2f}")
    total = round(total + amount, 2)
print(f"Ten-day total: Rs {total:.2f}")
