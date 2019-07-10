from selenium import webdriver
import math
from math import log, sin


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
	return  str(log(abs(12*sin(int(x)))))

buttonpp = browser.find_element_by_css_selector('.btn-primary')
buttonpp.click()

new_window = browser.window_handles[1]
first_window = browser.window_handles[0]

browser.switch_to.window(new_window)

valuex = browser.find_element_by_id('input_value')

result = calc(valuex.text)

stransver = browser.find_element_by_id('answer')
stransver.send_keys(result)

buttonp2 = browser.find_element_by_css_selector('.btn-primary')
buttonp2.click()