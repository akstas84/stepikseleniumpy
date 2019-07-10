from selenium import webdriver
import math
from math import log, sin

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
	return str(log(abs(12*sin(int(x)))))

elementx = browser.find_element_by_id('input_value')
result = calc(elementx.text)

fild = browser.find_element_by_id('answer')
fild.send_keys(result)

checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
checkbox.click()

radiobutton =  browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
radiobutton.click()

buttonSent = checkbox = browser.find_element_by_css_selector(".btn-default")
browser.execute_script("return arguments[0].scrollIntoView(true);", buttonSent)
buttonSent.click()