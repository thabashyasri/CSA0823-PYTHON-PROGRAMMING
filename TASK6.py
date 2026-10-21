BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
 
def rate_per_litre(fat, snf):
    """Calculate the rate per litre."""
    fs = round((fat - 3.5) / 0.1)
    ss = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fs * FAT_STEP_VALUE + ss * SNF_STEP_VALUE, 2)
 
def payout(litres, fat, snf):
    """Calculate payment for one entry."""
    return round(litres * rate_per_litre(fat, snf), 2)
 
def ten_day_total(payments):
    """Calculate total payments."""
    return round(sum(payments), 2)
 
payments = [payout(10, 3.5, 8.5), payout(8.5, 4.2, 8.7), payout(12, 3.1, 8.3)]
print(payments)
print(f"Total: Rs {ten_day_total(payments):.2f}")
