import pandas as pd
import json

data = pd.read_csv("netflix_titles.tsv", delimiter = "\t")

selected_information = data[["PRIMARYTITLE", "DIRECTOR", "CAST", "GENRES", "STARTYEAR"]]
selected_information.rename(columns={"PRIMARYTITLE": "title", "DIRECTOR": "directors", "CAST": "cast", "GENRES": "genres", "STARTYEAR": "decade"}, inplace=True)

selected_information[["directors", "cast", "genres"]] = selected_information[["directors", "cast", "genres"]].fillna("")

def splitting_into_list(value):
    individual_items = []
    if value != "":
        for item in value.split(","):
            individual_items.append(item.strip())
    return individual_items

selected_information["directors"] = selected_information["directors"].apply(splitting_into_list)
selected_information["cast"] = selected_information["cast"].apply(splitting_into_list)
selected_information["genres"] = selected_information["genres"].apply(splitting_into_list)

def change_to_decade(year):
    return year - (year % 10)

selected_information["decade"] = selected_information["decade"].apply(change_to_decade)

selected_information_list = selected_information.to_dict(orient='records')

with open("hw02_output.json", "w", encoding="utf-8") as json_file:
    json.dump(selected_information_list, json_file, indent=4, ensure_ascii=False)

