class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{} Typing={} Reflection={} Year={}".format(self.name, self.is_dynamic, self.reflection, self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"
