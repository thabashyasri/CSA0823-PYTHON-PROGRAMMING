BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
 
farmer_id = input("Farmer ID: ")
litres = float(input("Litres: "))
fat = float(input("Fat percentage: "))
snf = float(input("SNF percentage: "))
 
if litres < 0 or not 2.0 <= fat <= 7.0 or snf < 0:
    print("Invalid input")
else:
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    amount = round(litres * rate, 2)
    print("Farmer:", farmer_id)
    print(f"Rate: Rs {rate:.2f}")
    print(f"Payment: Rs {amount:.2f}")
