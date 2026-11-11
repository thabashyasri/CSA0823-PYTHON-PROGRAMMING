import re
import time
import random

def normalise_phone(phone):
    if not phone:
        return ""
    digits = re.sub(r"\\D", "", str(phone))
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    if len(digits) == 10:
        return digits
    return digits  # keep other digit strings, but validate before production use

def normalise_name(name):
    if not name:
        return ""
    return " ".join(str(name).strip().split()).title()

def normalise_email(email):
    return str(email).strip().lower() if email else ""

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

contacts = [
    {"name": "Dr. Ravi", "phone": "+91 98400 12345", "email": "RAVI@MAIL.COM"},
    {"name": "ravi kumar", "phone": "9840012345", "email": "ravi.alt@mail.com"},
    {"name": "Meena", "phone": "98765-43210", "email": "meena@mail.com"},
    {"name": "Ravi", "phone": "", "email": "unknown@mail.com"},
    {"name": "", "phone": "9840012345", "email": ""}
]

merged, review = merge_contacts(contacts)

for phone, details in sorted(merged.items()):
    print("Phone:", phone)
    print("Names:", sorted(details["names"]))
    print("Numbers:", sorted(details["phones"]))
    print("Emails:", sorted(details["emails"]))
print("Manual review:", review) 
