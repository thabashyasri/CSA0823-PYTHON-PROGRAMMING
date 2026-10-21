def read_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid number. Try again.")
 
farmer_id = input("Farmer ID: ").strip()
litres = read_number("Litres: ")
fat = read_number("Fat percentage: ")
snf = read_number("SNF percentage: ")
 
if litres < 0 or not 2.0 <= fat <= 7.0 or snf < 0:
    print("Invalid values")
else:
    print(f"{farmer_id:<12} {litres:>8.2f} L "
          f"Fat {fat:>5.2f} SNF {snf:>5.2f}")
