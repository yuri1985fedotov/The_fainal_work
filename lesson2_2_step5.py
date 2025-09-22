from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "input_value")
    y = calc(x)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Отправляем заполненную форму
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    option3 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    option3.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()