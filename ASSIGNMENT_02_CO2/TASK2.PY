import timeit

def otp_while(entries, correct="4821"):
    attempts, i = 0, 0

    while attempts < 3:
        if i >= len(entries):
            break

        code = entries[i].strip()
        i += 1

        if code == "":
            continue

        attempts += 1

        if code == correct:
            return f"verified on attempt {attempts}"

    else:
        return "LOCKED for 30 minutes"

    return "ended (no more input)"


def otp_for(entries, correct="4821"):
    it = iter(entries)

    for attempt in range(3):
        while True:
            code = next(it, None)

            if code is None:
                return "ended (no more input)"

            if code.strip() != "":
                break

        if code.strip() == correct:
            return f"verified on attempt {attempt + 1}"
        else:
            pass

    else:
        return "LOCKED for 30 minutes"


def otp_extended(entries, security_ok, correct="4821"):
    limit, attempts, i = 3, 0, 0

    while attempts < limit:
        if i >= len(entries):
            return "ended (no more input)"

        code = entries[i].strip()
        i += 1

        if code == "":
            continue

        attempts += 1

        if code == correct:
            return f"verified on attempt {attempts}"

        if attempts == 3 and limit == 3 and security_ok:
            limit = 5

    return "LOCKED for 30 minutes"


def otp_recursive(entries, i=0, attempts=0, correct="4821"):

    if attempts == 3:
        return "LOCKED for 30 minutes"

    if i >= len(entries):
        return "ended (no more input)"

    code = entries[i].strip()

    if code == "":
        return otp_recursive(entries, i + 1, attempts, correct)

    if code == correct:
        return f"verified on attempt {attempts + 1}"

    return otp_recursive(entries, i + 1, attempts + 1, correct)


cases = {
    "right on 2nd": ["1111", "4821"],
    "blank then right": ["", "4821"],
    "3 wrong": ["1", "2", "3"],
    "blanks + 3 wrong": ["", "1", "", "2", "3"]
}

for name, e in cases.items():
    print(
        name,
        "while:", otp_while(e),
        "for:", otp_for(e),
        "recursive:", otp_recursive(e)
    )

print("Extended security OK:",
      otp_extended(["1", "2", "3", "4", "4821"], True))

print("Extended security FAIL:",
      otp_extended(["1", "2", "3", "4", "4821"], False))


def wrong_counter(entries, correct="4821"):
    attempts = 0

    for code in entries:
        attempts += 1

        if code.strip() == "":
            continue

        if code == correct:
            return f"verified on attempt {attempts}"

        if attempts == 3:
            return "LOCKED"

    return "no result"


print("Wrong counter:",
      wrong_counter(["", "1", "2", "4821"]))

print("Right counter:",
      otp_while(["", "1", "2", "4821"]))

print("Time for 100000 runs:")

print("While:",
      timeit.timeit(
          lambda: otp_while(["1", "2", "3"]),
          number=100000
      ))

print("Recursive:",
      timeit.timeit(
          lambda: otp_recursive(["1", "2", "3"]),
          number=100000
      ))