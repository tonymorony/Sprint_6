import allure
from pages.base_page import BasePage
from data import TestsData as td


# Класс главной страницы
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(td.urls['home_page'])

    @allure.step('Раскрываем блок с вопросом FAQ и получаем текст ответа')
    def get_question_text(self, locator_question, locator_answer):
        self.wait_until_element_is_visible(locator_question)
        self.click_on_element(locator_question)
        self.wait_until_element_is_visible(locator_answer)
        return self.get_element_text(locator_answer)

