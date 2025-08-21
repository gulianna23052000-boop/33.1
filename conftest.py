import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.auth_page import AuthPage   # ✅ добавлен импорт

@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def auth_page(browser):
    page = AuthPage(browser)
    page.go_to_site("https://b2c.passport.rt.ru")
    return page
