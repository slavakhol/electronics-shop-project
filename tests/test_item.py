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