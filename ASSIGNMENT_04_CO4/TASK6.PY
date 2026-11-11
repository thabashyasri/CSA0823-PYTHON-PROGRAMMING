
class InvalidRecord(Exception):
    pass


FILES = {
    "biology.txt": [
        "101,Arun,Biology,arun@gmail.com,Quiz;Seminar",
        "102,Bala,Biology,bala@gmail.com,Workshop"
    ],

    "chemistry.txt": [
        "103,Charan,Chemistry,charan@gmail.com,Quiz;Workshop",
        "104,David,Chemistry,david@gmail.com,Seminar"
    ],

    "computer_science.txt": [
        "105,Elan,Computer Science,elan@gmail.com,Quiz;Hackathon",
        "106,Feroz,Computer Science,invalid-email,Hackathon"
    ],

    "physics.txt": [
        "107,Gokul,Physics,gokul@gmail.com,Seminar",
        "101,Arun,Physics,arun@gmail.com,Workshop"
    ],

    "mathematics.txt": [
        "108,Harish,Mathematics,harish@gmail.com,Quiz",
        "109,Kiran,Mathematics,kiran@gmail.com,"
    ]
}


def valid_email(email):
    if " " in email or email.count("@") != 1:
        return False

    local, domain = email.split("@")

    return bool(
        local and domain and "." in domain
        and not domain.startswith(".")
        and not domain.endswith(".")
    )


def parse_record(line):
    fields = [x.strip() for x in line.strip().split(",")]

    if len(fields) != 5:
        raise InvalidRecord("Expected 5 fields")

    reg, name, dept, email, events_text = fields

    if not reg or not name or not dept:
        raise InvalidRecord("Required field is empty")

    if not valid_email(email):
        raise InvalidRecord("Invalid email")

    events = [
        x.strip() for x in events_text.split(";") if x.strip()
    ]

    if not events:
        raise InvalidRecord("No event selected")

    return {
        "reg": reg,
        "name": name,
        "dept": dept,
        "email": email,
        "events": events
    }


def process_files():
    seen_registers = set()
    master = []
    event_groups = {}
    errors = []

    for filename, lines in FILES.items():

        for line_no, line in enumerate(lines, start=1):

            if not line.strip():
                continue

            try:
                record = parse_record(line)
                reg = record["reg"]

                if reg in seen_registers:
                    raise InvalidRecord(
                        "Duplicate register number"
                    )

                seen_registers.add(reg)
                master.append(record)

                for event in record["events"]:
                    event_groups.setdefault(event, []).append(record)

            except InvalidRecord as error:
                errors.append(
                    f"{filename}:{line_no}: {line} | {error}"
                )

    print("MASTER REGISTRATION LIST")
    print("-" * 65)

    for rec in master:
        print(
            rec["reg"], rec["name"],
            rec["dept"], rec["email"],
            ", ".join(rec["events"])
        )

    print("\nEVENT-WISE PARTICIPANTS")
    print("-" * 40)

    for event, participants in sorted(event_groups.items()):
        print("\nEvent:", event)

        for rec in participants:
            print(
                rec["reg"], "-", rec["name"],
                "-", rec["dept"]
            )

    print("\nSUMMARY")
    print("-" * 40)
    print("Unique valid registrations:", len(master))
    print("Number of events:", len(event_groups))
    print("Rejected records:", len(errors))

    print("\nREJECTED RECORDS")

    for error in errors:
        print(error)


if __name__ == "__main__":
    process_files()
