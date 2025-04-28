from .page import Page
from time import sleep
from elements.locators.locators_login_page import Login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage(Page, Login):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url
        self.wait = WebDriverWait(driver, 10)

    def autorization_or_email(self, login, password):
        input_email = self.find_element(self.EMAIL)
        input_email.clear()
        input_email.send_keys(login)
        input_password = self.find_element(self.PASSWORD)
        input_password.clear()
        input_password.send_keys(password)

    def click_button_autorization(self):
        self.find_element(self.BUTTON).click()


    def is_authorized(self):
        vizibility = self.is_element_visible(self.EXIT_PROFILE)
        return vizibility



