import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext
from kutuzovtest_data import *
from kutuzovtest_locators import *
import os


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(get_playwright):
    #browser = get_playwright.chromium.launch(headless=False)
    browser = get_playwright.firefox.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def browser_context(browser):
    context = browser.new_context(accept_downloads=True)
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext):
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session", autouse=True)  # чистим от скриншотов
def clean_screenshots_before_tests():
    screenshot_dir = "screenshots"

    # Удаляем все файлы в директории со скриншотами
    if os.path.exists(screenshot_dir):
        for filename in os.listdir(screenshot_dir):
            file_path = os.path.join(screenshot_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")


@pytest.fixture  # проверка открытия страницы отеля
def kutuzov_test_one(page: Page):
    def kutuzov_test_one_func():
        page.goto(data_page)
        page.wait_for_timeout(1000)
        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(1000)
        assert page.inner_text(locator_hotel) == data_hotel
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/kutuzov_1.png")
    return kutuzov_test_one_func


@pytest.fixture  # проверка бронирования номера standart
def kutuzov_test_two(page: Page):
    def kutuzov_test_two_func():
        page.goto(data_page)
        page.click(locator_numbers)
        page.click(locator_standart)
        page.wait_for_timeout(1000)
        page.click(locator_zabronirovat)
        page.wait_for_timeout(1000)
        assert page.url == 'https://kutuzov-art-hotel.ru/rooms/standard-suite/?tl-booking-open=true&room-type=208399'
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/kutuzov_2.png")
        page.wait_for_timeout(1000)
    return kutuzov_test_two_func


@pytest.fixture  # проверка раздела досуг
def kutuzov_test_three(page: Page):
    def kutuzov_test_three_func():
        page.goto(data_page)
        page.click(locator_dosug)
        page.wait_for_timeout(2000)
        assert page.inner_text(locator_dosug_title) == data_dosug_title
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/kutuzov_3.png")
    return kutuzov_test_three_func


@pytest.fixture  # проверка раздела новости
def kutuzov_test_four(page: Page):
    def kutuzov_test_four_func():
        page.goto(data_page)
        page.click(locator_news)
        page.wait_for_timeout(2000)
        assert page.inner_text(locator_news2) == data_news2
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/kutuzov_4.png")
        page.wait_for_timeout(3000)
    return kutuzov_test_four_func


@pytest.fixture  # проверка раздела фотогалерея
def kutuzov_test_five(page: Page):
    def kutuzov_test_five_func():
        page.goto(data_page)
        page.click(locator_fotogalery)
        page.wait_for_timeout(3000)
        page.click(locator_foto1)
        page.wait_for_timeout(2000)
        assert page.inner_text(locator_foto1_big) == data_foto1_big
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/kutuzov_5.png")
        page.wait_for_timeout(1000)
        page.click(locator_foto1_big_close)
        page.wait_for_timeout(3000)
        page.click(locator_foto39)
        page.wait_for_timeout(3000)
        assert page.inner_text(locator_foto39_big) == data_foto39_big
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/kutuzov_5a.png")
        page.wait_for_timeout(3000)
        page.click(locator_foto39_big_close)
    return kutuzov_test_five_func


@pytest.fixture  # проверка раздела контакты
def kutuzov_test_six(page: Page):
    def kutuzov_test_six_func():
        page.goto(data_page)
        page.click(locator_contacts)
        page.wait_for_timeout(3000)
        assert page.inner_text(locator_contacts2) == data_contacts2
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/kutuzov_6.png")
    return kutuzov_test_six_func


@pytest.fixture  # проверка раздела поиск
def kutuzov_test_seven(page: Page):
    def kutuzov_test_seven_func():
        page.goto(data_page)
        page.click(locator_poisk)
        page.wait_for_timeout(2000)
        page.fill(locator_field, str(data_poisk_vvod))
        page.wait_for_timeout(1000)
        page.keyboard.press('Enter')
        page.wait_for_timeout(1000)
        assert page.inner_text(locator_poisk_standart) == data_poisk_standart
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/kutuzov_7.png")
    return kutuzov_test_seven_func


@pytest.fixture  # проверка раздела Что обязательно стоит посетить в Смоленске? Кнопка «вперед»
def kutuzov_test_eight(page: Page):
    def kutuzov_test_eight_func():
        page.goto(data_page)
        page.click(locator_vpered)
        page.wait_for_timeout(1000)
        assert page.inner_text(locator_what_posetit) == data_what_posetit
        page.wait_for_timeout(2000)
        page.mouse.wheel(0, -200)
        page.click(locator_vpered)
        assert page.locator(locator_uspenskysobor).is_visible()
        page.screenshot(path="screenshots/kutuzov_8.png")
    return kutuzov_test_eight_func


@pytest.fixture  # проверка раздела Что обязательно стоит посетить в Смоленске? Кнопка «назад»
def kutuzov_test_nine(page: Page):
    def kutuzov_test_nine_func():
        page.goto(data_page)
        page.click(locator_nazad)
        page.wait_for_timeout(1000)
        assert page.inner_text(locator_what_posetit) == data_what_posetit
        page.mouse.wheel(0, -200)
        page.click(locator_nazad)
        assert page.locator(locator_kurgan).is_visible()
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/kutuzov_9.png")
    return kutuzov_test_nine_func


@pytest.fixture  # проверка раздела увеличить фото
def kutuzov_test_ten(page: Page):
    def kutuzov_test_ten_func():
        page.goto(data_page)
        page.click(locator_uvelichfoto1)
        page.wait_for_timeout(1000)
        assert page.inner_text(locator_uvelichfoto1_big) == data_uvelichfoto1_big
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/kutuzov_10.png")
        page.wait_for_timeout(1000)
        page.click(locator_uvelichfoto1_big_close)
        page.wait_for_timeout(1000)
        page.click(locator_uvelichfoto4)
        page.wait_for_timeout(1000)
        assert page.inner_text(locator_uvelichfoto4_big) == data_uvelichfoto4_big
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/kutuzov_10a.png")
        page.wait_for_timeout(1000)
        page.click(locator_uvelichfoto4_big_close)
    return kutuzov_test_ten_func


@pytest.fixture  # проверка раздела кнопка домой
def kutuzov_test_eleven(page: Page):
    def kutuzov_test_eleven_func():
        page.goto(data_page)
        page.click(locator_news)
        page.wait_for_timeout(2000)
        page.screenshot(path="screenshots/kutuzov_11.png")
        page.wait_for_timeout(1000)
        assert page.inner_text(locator_news2) == data_news2
        page.wait_for_timeout(1000)
        page.click(locator_home)
        page.wait_for_timeout(3000)
        page.screenshot(path="screenshots/kutuzov_11a.png")
        page.wait_for_timeout(1000)
        assert page.inner_text(locator_hotel) == data_hotel
        page.wait_for_timeout(2000)
    return kutuzov_test_eleven_func


@pytest.fixture  # проверка раздела выбор фото на главную страницу
def kutuzov_test_twelve(page: Page):
    def kutuzov_test_twelve_func():
        page.goto(data_page)
        page.click(locator_button_big_foto1)
        page.wait_for_timeout(1000)
        assert page.locator(locator_big_foto1).is_visible()
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/kutuzov_12.png")
        page.click(locator_button_big_foto4)
        page.wait_for_timeout(1000)
        assert page.locator(locator_big_foto4)
        page.wait_for_timeout(1000)
        page.screenshot(path="screenshots/kutuzov_12a.png")
    return kutuzov_test_twelve_func
