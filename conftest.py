import pytest
import allure
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from models.application import Application





@pytest.fixture(scope="function", autouse=True)
def app(request):
    """
    Фикстура для инициализации и управления экземпляром браузера Chrome на локальной машине.
    Используется для автоматизированного тестирования AMS сервера.
    Параметры:
        request (FixtureRequest): Стандартный объект pytest, предоставляющий информацию о текущем тесте.
    Возвращает:
        Application: Объект приложения, связанный с текущим экземпляром веб-драйвера.
    Завершение:
        Закрывает браузер после выполнения теста.
    """
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    allure.step("создание экзепляра класса драйвера и запуск браузера")

    @allure.step("Завершение теста")
    def fin():
        try:
            driver.quit()
            allure.step("Браузер успешно закрыт")
        except InvalidSessionIdException:
            print("Session has already ended or is invalid")
            allure.step("Не удалось закрыть браузер: сессия недействительна")

    request.addfinalizer(fin)
    return Application(driver=driver, base_url='https://stage-mgt.antisleep.ru/')



