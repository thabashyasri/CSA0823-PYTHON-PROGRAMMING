from decimal import Decimal
 
print(type(10), type(10.0), type("10"), type(True), type([10, 8, 5]))
print(7 / 2)      # 3.5
print(7 // 2)     # 3
print(7 % 2)      # 1
print(-7 // 2)    # -4
print(0.1 + 0.2 == 0.3)  # False
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True
 
payments = ["33.40"] * 1000 + ["0.10"] * 3
float_total = sum(float(x) for x in payments)
decimal_total = sum((Decimal(x) for x in payments), Decimal("0.00"))
print("Float:", float_total)
print("Decimal:", decimal_total)
