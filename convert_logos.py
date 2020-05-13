import json

logos = {
    "travel": "⛱",
    "study": "\uD83C\uDFEB",
    "work": "\uD83C\uDFE2",
    "relocate": "\uD83D\uDE9C",
    "coding": "✌"
}

with open("logos.json", "w", encoding="utf-8") as f:
   json.dump(logos, f, indent=4, ensure_ascii=True)
