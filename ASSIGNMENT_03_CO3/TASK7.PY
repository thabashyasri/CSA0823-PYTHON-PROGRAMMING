import re
import time


# Normalize phone number
def normalise_phone(phone):
    if not phone:
        return ""

    digits = re.sub(r"\D", "", str(phone))

    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]

    if len(digits) == 10:
        return digits

    return digits


# Normalize name
def normalise_name(name):
    if not name:
        return ""

    return " ".join(str(name).strip().split()).title()


# Normalize email
def normalise_email(email):
    return str(email).strip().lower() if email else ""


# Merge contacts
def merge_contacts(contact_lists):
    merged = {}
    review = []

    for contact in contact_lists:
        name = normalise_name(contact.get("name"))
        phone = normalise_phone(contact.get("phone"))
        email = normalise_email(contact.get("email"))

        if not phone:
            review.append({
                "name": name,
                "email": email,
                "reason": "No usable phone number"
            })
            continue

        if phone not in merged:
            merged[phone] = {
                "names": set(),
                "phones": set(),
                "emails": set()
            }

        if name:
            merged[phone]["names"].add(name)

        merged[phone]["phones"].add(phone)

        if email:
            merged[phone]["emails"].add(email)

    return merged, review


# Input contacts
contacts = [
    {
        "name": "Dr. Ravi",
        "phone": "+91 98400 12345",
        "email": "RAVI@MAIL.COM"
    },

    {
        "name": "ravi kumar",
        "phone": "9840012345",
        "email": "ravi.alt@mail.com"
    },

    {
        "name": "Meena",
        "phone": "98765-43210",
        "email": "meena@mail.com"
    },

    {
        "name": "Ravi",
        "phone": "",
        "email": "unknown@mail.com"
    },

    {
        "name": "",
        "phone": "9840012345",
        "email": ""
    }
]


merged, review = merge_contacts(contacts)

# Display merged contacts
for phone, details in sorted(merged.items()):
    print("Phone:", phone)
    print("Names:", sorted(details["names"]))
    print("Numbers:", sorted(details["phones"]))
    print("Emails:", sorted(details["emails"]))

print("Manual review:", review)


# Performance measurement
def generate_contacts(n):
    data = []

    for i in range(n):
        number = 9000000000 + (i % max(1, n // 2))

        data.append({
            "name": "Person " + str(i),
            "phone": str(number),
            "email": "person" + str(i) + "@example.com"
        })

    return data


for n in (1000, 100000):
    sample = generate_contacts(n)

    start = time.perf_counter()

    result, review_items = merge_contacts(sample)

    elapsed = time.perf_counter() - start

    print(
        n, "contacts:",
        round(elapsed, 6),
        "seconds; merged groups:",
        len(result)
    )