import csv
import io
import sqlite3
from collections import defaultdict
import pandas as pd

data = """station,day,pm25
Adyar,2026-10-01,48
Adyar,2026-10-01,60
Guindy,2026-10-01,95
Guindy,2026-10-01,105
Adyar,2026-10-02,70
"""

# Method 1: Python loops
reader = csv.DictReader(io.StringIO(data))
groups = defaultdict(list)

for row in reader:
    key = (row["station"], row["day"])
    groups[key].append(float(row["pm25"]))

print("Python Loops:")
for key, values in sorted(groups.items()):
    print(key, sum(values) / len(values))

# Method 2: Pandas
df = pd.read_csv(io.StringIO(data))
print("\nPandas GroupBy:")
print(df.groupby(["station", "day"])["pm25"].mean())

# Method 3: SQL
con = sqlite3.connect(":memory:")
df.to_sql("aq", con, index=False)

print("\nSQL GROUP BY:")
result = con.execute("""
SELECT station, day, AVG(pm25)
FROM aq
GROUP BY station, day
ORDER BY station, day
""")

for row in result:
    print(row)

con.close()
