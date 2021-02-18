import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By#ayuda a llamar a las excepciones que queremos validar

class AssertionsTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com/")

	def test_search_field(self):
		self.assertTrue(self.is_element_present(By.NAME, 'q'))

	def test_language_option(self):
		self.assertTrue(self.is_element_present(By.ID, 'select-language'))
		self.driver.implicitly_wait(3)

	def tearDown(self):
		self.driver.quit()

	#para saber si está presente el elemento
	#how: tipo de selector
	#what: el valor que tiene
	def is_element_present(self, how, what):
		try:  #busca los elementos según el parámetro
			self.driver.find_element(by = how, value = what) 
		except NoSuchElementException as variable:
			return False
		return True

