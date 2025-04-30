import allure
import pytest

import elements.locators.locators_device_page
from tests.data.constance import LOGIN, PASSWORD
from elements.locators.locators_device_page import Device

class TestDevice:
    """

    Ввиду того что небыло задачи писать тесты для авторизации проверка успешной авторизации будут указанны тут

    """
    @allure.feature('авторизации и переключение между разделами')
    @allure.story('Сценарий 1: Проверка авторизации переход к разделу устройств и проверка переключения таблицы')
    def test_check_autotest(self, app):
        with allure.step("Авторизация пользователя"):

            app.LoginPage.autorization_or_email(login=LOGIN, password=PASSWORD)
            app.LoginPage.click_button_autorization()
            # Проверка успешной авторизации
        with allure.step("Проверка  авторизации"):
            app.LoginPage.is_authorized()
            assert app.LoginPage.is_authorized(), "Не удачная авторизация"

        with allure.step("переход к разделу устройств и открытие таблицы"):
            app.DevicePage.step_tz(sections='Устройства')

        with allure.step("проверка что таблица закрылась"):
            assert app.DevicePage.check_invisible_element() , f'таблица все еще отображается на странице'

        with allure.step("переход к выгрузки файла"):
            Button = elements.locators.locators_device_page.Device.EXPORT_RESULTS
            popup = elements.locators.locators_device_page.Device.POPUP
            app.DevicePage.click_element(element=Button)
            assert app.DevicePage.check_visible_element(element=popup), f"Попап не отображается"










