from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_INPUT = By.XPATH, ".//input[@placeholder ='* Имя']"
    SURNAME_INPUT = By.XPATH, ".//input[@placeholder ='* Фамилия']"
    ADDRESS_INPUT = By.XPATH, ".//input[@placeholder ='* Адрес: куда привезти заказ']"
    METRO_STATION_INPUT = By.XPATH, ".//input[@placeholder='* Станция метро']"
    METRO_STATION = By.XPATH, './/*[@class="select-search__row"]'
    PHONE_INPUT = By.XPATH, ".//input[@placeholder ='* Телефон: на него позвонит курьер']"
    NEXT_BUTTON = By.XPATH, (".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' "
                             "and contains(text(), 'Далее')]")
    DATE_FIELD = By.XPATH, './/input[contains(@placeholder, "* Когда привезти самокат")]'
    TODAY_DATE = By.XPATH, './/*[contains(@class, "today")]'
    RENTAL_DURATION_FIELD = By.XPATH, './/*[contains(text(), "Срок аренды")]'
    RENTAL_DURATION_DROPDOWN = By.XPATH, './/*[@class="Dropdown-option"]'
    ORDER_BUTTON = By.XPATH, (".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' "
                             "and contains(text(), 'Заказать')]")
    CONFIRM_ORDER_BUTTON = By.XPATH, './/button[contains(@class, "Button_Middle") and text()="Да"]'
    PLACED_ORDER_MODAL = By.XPATH, '//*[contains(@class, "Order_Modal_")]'
    SAMOKAT_LOGO = By.XPATH, '//*[starts-with(@class, "Header_LogoScooter_")]'
    YANDEX_LOGO = By.XPATH, '//*[starts-with(@class, "Header_LogoYandex_")]'
