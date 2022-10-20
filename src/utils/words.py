"""
define generator function that yeild a word in each step
"""
from lxml import html
from string import Template

from requests import Session

from src.utils.IOtmp import r_json


PATH = "//span[@class='def_text']"

def word_generator() -> str:
    """
    generator
    """
    _ = r_json("src/word_db/words.json")
    for i, word in enumerate(_['words'], 1):
        yield word
        _['state'] += 1

def add_new_word(word: str) -> bool:
    """
    add new word to DB
    """
    LINK_TEMP = Template("https://www.britannica.com:443/dictionary/$word")
    with Session() as session:
        with session.get(LINK_TEMP.safe_substitute(word=word)) as response:
            result, defintion = _fetch_definition(response)
    #TODO: add new word and data to DB
    return result

def _fetch_definition(response: str):
    """
    parse html page content
    """
    if response.ok:
        source_code = html.fromstring(response.content)
        tree = source_code.xpath(PATH)
        defintion = tree[0].text
        return True, defintion
    return False, None


if __name__ == "__main__":
    add_new_word('under')
