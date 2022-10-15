"""
read json word file with CustomDecoder
"""
import json

from src.utils.exception import NonValidState


class CustomDecoder(json.JSONDecoder):
    """
    add some condition on loaded words
    """
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(
            self,
            object_hook=self.object_hook,
            *args,
            **kwargs
        )

    def object_hook(self, obj):
        if 'state' in obj:
            if not isinstance(obj['state'], int):
                raise NonValidState("update your state ")
        elif 'word' in obj:
            print(obj)
            return dict(
                word=obj['word'],
                definition=obj['definition']
            )
        else:
            raise ValueError('Some value in your json file not valid')



def r_json(path: str) -> list:
    """
    loading data
    """
    with open(path, encoding='utf-8') as f_words:
        words = json.load(f_words, cls=CustomDecoder)
    return words


if __name__ == "__main__":
    result = r_json('src/word_db/words.json')
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(result)
