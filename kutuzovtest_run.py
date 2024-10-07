import pytest

from kutuzovtest_step import *


@pytest.mark.smoke  # проверка открытия страницы
def test_one(page: Page, kutuzov_test_one):
    kutuzov_test_one()


@pytest.mark.smoke  # проверка бронирования номера
def test_two(page: Page, kutuzov_test_two):
    kutuzov_test_two()


@pytest.mark.smoke   # проверка раздела досуг
def test_three(page: Page, kutuzov_test_three):
    kutuzov_test_three()


@pytest.mark.smoke  # проверка раздела новости
def test_four(page: Page, kutuzov_test_four):
    kutuzov_test_four()


@pytest.mark.smoke  # проверка раздела фотогалерея
def test_five(page: Page, kutuzov_test_five):
    kutuzov_test_five()


@pytest.mark.smoke    # проверка раздела контакты
def test_six(page: Page, kutuzov_test_six):
    kutuzov_test_six()


@pytest.mark.smoce  # проверка раздела поиск
def test_seven(page: Page, kutuzov_test_seven):
    kutuzov_test_seven()


@pytest.mark.smoke  # проверка раздела Что обязательно стоит посетить в Смоленске? Кнопка «вперед»
def test_eight(page: Page, kutuzov_test_eight):
    kutuzov_test_eight()


@pytest.mark.smoke  # проверка раздела Что обязательно стоит посетить в Смоленске? Кнопка «назад»
def test_nine(page: Page, kutuzov_test_nine):
    kutuzov_test_nine()


@pytest.mark.smoke  # проверка раздела увеличить фото
def test_ten(page: Page, kutuzov_test_ten):
    kutuzov_test_ten()


@pytest.mark.smoke  # проверка раздела кнопка домой
def test_eleven(page: Page, kutuzov_test_eleven):
    kutuzov_test_eleven()


@pytest.mark.smoke  # проверка раздела выбор фото на главную страницу
def test_twelve(page: Page, kutuzov_test_twelve):
    kutuzov_test_twelve()
