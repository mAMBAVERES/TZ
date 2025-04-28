from selenium.webdriver.common.by import By

class Device:


    CHECK_CLOSE_FORM = (By.XPATH, '//*[@class="modal fade device-table-column-switcher show"]')
    CLOSE_FORM = (By.XPATH, "/html/body/main/div[3]/div[1]/div[1]/div/div/div[1]/button/span")
    BUTTON_SWITCH_TABLE = (By.XPATH, "//*[@class='btn btn-sm btn-secondary mr-3']")

    def section_constructor(self, section):
        xpath = f"//*[text()='{section}']"
        return (By.XPATH, xpath)
