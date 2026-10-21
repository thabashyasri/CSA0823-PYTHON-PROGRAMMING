from decimal import Decimal, ROUND_HALF_UP
 
def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
 
def read_decimal(prompt):
    while True:
        try:
            value = Decimal(input(prompt).strip())
            if not value.is_finite():
                raise ValueError
            return value
        except (ValueError, ArithmeticError):
            print("Enter a valid number.")
 
def rate_per_litre(fat, snf):
    fs = round((float(fat) - 3.5) / 0.1)
    ss = round((float(snf) - 8.5) / 0.1)
    return money(30 + fs * 0.40 + ss * 0.30)
 
def payout(litres, fat, snf):
    return money(litres * rate_per_litre(fat, snf))
 
def main():
    farmer = input("Farmer ID: ").strip()
    total = Decimal("0.00")
    for day in range(1, 11):
        print("Entry", day)
        litres = read_decimal("Litres: ")
        fat = read_decimal("Fat: ")
        snf = read_decimal("SNF: ")
        if litres < 0 or not Decimal("2") <= fat <= Decimal("7") or snf < 0:
            print("Invalid values; entry skipped.")
            continue
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        total += amount
        print(f"Rate Rs {rate:.2f}; payment Rs {amount:.2f}")
    print(f"{farmer} total: Rs {total:.2f}")
 
if __name__ == "__main__":
    main()
