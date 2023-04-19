import pytest

from src.phone import Phone

@pytest.fixture
def phone_test():
    return Phone("Самсунг", 36000, 2, 2)
def test_phone_init(phone_test):
    assert phone_test.name == 'Самсунг'
    assert phone_test.price == 36000
    assert phone_test.quantity == 2
    assert phone_test.number_of_sim == 2