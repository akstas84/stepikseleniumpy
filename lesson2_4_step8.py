from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from math import log, sin

link = "http://suninjuly.github.io/explicit_wait2.html" 
browser = webdriver.Chrome()
browser.get(link)

checkprice = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "10000 RUR"))

bookbutton = browser.find_element_by_css_selector('.btn-primary')
bookbutton.click()


def calc(x):
	return  str(log(abs(12*sin(int(x)))))

valuex = browser.find_element_by_id('input_value')

result = calc(valuex.text)

stransver = browser.find_element_by_id('answer')
stransver.send_keys(result)

submitbutton = browser.find_element_by_id('solve')
submitbutton.click()
