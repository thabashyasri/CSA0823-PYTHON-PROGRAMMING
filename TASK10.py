tests = [
    (10, 3.5, 8.5, 30.00, 300.00),
    (8.5, 4.2, 8.7, 33.40, 283.90),
    (12, 3.1, 8.3, 27.80, 333.60),
]
for litres, fat, snf, expected_rate, expected_pay in tests:
    actual_rate = rate_per_litre(fat, snf)
    actual_pay = payout(litres, fat, snf)
    print("Rate:", actual_rate, "Expected:", expected_rate)
    print("Pay:", actual_pay, "Expected:", expected_pay)
 
from decimal import Decimal
values = ["33.40"] * 1000 + ["0.10"] * 3
print(sum((Decimal(x) for x in values), Decimal("0.00")))  # 33400.30
