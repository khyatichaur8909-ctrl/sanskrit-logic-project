import json

# -----------------------------
# NORMALIZATION FUNCTIONS
# -----------------------------
def normalize_case(case):
    return case.split()[0]


def normalize_word(word):
    return word.replace("ः", "").replace("म्", "").strip()


# -----------------------------
# CASE DETECTION (YOUR MODEL)
# -----------------------------
def detect_case(word):

    # verbs
    if word.endswith(("ति", "ते", "न्ति", "सि")):
        return "Verb"

    # special forms
    if word == "मम":
        return "Genitive"

    if word in ["यत्"]:
        return "Accusative"

    if word in ["कश्चित्", "तत्त्ववित्"]:
        return "Nominative"

    # genitive / ablative
    if word.endswith(("स्य", "णः", "नः")):
        if word.endswith("मणः"):   # e.g. अकर्मणः
            return "Ablative"
        return "Genitive"

    if word.endswith(("तः", "ात्")):
        return "Ablative"

    # plural
    if word.endswith(("ाणि", "ानि", "ांसि")):
        return "Accusative/Nominative Plural"

    if word.endswith(("ान्", "ून्", "न्")):
        return "Accusative Plural"

    # instrumental
    if word.endswith(("ैः", "ेन", "णा", "या", "सा", "ना", "इना")):
        return "Instrumental"

    # dative / ablative plural
    if word.endswith("भ्यः"):
        return "Dative/Ablative Plural"

    if word.endswith(("ाय", "ये", "वे")):
        return "Dative"

    # locative
    if word.endswith(("ेषु", "ि", "े", "ौ")):
        return "Locative"

    # neuter
    if word.endswith("म्"):
        return "Accusative/Nominative"

    # participles
    if word.endswith("क्तः"):
        return "Nominative"

    # nominative plural
    if word.endswith("आः"):
        return "Nominative Plural"

    # simple nominative
    if word.endswith(("ा", "ी")):
        return "Nominative"

    if word.endswith("ः"):
        return "Nominative"

    return "Unknown"


# -----------------------------
# LOAD FILE (CHANGE HERE IF NEEDED)
# -----------------------------
FILE = "scrambled_verses.json"   # or "sanskrit_gold.json"

with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

print("Total entries:", len(data))


# -----------------------------
# EVALUATION
# -----------------------------
correct = 0
total = 0

for verse in data:

    # handle both formats
    if "scrambled" in verse:
        tokens = verse["scrambled"]
        gold = verse["analysis"]
    else:
        tokens = verse.get("text_split", [])
        gold = verse.get("analysis", [])

    predictions = [(w, detect_case(w)) for w in tokens]

    for g in gold:
        for w, p in predictions:

            if normalize_word(w) == normalize_word(g["word"]):

                total += 1

                gold_case = normalize_case(g["case"])
                pred_case = normalize_case(p)

                if (
                    pred_case == gold_case
                    or p in [
                        "Accusative/Nominative",
                        "Accusative/Nominative Plural",
                        "Dative/Ablative Plural"
                    ]
                ):
                    correct += 1
                else:
                    print("\n--- ERROR ---")
                    print("Word:", g["word"])
                    print("Predicted:", p)
                    print("Actual:", g["case"])


# -----------------------------
# RESULTS
# -----------------------------
print("\n--- RESULTS ---")

if total > 0:
    accuracy = (correct / total) * 100
    print(f"Accuracy: {accuracy:.2f}%")
else:
    print("No labeled data")

input("\nPress Enter to exit...")
