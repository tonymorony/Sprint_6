import allure

from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data import TestsData as td


class TestOrderPage:

    @allure.title('Успешный заказ самоката с использованием кнопки заказа в заголовке. Набор данных 1.')
    def test_successful_scooter_order_header_button(self, firefox_driver):
        ds_1 = td.scooter_order_dataset_1
        home_page = HomePage(firefox_driver)
        home_page.click_on_element(HomePageLocators.HEADER_ORDER_BUTTON)
        order_page = OrderPage(firefox_driver)
        order_page.scooter_order_flow(ds_1['name'], ds_1['surname'], ds_1['address'], ds_1['phone_number'])

    @allure.title('Успешный заказ самоката с использованием кнопки заказа в теле страницы. Набор данных 2.')
    def test_successful_scooter_order_body_button(self, firefox_driver):
        ds_2 = td.scooter_order_dataset_2
        home_page = HomePage(firefox_driver)
        home_page.scroll_into_element(HomePageLocators.BODY_ORDER_BUTTON)
        home_page.click_on_element(HomePageLocators.BODY_ORDER_BUTTON)
        order_page = OrderPage(firefox_driver)
        order_page.scooter_order_flow(ds_2['name'], ds_2['surname'], ds_2['address'], ds_2['phone_number'])
