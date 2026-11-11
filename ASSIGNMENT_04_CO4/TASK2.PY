def process_attendance():

    attendance = {}
    damaged_records = []
    dates_seen = set()

    daily_files = {
        "day1.txt": [
            "101,2026-11-01,P",
            "102,2026-11-01,A",
            "103,2026-11-01,P",
            "104,2026-11-01,A"
        ],

        "day2.txt": [
            "101,2026-11-02,P",
            "102,2026-11-02,P",
            "103,2026-11-02,A",
            "104,2026-11-02,A"
        ],

        "day3.txt": [
            "101,2026-11-03,P",
            "102,2026-11-03,A",
            "103,2026-11-03,P",
            "104,2026-11-03,X",
            "101,2026-11-01,A"
        ]
    }

    for filename, lines in daily_files.items():

        for line_number, line in enumerate(lines, start=1):

            line = line.strip()

            if not line:
                continue

            parts = line.split(",")

            if len(parts) != 3:
                damaged_records.append(
                    (filename, line_number, "Expected 3 fields")
                )
                continue

            reg_no, date, status = map(str.strip, parts)

            if status not in ("P", "A"):
                damaged_records.append(
                    (filename, line_number, "Invalid status")
                )
                continue

            key = (reg_no, date)

            if key in dates_seen:
                damaged_records.append(
                    (filename, line_number, "Duplicate record")
                )
                continue

            dates_seen.add(key)

            if reg_no not in attendance:
                attendance[reg_no] = {
                    "present": 0,
                    "absent": 0
                }

            if status == "P":
                attendance[reg_no]["present"] += 1
            else:
                attendance[reg_no]["absent"] += 1

    print("ATTENDANCE SUMMARY")
    print("-" * 55)

    for reg_no, details in sorted(attendance.items()):

        present = details["present"]
        absent = details["absent"]
        working_days = present + absent
        percentage = (present / working_days) * 100

        print(
            reg_no, present, absent,
            working_days, round(percentage, 2), "%"
        )

    print("\nSTUDENTS BELOW 75%")
    print("-" * 30)

    for reg_no, details in sorted(attendance.items()):

        present = details["present"]
        absent = details["absent"]
        working_days = present + absent
        percentage = (present / working_days) * 100

        if percentage < 75:
            print(reg_no, round(percentage, 2), "%")

    print("\nDAMAGED RECORDS")
    print("-" * 30)

    for record in damaged_records:
        print(record)

    print("\nTotal students:", len(attendance))
    print("Total damaged records:", len(damaged_records))


if __name__ == "__main__":
    process_attendance()


