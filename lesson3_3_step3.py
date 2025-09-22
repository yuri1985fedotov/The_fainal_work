import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_first_registration():
    link_name = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link_name)

    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys('answer')
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys('answer2')
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys('answer3')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert 'Congratulations! You have successfully registered!' == welcome_text, 'expected text != actual text'


def test_second_registration():
    link_name = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link_name)

    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys('answer')
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys('answer2')
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys('answer3')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == 'Congratulations! You have successfully registered!', 'expected text != actual text'


if __name__ == '__main__':
    pytest.main()
