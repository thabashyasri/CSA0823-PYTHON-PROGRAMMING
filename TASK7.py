BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
 
def rate_per_litre(fat, snf):
    """Return rate per litre."""
    fs = round((fat - 3.5) / 0.1)
    ss = round((snf - 8.5) / 0.1)
    return round(BASE_RATE + fs * FAT_STEP_VALUE + ss * SNF_STEP_VALUE, 2)
 
def payout(litres, fat, snf):
    """Return payment amount."""
    return round(litres * rate_per_litre(fat, snf), 2)
 
if __name__ == "__main__":
    for entry in [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]:
        litres, fat, snf = entry
        print(rate_per_litre(fat, snf), payout(litres, fat, snf))


import milkrate as mr
 
print(mr.rate_per_litre(4.2, 8.7))
print(mr.payout(8.5, 4.2, 8.7))
