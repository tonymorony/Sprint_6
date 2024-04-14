import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def firefox_driver():

    driver = webdriver.Firefox()
    yield driver

    driver.quit()

