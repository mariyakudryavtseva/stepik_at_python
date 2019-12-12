from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока цена не станет 100
    prize = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element_by_id("book")
    button.click()
	
	# порскроллим страницу вниз до кнопки Submit
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	
	# Считываем значение переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
	
    # Вводим ответ ln(abs(12*sin(x))) в текстовое поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
	
	# Наимаем на кнопку Submit
#    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()