from src.utils.IO import r_json

def words(num):
    words = []
    _ = r_json("src/word_db/words.json")
    state = _['state']
    for i, word in enumerate(_['words'], 1):
        print(i, word, sep=" = = ")
        words.append(word)
        if i == (state + num):
            return words

if __name__ == "__main__":
    words()
