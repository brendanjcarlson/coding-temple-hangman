import requests


class RandomWord:
    def __init__(self):
        self.word = ''
        self.chars = []
        self.url = 'https://api.api-ninjas.com/v1/randomword'
        self.get()

    def get(self):
        res = requests.get(self.url)
        try:
            if res.ok:
                json = res.json()
                self.word = json["word"].upper()
                self.chars = list(self.word)
        except requests.exceptions:
            return "Unable to get word."

    @property
    def length(self):
        return len(self.chars)
