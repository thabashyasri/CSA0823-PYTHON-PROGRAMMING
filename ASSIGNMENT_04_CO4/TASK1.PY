
from decimal import Decimal, InvalidOperation

def process_mess_file(filename):
    total = Decimal("0.00")
    report_rows = []
    rejected_lines = []

    data = [
        "101,Arun,1500",
        "102,Bala,1800",
        "103,Charan,1200",
        "104,David,-500",
        "105,Elan,abc",
        "106,Feroz,2000"
    ]

    for line_number, line in enumerate(data, start=1):
        line = line.strip()

        if not line:
            continue

        parts = line.split(",")

        if len(parts) != 3:
            rejected_lines.append(
                (line_number, line, "Expected 3 fields")
            )
            continue

        reg_no, name, amount_text = map(str.strip, parts)

        try:
            amount = Decimal(amount_text)

            if not amount.is_finite():
                raise ValueError("Invalid amount")

            if amount < 0:
                raise ValueError("Negative amount")

        except (InvalidOperation, ValueError) as error:
            rejected_lines.append(
                (line_number, line, str(error))
            )
            continue

        total += amount
        report_rows.append(
            f"{reg_no} {name} {amount:.2f}"
        )

    print("MESS BILL REPORT")

    for row in report_rows:
        print(row)

    print("Total:", total)

    print("\nREJECTED RECORDS")

    for item in rejected_lines:
        print(item)


if __name__ == "__main__":
    process_mess_file("mess_oct.txt")
