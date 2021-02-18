import unittest
from selenium import webdriver

class NombreDeClasePrueba(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver')
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_nombre_del_test(self):
        driver=self.driver
        for i in range(5): 
            print(f'hola mundo {i} ')   
        

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)