import pytest

""""Папки и файлы начинать со слова test lдля работы с Pytest"""
""""Для наглядности"""


@pytest.fixture
def set_up():
    print("Вход в систему выполнен")

def test_sending_mail_1(set_up):
    print("Письмо отправлено")

def test_sending_mail_2(set_up):
    print("Письмо отправлено")