"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def item_cover():
    return Item("Чехол", 100, 10)

def test_item_init(item_cover):
    assert item_cover.price == 100
    assert item_cover.quantity == 10

def test_item_total(item_cover):
    assert item_cover.calculate_total_price() == 1000

def test_apply_discount(item_cover):
    Item.pay_rate = 0.5
    item_cover.apply_discount()
    assert item_cover.price == 50


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/test_items.csv')
    assert Item.all[-1].name == 'Подставка'
    assert Item.all[-2].price == 2
    assert Item.all[-2].name == 'Сумка'

def test_name_setter(item_cover):
    item_cover.name = 'Alice'
    assert item_cover.name == 'Alice'
    with pytest.raises(Exception):
        item_cover.name = 'ThisNameIsTooLong'

def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('11.789') == 11
    assert Item.string_to_number('ten') == 'Некорректный формат'