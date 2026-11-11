
class InvalidRecord(Exception):
    pass


def parse_line(line):
    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord(
            f"Expected 3 fields, found {len(parts)}"
        )

    register_no, date, status = [x.strip() for x in parts]

    if status not in ("P", "A"):
        raise InvalidRecord(f"Invalid status {status!r}")

    return register_no, date, status


def summarise(data, filename):
    present = 0
    absent = 0
    errors = []

    try:
        for line_number, line in enumerate(data.splitlines(), start=1):

            if not line.strip():
                continue

            try:
                record = parse_line(line)

            except InvalidRecord as error:
                errors.append((line_number, str(error)))
                continue

            if record[2] == "P":
                present += 1
            else:
                absent += 1

    finally:
        print("Finished processing attempt:", filename)

    return present, absent, errors


data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)

try:
    result = summarise(data, "attendance.csv")
    print("Attendance Summary:")
    print("Present:", result[0])
    print("Absent:", result[1])
    print("Errors:", result[2])

except Exception as error:
    print(error)


print("\nMissing-file test:")
try:
    raise RuntimeError(
        "Attendance file not found: missing_attendance.csv"
    )
except RuntimeError as error:
    print(error)
