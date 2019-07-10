import os 
from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

firstname = browser.find_element_by_name('firstname')
firstname.send_keys("Ivan")
lastname = browser.find_element_by_name('lastname')
lastname.send_keys("Petrov")
email= browser.find_element_by_name('email')
email.send_keys("email@")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element = browser.find_element_by_id('file')
element.send_keys(file_path)

buttonSent = checkbox = browser.find_element_by_css_selector(".btn-primary")
buttonSent.click()