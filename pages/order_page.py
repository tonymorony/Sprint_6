import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


# Класс страницы заказа самоката
class OrderPage(BasePage):

    @allure.step('Заполнение данных первой страницы формы заказа')
    def fill_order_first_stage(self, name, surname, address, phone_number):
        self.wait_until_element_is_visible(OrderPageLocators.NAME_INPUT)
        self.send_text_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_text_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_text_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        self.click_on_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click_on_element(OrderPageLocators.METRO_STATION)
        self.send_text_to_element(OrderPageLocators.PHONE_INPUT, phone_number)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнение данных второй страницы формы заказа и подтверждение формы')
    def fill_order_second_stage(self):
        self.click_on_element(OrderPageLocators.DATE_FIELD)
        self.click_on_element(OrderPageLocators.TODAY_DATE)
        self.click_on_element(OrderPageLocators.RENTAL_DURATION_FIELD)
        self.click_on_element(OrderPageLocators.RENTAL_DURATION_DROPDOWN)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверка всплывающего окна об успешном заказе')
    def check_order_success(self):
        self.wait_until_element_is_visible(OrderPageLocators.PLACED_ORDER_MODAL)

    @allure.step('Полный процесс заказа самоката')
    def scooter_order_flow(self, name, surname, address, phone_number):
        self.fill_order_first_stage(name, surname, address, phone_number)
        self.fill_order_second_stage()
        self.check_order_success()

    @allure.step('Кликаем на логотип Самокат')
    def click_on_samokat_logo(self):
        self.click_on_element(OrderPageLocators.SAMOKAT_LOGO)

    @allure.step('Кликаем на логотоип Яндекс')
    def click_on_yandex_logo(self):
        self.click_on_element(OrderPageLocators.YANDEX_LOGO)