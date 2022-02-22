import unittest
from selenium import webdriver
#Importar libreria para el exception asert para validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException
#Importar libreria para poder cambiar el tipo de selector
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window
        driver.implicitly_wait(5)

    #Buscar el valor "q" por el método de busqueda "NAME"
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME,"q"))

    #Buscar el valor "select-language" por el método de busqueda "id"
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID,"select-language"))


    def tearDown(self):
        self.driver.quit()

    #Confirmar que un valor (what) con el un método de busqyeda (how) existe.
    #Si existe, devolver True, sino devolver un error y False
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value=what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__=="__main__":
    unittest.main(verbosity=2)