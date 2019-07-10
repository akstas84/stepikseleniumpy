from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
elemId = browser.find_element_by_id('treasure')
x_element = elemId.get_attribute('valuex')
print("value of x_element: ", x_element)
y = calc(x_element)


fild = browser.find_element_by_id('answer')
fild.click()
fild.send_keys(y)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

radibutton =  browser.find_element_by_id('robotsRule') 
radibutton.click()

buttonSent = checkbox = browser.find_element_by_css_selector(".btn-default")
buttonSent.click()