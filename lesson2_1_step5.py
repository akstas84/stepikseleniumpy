from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)



fild = browser.find_element_by_css_selector('.form-control')
fild.click()
fild.send_keys(y)

checkbox = browser.find_element_by_css_selector("[for= 'robotCheckbox']")
checkbox.click()

radibutton =  browser.find_element_by_id('robotsRule') 
radibutton.click()

buttonSent = checkbox = browser.find_element_by_css_selector(".btn-default")
buttonSent.click()