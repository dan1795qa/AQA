import pytest


@pytest.mark.order(2)
def test_method_1():
    print("Метод 1")

@pytest.mark.order(5)
def test_method_2():
    print("Метод 2")

@pytest.mark.order(4)
def test_method_3():
    print("Метод 3")

@pytest.mark.order(3)
def test_method_4():
    print("Метод 4")

@pytest.mark.order(1)
def test_method_5():
    print("Метод 5")

@pytest.mark.order(6)
def test_method_6():
    print("Метод 6")
