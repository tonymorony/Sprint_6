from selenium.webdriver.common.by import By


class HomePageLocators:

    QUESTION_1 = By.XPATH, ".//div[@id='accordion__heading-0' and @class ='accordion__button']"
    ANSWER_1 = By.XPATH, ".//parent::div[@id='accordion__panel-0' and @class ='accordion__panel']/p"
    QUESTION_2 = By.XPATH, ".//div[@id='accordion__heading-1' and @class ='accordion__button']"
    ANSWER_2 = By.XPATH, ".//div[@id='accordion__panel-1' and @class ='accordion__panel']/p"
    QUESTION_3 = By.XPATH, ".//div[@id='accordion__heading-2' and @class ='accordion__button']"
    ANSWER_3 = By.XPATH, ".//div[@id='accordion__panel-2' and @class ='accordion__panel']/p"
    QUESTION_4 = By.XPATH, ".//div[@id='accordion__heading-3' and @class ='accordion__button']"
    ANSWER_4 = By.XPATH, ".//div[@id='accordion__panel-3' and @class ='accordion__panel']/p"
    QUESTION_5 = By.XPATH, ".//div[@id='accordion__heading-4' and @class ='accordion__button']"
    ANSWER_5 = By.XPATH, ".//div[@id='accordion__panel-4' and @class ='accordion__panel']/p"
    QUESTION_6 = By.XPATH, ".//div[@id='accordion__heading-5' and @class ='accordion__button']"
    ANSWER_6 = By.XPATH, ".//div[@id='accordion__panel-5' and @class ='accordion__panel']/p"
    QUESTION_7 = By.XPATH, ".//div[@id='accordion__heading-6' and @class ='accordion__button']"
    ANSWER_7 = By.XPATH, ".//div[@id='accordion__panel-6' and @class ='accordion__panel']/p"
    QUESTION_8 = By.XPATH, ".//div[@id='accordion__heading-7' and @class ='accordion__button']"
    ANSWER_8 = By.XPATH, ".//div[@id='accordion__panel-7' and @class ='accordion__panel']/p"
    QUESTIONS_SECTION = By.XPATH, './/div[contains(@class, "Home_SubHeader__zwi_E") and text()="Вопросы о важном"]'
    COOKIE_ACCEPT_BUTTON = By.ID, 'rcc-confirm-button'
    HEADER_ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']"
    BODY_ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
