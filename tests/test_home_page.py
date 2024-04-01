import pytest
import allure

from data import TestsData as td
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage


class TestMainPage:

    @pytest.mark.parametrize(
        "locator_question, locator_answer, expected_text",
        [
            [HomePageLocators.QUESTION_1, HomePageLocators.ANSWER_1, td.faq_answers['Q1']],
            [HomePageLocators.QUESTION_2, HomePageLocators.ANSWER_2, td.faq_answers['Q2']],
            [HomePageLocators.QUESTION_3, HomePageLocators.ANSWER_3, td.faq_answers['Q3']],
            [HomePageLocators.QUESTION_4, HomePageLocators.ANSWER_4, td.faq_answers['Q4']],
            [HomePageLocators.QUESTION_5, HomePageLocators.ANSWER_5, td.faq_answers['Q5']],
            [HomePageLocators.QUESTION_6, HomePageLocators.ANSWER_6, td.faq_answers['Q6']],
            [HomePageLocators.QUESTION_7, HomePageLocators.ANSWER_7, td.faq_answers['Q7']],
            [HomePageLocators.QUESTION_8, HomePageLocators.ANSWER_8, td.faq_answers['Q8']]
        ]
    )
    @allure.title('Проверка текста ответов вопросов FAQ')
    def test_faq(self, firefox_driver, locator_question, locator_answer, expected_text):
        home_page = HomePage(firefox_driver)
        home_page.scroll_into_element(HomePageLocators.QUESTIONS_SECTION)
        home_page.click_on_element(HomePageLocators.COOKIE_ACCEPT_BUTTON)
        actual_text = home_page.get_question_text(locator_question, locator_answer)
        assert actual_text == expected_text
