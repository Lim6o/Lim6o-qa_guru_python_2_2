import pytest
from selene.support.shared import browser

# Устанавливаем размер окна
@pytest.fixture(autouse=True)
def size_window():
    browser.config.window_height = 1900
    browser.config.window_width = 1200

# Открываем браузер
@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
    print("Браузер открыт")
    yield
    print("Тест проведен")