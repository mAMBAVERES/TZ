from .page import Page
from elements.locators.locators_device_page import Device

class DevicePage(Page, Device):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url

    def step_tz(self,sections):
        sek = self.section_constructor(sections)
        self.find_element(sek).click()
        self.find_element(self.BUTTON_SWITCH_TABLE).click()
        self.element_clickable(self.CLOSE_FORM).click()

    def check_close_form(self):
        n = 2
        while n > 0:
            check = self.is_element_not_visible(self.CHECK_CLOSE_FORM)
            if check:
                return check
            n -= 1  # Уменьшаем n на 1
        return False






