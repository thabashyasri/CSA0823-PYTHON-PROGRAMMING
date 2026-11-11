import re
from collections import Counter, defaultdict

def clean_words(text):
    # Keep alphabetic words and convert them to lowercase
    return re.findall(r"[a-z]+", text.lower())

def analyse_complaints(records, stop_words):
    counts = {}
    by_district = defaultdict(list)
    by_crop = defaultdict(list)

    for record in records:
        complaint = record["text"]
        district = record["district"]
        crop = record["crop"]

        by_district[district].append(complaint)
        by_crop[crop].append(complaint)

        for word in clean_words(complaint):
            if word not in stop_words:
                counts[word] = counts.get(word, 0) + 1

    return counts, dict(by_district), dict(by_crop)

records = [
    {"district": "Chennai", "crop": "rice", "text": "Seeds not received!"},
    {"district": "Madurai", "crop": "cotton", "text": "Fertiliser price high."},
    {"district": "Chennai", "crop": "rice", "text": "Seeds delayed; seeds needed."},
]
stop_words = {"not", "high", "the", "is"}
counts, district_groups, crop_groups = analyse_complaints(records, stop_words)
print("Word counts:", counts)
print("Top words:", sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:5])
print("By district:", district_groups)
print("By crop:", crop_groups)
