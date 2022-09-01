from src.utils.IO import r_json

def words():
    words = r_json('src/word_db/words.json')
    return words
