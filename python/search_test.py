import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomeMadeTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        cls.driver.implicitly_wait(3)

    def test_search_text_field(self):
        self.driver.get('https://www.platzi.com')
        
    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.com')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output='reportes', report_name='hello-world-report'))
