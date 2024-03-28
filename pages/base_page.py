import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем видимости элемента')
    def wait_until_element_is_visible(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))

    @allure.step('Ищем элемент')
    def get_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    @allure.step('Скроллим до элемента')
    def scroll_into_element(self, locator):
        self.wait_until_element_is_visible(locator)
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текст элемента')
    def get_element_text(self, locator):
        self.wait_until_element_is_visible(locator)
        element = self.get_element(locator)
        return element.text

    @allure.step('Кликаем по элементу')
    def click_on_element(self, locator):
        self.wait_until_element_is_visible(locator)
        element = self.get_element(locator)
        element.click()

    @allure.step('Передаем текст элементу')
    def send_text_to_element(self, locator, text_to_send):
        self.wait_until_element_is_visible(locator)
        element = self.get_element(locator)
        element.send_keys(text_to_send)

    @allure.step('Выбираем пункт из выпадающего списка')
    def select_from_dropdown(self, locator, selection_text):
        select = Select(self.get_element(locator))
        select.select_by_visible_text(selection_text)
