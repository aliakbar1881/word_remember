"""
read json files
"""
import json
from pathlib import Path


def r_json(path):
    """
    load json file and return python objects
    """
    file = Path(path)
    with open(file) as file_handeler:
        words = json.load(file_handeler)
    return words


if __name__ == "__main__":
    print(r_json('src/word_db/words.json'))
