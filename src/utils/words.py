"""
define generator function that yeild a word in each step
"""
from requests import Session
from src.utils.IOtmp import r_json


def word_generator():
    """
    generator
    """
    _ = r_json("src/word_db/words.json")
    for i, word in enumerate(_['words'], 1):
        yield word
        _['state'] += 1

def add_new_word(word: str):
    """
    add new word to DB
    """
    #TODO: fetch words data from web
    #TODO: add new word and data to DB
    return True


if __name__ == "__main__":
    word = word_generator()
    next(word)
    next(word)
