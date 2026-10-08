import random
import json

# Завантаження JSON один раз
with open("bunker.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)

class story:
    def __init__(self):
        self.story_ = " "

    def getStory(self):
        # Обираємо випадковий об’єкт з масиву story
        item = random.choice(DATA["story"])
        self.story_ = item
        return self.story_
