CURRENT_YEAR = 2019


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        print("{} ({}): ${:.2f}".format(self.name, self.year, self.cost))

    def get_age(self):
        guitar_year = self.year
        guitar_age = CURRENT_YEAR - guitar_year
        return guitar_age

    def is_vintage(self, guitar_age):
        if guitar_age >= 50:
            return True
        else:
            return False
