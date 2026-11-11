
def read_attendance(data):
    records = []

    for line in data.splitlines():
        parts = line.strip().split(",")

        if len(parts) == 3 and parts[2].strip() in ("P", "A"):
            records.append(tuple(x.strip() for x in parts))

    return records


def calculate_stats(records):
    counts = {}

    for reg, date, status in records:
        counts.setdefault(reg, {"P": 0, "A": 0})
        counts[reg][status] += 1

    return counts


def write_report(stats):
    report = []

    for reg, values in stats.items():
        total = values["P"] + values["A"]

        percent = (
            values["P"] / total * 100 if total else 0
        )

        report.append(f"{reg},{percent:.2f}%")

    return report


if __name__ == "__main__":

    data = (
        "192311001,2026-11-01,P\n"
        "192311001,2026-11-02,P\n"
        "192311001,2026-11-03,A\n"
        "192311002,2026-11-01,A\n"
        "192311002,2026-11-02,P\n"
        "192311002,2026-11-03,A\n"
        "192311003,2026-11-01,P\n"
        "192311003,2026-11-02,P\n"
        "192311003,2026-11-03,P\n"
    )

    records = read_attendance(data)
    stats = calculate_stats(records)
    report = write_report(stats)

    print("ATTENDANCE REPORT")
    print("-------------------------")

    for row in report:
        print(row)

    print("\nTotal records:", len(records))
