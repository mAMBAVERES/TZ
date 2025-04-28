from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from pages.device_page import DevicePage


class Application(object):

    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.LoginPage = LoginPage(driver, base_url)
        self.DevicePage = DevicePage(driver, base_url)