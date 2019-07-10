from selenium import webdriver
import math
from math import log, sin 

link = "http://suninjuly.github.io/alert_accept.html"
driver = webdriver
browser = driver.Chrome()
browser.get(link)

def calc(x):
	return  str(log(abs(12*sin(int(x)))))

buttonp1 = browser.find_element_by_css_selector('.btn-primary')
buttonp1.click()

confirm = browser.switch_to.alert
confirm.accept()

valuex = browser.find_element_by_id('input_value')

result = calc(valuex.text)

stransver = browser.find_element_by_id('answer')
stransver.send_keys(result)

buttonp2 = browser.find_element_by_css_selector('.btn-primary')
buttonp2.click()