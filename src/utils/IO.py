import json

class CustomDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if obj is not None:
            return obj

def r_json(path: str) -> dict:
    with open(path) as f:
        words = json.load(f, cls=CustomDecoder)
        return words

if __name__ == "__main__":
    result = r_json('src/word_db/words.json')
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(result)
