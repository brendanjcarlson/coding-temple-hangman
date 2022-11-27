import requests


class RandomWord:
    def __init__(self):
        self.word = ''
        self.chars = []
        self.url = 'https://api.api-ninjas.com/v1/randomword'
        self.get_word()

    def get_word(self):
        res = requests.get(self.url)
        try:
            if res.ok:
                json = res.json()
                self.word = json["word"].upper()
                self.chars = list(self.word)
                return "Success"
            else:
                raise Exception
        except:
            return "Bad response"

    @property
    def length(self):
        return len(self.chars)
