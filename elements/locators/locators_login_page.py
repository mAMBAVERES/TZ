from selenium.webdriver.common.by import By


class Login:

    EMAIL = (By.XPATH, '//*[@id="email"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    BUTTON = (By.XPATH, '//*[@class="btn btn-primary"]')
    EXIT_PROFILE = (By.XPATH, '//*[@title="Выйти"]')
