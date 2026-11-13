POSITIVE = {"good", "clean", "helpful", "improved"}
NEGATIVE = {"bad", "dirty", "slow", "smoke"}
NEGATORS = {"not", "never", "no"}

def sentiment(text):
    words = text.lower().replace(".", "").split()
    score = 0
    for i, word in enumerate(words):
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if i > 0 and words[i - 1] in NEGATORS:
            value = -value
        score += value
    return "positive" if score > 0 else "negative" if score < 0 else "neutral"

def chatbot(question):
    q = question.lower()
    if "pm2.5" in q and "adyar" in q:
        return "Adyar PM2.5 reading: 48"
    return "Sorry, I can answer only predefined station questions."

print("Sentiment:", sentiment("The air is not bad"))
print("Chatbot:", chatbot("What is the PM2.5 in Adyar today?"))
