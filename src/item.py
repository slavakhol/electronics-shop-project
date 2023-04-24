import csv



class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    file = '../src/items.csv'

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return  self.name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 11:
            self.__name = value
        else:
            raise Exception("Имя больше 10 символов")

    @classmethod
    def instantiate_from_csv(cls):

        try:
            with open(Item.file, 'r', encoding='cp1251') as csv_file:
                reader = csv.DictReader(csv_file)
                next(reader)
                expected_cols = ['name', 'price', 'quantity']
                if reader.fieldnames == expected_cols:
                    for row in reader:
                        Item(row['name'], float(row['price']), int(row['quantity']))
                else:
                    raise InstantiateCSVError
        except InstantiateCSVError:
            print("Файл items.csv поврежден")

        except FileNotFoundError:
            print("Отсутствует файл items.csv")



    @staticmethod
    def string_to_number(string):
        try:
            return int(float(string))
        except ValueError:
            return "Некорректный формат"
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

class InstantiateCSVError(Exception):
    pass