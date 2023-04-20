from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim <= 0:
            raise ValueError("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.number_of_sim = number_of_sim
    @property
    def number_of_sim(self):
        return self._number_of_sim
    @number_of_sim.setter
    def number_of_sim(self, value):
        if value <= 0:
            raise ValueError("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._number_of_sim = value
    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"