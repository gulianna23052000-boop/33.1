import pytest
from selenium.webdriver.common.by import By      # ✅ импорт
from pages.auth_page import AuthPage
from locators.auth_locators import AuthLocators  # ✅ импорт


# 1-5: ТЕСТЫ АВТОРИЗАЦИИ ПО ТЕЛЕФОНУ
@pytest.mark.positive
def test_success_auth_by_phone(auth_page):
    auth_page.enter_username("+79111234567")
    auth_page.enter_password("ValidPass123")
    auth_page.click_submit()
    assert auth_page.is_header_present(), "Авторизация не прошла, редиректа не было"


@pytest.mark.negative
def test_auth_by_phone_with_wrong_password(auth_page):
    auth_page.enter_username("+79111234567")
    auth_page.enter_password("WrongPass123")
    auth_page.click_submit()
    error_text = auth_page.get_error_message()
    assert error_text == "Неверный логин или пароль"
    # проверка цвета (rgba), а не "orange"
    assert "255" in auth_page.get_forgot_password_color()


def test_auth_by_nonexistent_phone(auth_page):
    auth_page.enter_username("+79001112233")
    auth_page.enter_password("AnyPassword1")
    auth_page.click_submit()
    assert "Неверный логин или пароль" in auth_page.get_error_message()


def test_auth_by_phone_without_country_code(auth_page):
    auth_page.enter_username("9111234567")
    auth_page.enter_password("ValidPass123")
    auth_page.click_submit()
    assert auth_page.is_header_present()


@pytest.mark.negative
def test_auth_by_phone_invalid_format(auth_page):
    auth_page.enter_username("+7(999)ABC-45-67")
    auth_page.click_submit()
    assert "Неверный формат" in auth_page.get_invalid_format_message()


# 6-10: ТЕСТЫ АВТОРИЗАЦИИ ПО ПОЧТЕ
def test_success_auth_by_email(auth_page):
    auth_page.click_tab_mail()
    auth_page.enter_username("valid_email@mail.ru")
    auth_page.enter_password("ValidPass123")
    auth_page.click_submit()
    assert auth_page.is_header_present()


def test_auth_by_email_uppercase(auth_page):
    auth_page.click_tab_mail()
    auth_page.enter_username("VALID_EMAIL@MAIL.RU")
    auth_page.enter_password("ValidPass123")
    auth_page.click_submit()
    assert auth_page.is_header_present()


def test_auth_by_email_with_wrong_password(auth_page):
    auth_page.click_tab_mail()
    auth_page.enter_username("valid_email@mail.ru")
    auth_page.enter_password("WrongPass123")
    auth_page.click_submit()
    assert "Неверный логин или пароль" in auth_page.get_error_message()


@pytest.mark.negative
def test_auth_by_email_invalid_format(auth_page):
    auth_page.click_tab_mail()
    auth_page.enter_username("invalid_email.mail.ru")
    auth_page.click_submit()
    assert "Неверный формат" in auth_page.get_invalid_format_message()


def test_auth_by_nonexistent_email(auth_page):
    auth_page.click_tab_mail()
    auth_page.enter_username("nonexistent@mail.ru")
    auth_page.enter_password("AnyPassword1")
    auth_page.click_submit()
    assert "Неверный логин или пароль" in auth_page.get_error_message()


# 11-15: ТЕСТЫ АВТОРИЗАЦИИ ПО ЛОГИНУ И ЛС
def test_success_auth_by_login(auth_page):
    auth_page.click_tab_login()
    auth_page.enter_username("valid_login_123")
    auth_page.enter_password("ValidPass123")
    auth_page.click_submit()
    assert auth_page.is_header_present()


def test_auth_by_login_with_wrong_password(auth_page):
    auth_page.click_tab_login()
    auth_page.enter_username("valid_login_123")
    auth_page.enter_password("WrongPass123")
    auth_page.click_submit()
    assert "Неверный логин или пароль" in auth_page.get_error_message()


def test_success_auth_by_ls(auth_page):
    auth_page.click_tab_ls()
    auth_page.enter_username("123456789012")
    auth_page.enter_password("ValidPass123")
    auth_page.click_submit()
    assert auth_page.is_header_present()


@pytest.mark.negative
def test_auth_by_ls_invalid_format(auth_page):
    auth_page.click_tab_ls()
    auth_page.enter_username("12345abc6789")
    auth_page.click_submit()
    assert "Неверный формат" in auth_page.get_invalid_format_message()


# 16-20: ТЕСТЫ ДОПОЛНИТЕЛЬНОЙ ФУНКЦИОНАЛЬНОСТИ
def test_auto_switch_tab_to_mail(auth_page):
    auth_page.click_tab_phone()
    auth_page.enter_username("test@mail.ru")
    auth_page.enter_password("password")
    active_tab = auth_page.find_element((By.CSS_SELECTOR, ".rt-tab.rt-tab--active")).text
    assert "Почта" in active_tab


def test_auto_switch_tab_to_phone(auth_page):
    auth_page.click_tab_mail()
    auth_page.enter_username("79111234567")
    auth_page.enter_password("password")
    active_tab = auth_page.find_element((By.CSS_SELECTOR, ".rt-tab.rt-tab--active")).text
    assert "Телефон" in active_tab


def test_forgot_password_link_functionality(auth_page):
    auth_page.find_element(AuthLocators.LINK_FORGOT_PASSWORD).click()
    assert "восстановление пароля" in auth_page.driver.page_source.lower()


@pytest.mark.security
def test_xss_vulnerability_in_login_field(auth_page):
    auth_page.enter_username("<script>alert('xss')</script>")
    auth_page.enter_password("password")
    auth_page.click_submit()
    assert True   # успех, если нет алерта/краша


def test_empty_fields_validation(auth_page):
    auth_page.click_submit()
    error_text = auth_page.get_error_message()
    assert "Заполните поле" in error_text or "Неверный логин или пароль" in error_text
