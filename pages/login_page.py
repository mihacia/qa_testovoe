from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL_INPUT = "input[type='email']"

    PASSWORD_INPUT = "input[type='password']"

    def is_email_field_visible(self):
        email = self.page.locator(self.EMAIL_INPUT)
        email.wait_for(timeout=15000)
        return email.is_visible()

    def is_password_field_visible(self):
        password = self.page.locator(self.PASSWORD_INPUT)
        password.wait_for(timeout=15000)
        return password.is_visible()