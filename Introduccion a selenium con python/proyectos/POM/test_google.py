import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):
    #Se van a buscar valores con el método ddt.
    #Con este decorados, la busqueda de las palabras se hacen una despues de otra, sin necesadad de hacer otro test para eso
    @classmethod
    def setUp(cls):
        cls.driver=webdriver.Chrome(executable_path=r"./chromedriver")


    def test_search(self):
        #Ejecutar init de googlepage con el driver de este archivo
        google=GooglePage(self.driver)
        #Ejecutar open del archivo googlepage
        google.open()
        #Usar método search de googlepage para buscar la palabra platzi
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)