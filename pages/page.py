from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from selenium.common.exceptions import NoSuchElementException


class Page(object):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url
        self.wait = WebDriverWait(driver, 10)

    def is_element_not_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return not element.is_displayed()  # Возвращает True, если элемент не виден
        except NoSuchElementException:
            return True  # Если элемент не найден, он считается невидимым

    def is_element_visible(self, locator):
        """
        Проверяет, виден ли элемент на странице.

        Аргументы:
            locator (tuple): Локатор, используемый для поиска элемента.

        Возвращает:
            bool: True, если элемент виден, иначе False.

        Исключения:
            WebDriverException: Если произошла ошибка при ожидании видимости элемента.
        """
        try:
            self.wait.until(visibility_of_element_located(locator))
            return True
        except WebDriverException:
            return False

    def is_elements_visible(self, locators):
        """
        Проверяет, видны ли все элементы на странице.

        Аргументы:
            locators (list): Список локаторов, используемых для поиска элементов.

        Возвращает:
            bool: True, если все элементы видны, иначе False.

        Исключения:
            WebDriverException: Если произошла ошибка при ожидании видимости всех элементов.
        """
        try:
            self.wait.until(visibility_of_all_elements_located(locators))
            return True
        except WebDriverException:
            return False

    def screenshot(self, title: str):
        """
        Делает скриншот текущего окна браузера и прикрепляет его к отчету.

        Аргументы:
            title (str): Название для скриншота, которое будет использовано в отчете.
        """
        attach(self.driver.get_screenshot_as_png(), name=title, attachment_type=AttachmentType.PNG)

    def scroll_down(self):
        """
        Прокручивает страницу вниз до конца.
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def switch_to_last_tab(self):
        """
        Переключается на последнюю открытую вкладку в браузере.
        """
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_tab(self):
        """
        Закрывает текущую вкладку и переключается на первую открытую вкладку.
        """
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def wait_element(self, locator):
        """
        Ожидает появления элемента на странице в течение 60 секунд.

        Аргументы:
            locator (tuple): Локатор, используемый для поиска элемента.
        """
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))

    def refresh_browser(self):
        """
        Обновляет текущую страницу браузера.
        """
        self.driver.refresh()

    def check_status_code_url(self, url):
        """
        Проверяет, что запрашиваемый URL возвращает статус-код 200 (OK).

        Аргументы:
            url (str): URL, который необходимо проверить.

        Исключения:
            AssertionError: Если статус-код ответа не равен 200.
        """
        status = requests.get(url)
        assert status.status_code == 200

    def mouse_over_element(self, element):
        """
        Наводит курсор мыши на переданный элемент с использованием ActionChains.

        Аргументы:
            element (WebElement): Элемент, на который необходимо навести курсор.
        """
        hover = ActionChains(self.driver).move_to_element(element).perform()

    def find_element(self, locator, time=60):
        """
        Ищет элемент на странице по заданному локатору в течение указанного времени ожидания.

        Аргументы:
            locator (tuple): Локатор, используемый для поиска элемента.
            time (int, необязательный): Время ожидания в секундах (по умолчанию 10).

        Возвращает:
            WebElement: Найденный элемент.

        Исключения:
            TimeoutException: Если элемент не найден в течение указанного времени.
        """
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)
        return WebDriverWait(self.driver, timeout=time, poll_frequency=1, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        """
        Ищет все элементы на странице, соответствующие заданному локатору.

        Аргументы:
            locator (tuple): Локатор, используемый для поиска элементов.
            time (int, необязательный): Время ожидания в секундах (по умолчанию 10).

        Возвращает:
            list: Список найденных элементов.

        Исключения:
            TimeoutException: Если элементы не найдены в течение указанного времени.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def element_clickable(self, locator, time=60):
        """
        Ожидает, что элемент станет кликабельным, в течение указанного времени.

        Аргументы:
            locator (tuple): Локатор, используемый для поиска кликабельного элемента.
            time (int, необязательный): Время ожидания в секундах (по умолчанию 60).

        Возвращает:
            WebElement: Кликабельный элемент.

        Исключения:
            TimeoutException: Если элемент не стал кликабельным в течение указанного времени.
        """
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)
        return WebDriverWait(self.driver, time, poll_frequency=1, ignored_exceptions=ignored_exceptions).until(
            EC.element_to_be_clickable(locator),
            message=f"Can't find clickable element by locator {locator}"
        )
