from pages.base_page import BasePage
from locators.auth_locators import AuthLocators


class AuthPage(BasePage):

    def enter_username(self, username):
        field = self.find_element(AuthLocators.INPUT_USERNAME)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.find_element(AuthLocators.INPUT_PASSWORD)
        field.clear()
        field.send_keys(password)

    def click_submit(self):
        self.find_element(AuthLocators.BUTTON_SUBMIT).click()

    def click_tab_phone(self):
        self.find_element(AuthLocators.TAB_PHONE).click()

    def click_tab_mail(self):
        self.find_element(AuthLocators.TAB_MAIL).click()

    def click_tab_login(self):
        self.find_element(AuthLocators.TAB_LOGIN).click()

    def click_tab_ls(self):
        self.find_element(AuthLocators.TAB_LS).click()

    def get_error_message(self):
        return self.find_element(AuthLocators.ERROR_MESSAGE).text

    def get_invalid_format_message(self):
        return self.find_element(AuthLocators.ERROR_INVALID_USERNAME).text

    def get_forgot_password_color(self):
        return self.find_element(
            AuthLocators.LINK_FORGOT_PASSWORD
        ).value_of_css_property("color")

    def is_header_present(self):
        try:
            return len(self.find_elements(AuthLocators.HEADER)) > 0
        except:
            return False
