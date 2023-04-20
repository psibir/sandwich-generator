import csv
import random


class Sandwich:
    def __init__(self):
        self.cheeses = []
        self.meats = []
        self.vegetables = []
        self.condiments = []

    def add_cheese(self, cheese):
        if len(self.cheeses) < 2:
            self.cheeses.append(cheese)
        else:
            print("You can't add more than two cheeses.")

    def add_meat(self, meat):
        if len(self.meats) < 2:
            self.meats.append(meat)
        else:
            print("You can't add more than two meats.")

    def add_vegetable(self, vegetable):
        if len(self.vegetables) < 2:
            self.vegetables.append(vegetable)
        else:
            print("You can't add more than two vegetables.")

    def add_condiment(self, condiment):
        if len(self.condiments) < 1:
            self.condiments.append(condiment)
        else:
            print("You can't add more than one condiment.")

    def generate_sandwich(self):
        with open('ingredients.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            ingredients = list(reader)

            cheeses = [row[0] for row in ingredients if row[0] not in self.cheeses]
            meats = [row[1] for row in ingredients if row[1] not in self.meats]
            vegetables = [row[2] for row in ingredients if row[2] not in self.vegetables]
            condiments = [row[3] for row in ingredients if row[3] not in self.condiments]

        # Randomly select two cheeses or one cheese
        if random.choice([True, False]):
            max_cheeses = 2
        else:
            max_cheeses = 1

        self._add_items_to_sandwich(cheeses, self.add_cheese, max_cheeses)
        self._add_items_to_sandwich(meats, self.add_meat, 2)
        self._add_items_to_sandwich(vegetables, self.add_vegetable, 2)
        self._add_items_to_sandwich(condiments, self.add_condiment, 1)

        ingredients = filter(None, self.cheeses + self.meats + self.vegetables + self.condiments)
        print(', '.join(ingredients))

    def _add_items_to_sandwich(self, items, add_func, max_items):
        for item in random.sample(items, min(len(items), max_items)):
            add_func(item)


if __name__ == '__main__':
    sandwich = Sandwich()
    sandwich.generate_sandwich()
