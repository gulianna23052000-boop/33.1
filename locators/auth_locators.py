from selenium.webdriver.common.by import By

class AuthLocators:
    # Табы выбора типа аутентификации
    TAB_PHONE = (By.ID, 't-btn-tab-phone')
    TAB_MAIL = (By.ID, 't-btn-tab-mail')
    TAB_LOGIN = (By.ID, 't-btn-tab-login')
    TAB_LS = (By.ID, 't-btn-tab-ls')

    # Поля ввода
    INPUT_USERNAME = (By.ID, 'username')  # Универсальное поле для всех табов
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_SUBMIT = (By.ID, 'kc-login')

    # Сообщения об ошибках
    ERROR_MESSAGE = (By.ID, 'form-error-message')
    ERROR_INVALID_USERNAME = (By.XPATH, "//span[contains(text(), 'Неверный формат')]")

    # Ссылка "Забыл пароль"
    LINK_FORGOT_PASSWORD = (By.ID, 'forgot_password')

    # Продуктовый слоган (для проверки успешного редиректа)
    HEADER = (By.TAG_NAME, 'h1')