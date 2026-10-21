BASE_RATE = 32.00
FAT_STEP_VALUE = 0.45
SNF_STEP_VALUE = 0.30
BONUS_THRESHOLD = 500
BONUS_PER_LITRE = 0.50
 
def revised_rate(fat, snf):
    fs = round((fat - 3.5) / 0.1)
    ss = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fs * FAT_STEP_VALUE + ss * SNF_STEP_VALUE, 2)
 
def revised_payout(litres, fat, snf):
    return round(litres * revised_rate(fat, snf), 2)
 
def bonus(total_litres):
    # Assumption: once total exceeds 500 L, every litre earns the bonus.
    return round(total_litres * BONUS_PER_LITRE, 2) if total_litres > BONUS_THRESHOLD else 0.00
 
def final_total(payments, total_litres):
    return round(sum(payments) + bonus(total_litres), 2)
 
entries = [(10, 3.50, 8.50), (8.5, 4.20, 8.70), (12, 3.10, 8.30)]
payments = []
litres_total = 0
for litres, fat, snf in entries:
    amount = revised_payout(litres, fat, snf)
    payments.append(amount)
    litres_total += litres
    print(f"Payment: Rs {amount:.2f}")
print("Litres:", litres_total)
print(f"Bonus: Rs {bonus(litres_total):.2f}")
print(f"Final total: Rs {final_total(payments, litres_total):.2f}")
