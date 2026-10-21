def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = 30.00 + fat_steps * 0.40 + snf_steps * 0.30
    return round(rate, 2)
 
def payout(litres, fat, snf):
    return round(litres * rate_per_litre(fat, snf), 2)
 
print(rate_per_litre(3.5, 8.5))  # 30.00
print(payout(8.5, 4.2, 8.7))     # 283.90
print(payout(12, 3.1, 8.3))      # 333.60
print(2.0 <= 4.2 <= 7.0)        # True
print(int(7.9), round(7.9))      # 7 8
print(-7 // 2)                   # -4
