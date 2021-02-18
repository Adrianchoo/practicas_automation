import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_compare_products_removal_alert(self):
        driver=self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('Tee')
        search_field.submit()



    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)