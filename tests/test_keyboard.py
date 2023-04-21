import pytest

from src.keyboard import Keyboard

@pytest.fixture
def keyboard_test():
    return Keyboard("Клавиатура", 8400, 3)
def test_keyboard_init(keyboard_test):
    assert keyboard_test.name == 'Клавиатура'
    assert keyboard_test.price == 8400
    assert keyboard_test.quantity == 3
    assert keyboard_test.language == 'EN'