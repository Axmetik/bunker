import random
import json

with open("bunker.json", "r", encoding="utf-8") as f:
    DATA = json.load(f)

sex = ['Чоловік', 'Жінка']
CAN_HAVE_KIDS = 'Може мати дітей'
CANNOT_HAVE_KIDS = 'Не може мати дітей'
HEALTHY = 'Абсолютно здоровий'

MILD_ILLNESSES = [
    'Алергія на пил',
    'Астма',
    'Псоріаз',
    'Мігрень',
    'Хронічний гастрит',
    'Порушення сну',
    'Сезонна депресія'
]

SERIOUS_ILLNESSES = [
    'Діабет першого типу',
    'Гіпертонія',
    'Виразка шлунка',
    'Епілепсія у ремісії',
    'Хронічний бронхіт',
    'Посттравматичний стресовий розлад',
    'Серцева недостатність',
    'Анемія',
    'Аутоімунне захворювання'
]

class person():
    def __init__(self):
        self.sex = ' '
        self.age = 0
        self.profession = ' '
        self.illness = ' '
        self.invalid = ' '
        self.kids = ' '
        self.phobia = ' '
        self.character = ' '
        self.skill = ' '
        self.religion = ' '
        self.addition = ' '
        self.inventar = ' '
        self.card1 = ' '
        self.card2 = ' '

    def setSkills(self):
        self.skill = random.choice(DATA["skills"])

    def setProfession(self):
        self.profession = random.choice(DATA["profession"])

    def setInvalid(self):
        self.invalid = random.choice(DATA["invalid"])

    def setIllness(self):
        healthy = [illness for illness in DATA["illness"] if illness == HEALTHY]
        mild = [illness for illness in DATA["illness"] if illness in MILD_ILLNESSES]
        serious = [illness for illness in DATA["illness"] if illness in SERIOUS_ILLNESSES]

        if self.age <= 30:
            groups = [healthy, mild, serious]
            weights = [55, 35, 10]
        elif self.age <= 50:
            groups = [healthy, mild, serious]
            weights = [40, 40, 20]
        elif self.age <= 65:
            groups = [healthy, mild, serious]
            weights = [25, 40, 35]
        else:
            groups = [healthy, mild, serious]
            weights = [15, 35, 50]

        illness_group = random.choices(groups, weights=weights, k=1)[0]
        self.illness = random.choice(illness_group or DATA["illness"])

    def setInventar(self):
        self.inventar = random.choice(DATA["inventar"])

    def setAddition(self):
        self.addition = random.choice(DATA["addition"])

    def setReligion(self):
        self.religion = random.choice(DATA["religion"])

    def setCard1(self):
        self.card1 = random.choice(DATA["cards"])

    def setCard2(self):
        self.card2 = random.choice(DATA["cards"])

    def setCharacteristics(self):
        self.character = random.choice(DATA["characteristics"])

    def setPhobias(self):
        self.phobia = random.choice(DATA["phobias"])

    def setAge(self):
        self.age = random.randint(17, 85)

    def setSex(self):
        self.sex = random.choice(sex)

    def setKids(self):
        if self.age <= 35:
            chance = 0.85
        elif self.age <= 50:
            chance = 0.85 - ((self.age - 35) / 15) * 0.25
        else:
            chance = max(0, 0.60 * ((85 - self.age) / 35))

        if self.illness in ['Серцева недостатність', 'Аутоімунне захворювання']:
            chance *= 0.75

        self.kids = CAN_HAVE_KIDS if random.random() < chance else CANNOT_HAVE_KIDS

    def setPerson(self):
        self.setSex()
        self.setAge()
        self.setProfession()
        self.setIllness()
        self.setInvalid()
        self.setKids()
        self.setCharacteristics()
        self.setPhobias()
        self.setSkills()
        self.setAddition()
        self.setInventar()
        self.setCard1()
        self.setCard2()
        self.setReligion()

    def getPerson(self):
        return f"""
🚻Стать: {self.sex}
🎂Вік: {self.age}
🔧Професія: {self.profession}
💟Стан здоров'я: {self.illness}
♿Інвалідність: {self.invalid}
🚼Можливість мати дітей: {self.kids}
☀Характер: {self.character}
🛐Релігія: {self.religion}
🙈Фобія: {self.phobia}
⛳Хобі/вміння: {self.skill}
➕Додаткова інформація: {self.addition}
🎒Багаж: {self.inventar}
🃏Карта дії №1: {self.card1}
🃏Карта дії №2: {self.card2}
        """
