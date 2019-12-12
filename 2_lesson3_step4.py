from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку I want to go on a magical journey!
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
	
	# Нажимаем на кнопку Ok на алерте
    confirm = browser.switch_to.alert
    confirm.accept() 

    # Считываем значение переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
	
    # Вводим ответ ln(abs(12*sin(x))) в текстовое поле
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
	
	# Наимаем на кнопку Submit
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()