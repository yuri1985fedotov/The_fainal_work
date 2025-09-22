from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[1]/input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[2]/input')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[3]/input')
    input3.send_keys("Smolensk")
    time.sleep(5)
    # Отправляем заполненную форму
    option1 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    option1.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
