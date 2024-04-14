import allure
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import TestsData as td


class TestTransfers:

    @allure.title('Тестируем переход на главную страницу по клику на логотип Самокат')
    def test_successful_transition_to_main_page_by_samokat_logo_click(self, firefox_driver):
        order_page = OrderPage(firefox_driver)
        order_page.driver.get(td.urls['order_page'])
        order_page.click_on_samokat_logo()
        assert WebDriverWait(firefox_driver, 30).until(EC.url_to_be(td.urls['home_page']))

    @allure.title('Переход на Дзен по клику на логотип Яндекс')
    def test_successful_transition_to_dzen_page_by_yandex_logo_click(self, firefox_driver):
        order_page = OrderPage(firefox_driver)
        order_page.driver.get(td.urls['order_page'])
        order_page.click_on_yandex_logo()
        WebDriverWait(firefox_driver, 10).until(EC.number_of_windows_to_be(2))
        order_page.driver.switch_to.window(order_page.driver.window_handles[-1])
        assert WebDriverWait(firefox_driver, 30).until(EC.url_to_be(td.urls['dzen_redirect']))
