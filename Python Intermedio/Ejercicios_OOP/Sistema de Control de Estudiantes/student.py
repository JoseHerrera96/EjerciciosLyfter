class student:

    def __init__(self, name, section, spanish, english, history, science):
        self.__name = name
        self.__section = section
        self.__spanish = spanish
        self.__english = english
        self.__history = history
        self.__science = science
        self.__average_score = self.get_average_score()
    
    @property
    def name(self):
        return self.__name
    
    @property
    def section(self):
        return self.__section
    
    @property
    def spanish(self):
        return self.__spanish
    
    @property
    def english(self):
        return self.__english
    
    @property
    def history(self):
        return self.__history
    
    @property
    def science(self):
        return self.__science
    
    @property
    def average_score(self):
        return self.__average_score
    
    def __str__(self):
        return f"name: {self.__name} ({self.__section}): {self.__spanish}, {self.__english}, {self.__history}, {self.__science}, {self.__average_score:.2f}"
    
    def get_average_score(self):
        return (self.__spanish + self.__english + self.__history + self.__science) / 4
    
    def get_attributes(self):
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "history": self.history,
            "science": self.science,
            "average_score": self.average_score
        }
