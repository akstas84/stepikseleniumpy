from selenium import webdriver
import time
import unittest


class TestsRegistration(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()

################test1
	def test_registaration_strreg1(self):
		link = "http://suninjuly.github.io/registration1.html"
		driver = self.driver
		driver.get(link)

		firstname = driver.find_element_by_css_selector("[placeholder='Введите имя']")
		firstname.send_keys("Имя")
		lastname = driver.find_element_by_css_selector("[placeholder='Введите фамилию']")
		lastname.send_keys("Фамилия")
		mail = driver.find_element_by_css_selector("[placeholder='Введите Email']")
		mail.send_keys("мейл")

		button = driver.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(1)
		welcome_text_elt = driver.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text

		self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

################test2
	def test_registaration_strreg2(self):
		link = "http://suninjuly.github.io/registration2.html"
		driver = self.driver
		driver.get(link)

		firstname = driver.find_element_by_css_selector("[placeholder='Введите имя']")
		firstname.send_keys("Имя")
		lastname = driver.find_element_by_css_selector("[placeholder='Введите фамилию']")
		lastname.send_keys("Фамилия")
		mail = driver.find_element_by_css_selector("[placeholder='Введите Email']")
		mail.send_keys("мейл")

		button = driver.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(1)
		welcome_text_elt = driver.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text

		self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text) 

########main#######
if __name__ == "__main__":
    unittest.main()