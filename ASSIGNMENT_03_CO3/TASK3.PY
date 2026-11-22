import re
from collections import Counter, defaultdict

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}


def frequencies(texts, stop):
    counts = {}

    for text in texts:
        for word in text.lower().split():
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts


def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]


print(top(frequencies(calls, STOP), 3))


# Improved complaint processing
def clean_words(text):
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
    {"district": "Chennai", "crop": "rice",
     "text": "Seeds not received!"},
    {"district": "Madurai", "crop": "cotton",
     "text": "Fertiliser price high."},
    {"district": "Chennai", "crop": "rice",
     "text": "Seeds delayed; seeds needed."}
]

stop_words = {"not", "high", "the", "is"}

counts, district_groups, crop_groups = analyse_complaints(
    records, stop_words
)

print("Word counts:", counts)
print("Top words:", sorted(
    counts.items(), key=lambda x: (-x[1], x[0])
)[:5])
print("By district:", district_groups)
print("By crop:", crop_groups)

# Counter method
words = [
    word for text in calls
    for word in clean_words(text)
]

counter_result = Counter(w for w in words if w not in STOP)

print("Counter result:", counter_result.most_common(3))