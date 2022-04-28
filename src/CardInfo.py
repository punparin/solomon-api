import json

class CardInfo:
    def __init__(self, url):
        self.cards = []
        self.url = url

    def add_card(self, card):
        self.cards.append(card)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
