from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x, y):
	return str(int(x) + int(y))

elementnum1 = browser.find_element_by_id('num1')
elementnum2 = browser.find_element_by_id('num2')

resultsum = calc(elementnum1.text, elementnum2.text)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(resultsum) 

buttonSent = checkbox = browser.find_element_by_css_selector(".btn-default")
buttonSent.click()

