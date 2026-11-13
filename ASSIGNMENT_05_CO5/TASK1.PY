import csv
from io import StringIO

csv_text = """station,date,hour,pm25,pm10,no,temperature
Adyar,2026-10-01,10,48,80,15,30
Guindy,2026-10-01,11,95,120,20,86
"""

reader = csv.DictReader(StringIO(csv_text))
print("CSV columns:", reader.fieldnames)

for row in reader:
    print("Station:", row["station"])
    print("Date:", row["date"])
    print("PM2.5:", row["pm25"])
    print("Temperature:", row["temperature"])
