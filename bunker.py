import random
import json

# Завантажуємо JSON лише один раз
with open("bunker.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)

class bunker():
    def __init__(self):
        self.place = ' '
        self.square = ' '
        self.food = ' '

    def setPlace(self):
        self.place = random.choice(DATA["bunker_"])["place"]

    def setSquare(self):
        self.square = random.choice(DATA["bunker_"])["square"]

    def setFood(self):
        self.food = random.choice(DATA["bunker_"])["food"]

    def setBunker(self):
        bunker_data = random.choice(DATA["bunker_"])
        self.place = bunker_data["place"]
        self.square = bunker_data["square"]
        self.food = bunker_data["food"]

    def getBunker(self):
        return f"""
{self.place}
{self.square}
{self.food}
        """
