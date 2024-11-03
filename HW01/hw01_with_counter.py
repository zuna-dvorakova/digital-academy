import json
from collections import Counter

character_count = {}

with open("alice.txt", encoding="utf-8") as file:
    character_count = Counter(file.read().lower())

for char in (" ", "\n"):
    del character_count[char]

with open("hw01_output.json", "w", encoding="utf-8") as json_file:
    json.dump(character_count, json_file, indent=4, ensure_ascii=False, sort_keys=True)