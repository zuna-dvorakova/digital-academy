import json

character_count = {}

with open("alice.txt", encoding="utf-8") as file:
    for line in file:
        for character in line:
            character = character.lower()
            if character not in [' ', '\n']:
                if character in character_count:
                    character_count[character] += 1
                else:
                    character_count[character] = 1

with open("hw01_output", "w", encoding="utf-8") as json_file:
    json.dump(character_count, json_file, indent=4, ensure_ascii=False, sort_keys=True)

    