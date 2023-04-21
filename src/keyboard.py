from src.item import Item


class LanguageChange:

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language
    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self


class Keyboard(Item, LanguageChange):
    pass

