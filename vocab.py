import requests
import random


def get_word():
    file_path = "./words_list.txt"
    try:
        with open(file_path, "r") as file:
            words = file.readlines()
            random_word = random.choice(words).strip()
            return random_word
    except FileNotFoundError:
        print("Word Lists File not found.")
    except Exception as e:
        print("An error occurred ;-; ", e)


def get_meaning(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            definition_arr = data[0]['meanings'][0]['definitions']

            definition_1 = definition_arr[0]["definition"]

            example_1 = definition_arr[0]["example"] if "example" in definition_arr[0] else None

            definition_2 = definition_arr[1]["definition"] if len(
                definition_arr) > 1 else None

            example_2 = definition_arr[1]["example"] if len(
                definition_arr) > 1 and "example" in definition_arr[1] else None

            synonyms = data[0]['meanings'][0]["synonyms"]

            meaningResponse = f'Definition 1:\t{definition_1}\nExample:\t{example_1}\n\nDefinition 2:\t{definition_2}\nExample:\t{example_2}\n\nSynonyms:\t{synonyms}'

            return meaningResponse
        else:
            return "Something went wrong ;-;"
    else:
        print(
            f"Error: Unable to fetch data. Status code: {response.status_code}")
        return "Something went wrong ;-;"
