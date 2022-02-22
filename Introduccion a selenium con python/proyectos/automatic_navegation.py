import unittest
from selenium import webdriver
#Agregar unas pausas antes de pasar al siguiente comando
from time import sleep

class NavegationTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://google.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.implicitly_wait(5)
        
    def test_browser_navegation(self):
        driver=self.driver
        #Buscar la pagina de platzi en el buscados de google
        searchfield=driver.find_element_by_name("q")
        searchfield.clear()
        searchfield.send_keys("platzi")
        searchfield.submit()

        #avanzar una pagina, luego retrocede y luego avanzar
        driver.back()
        #Pausas
        sleep(3)
        driver.forward()
        sleep(3)
        driver.refresh()
        sleep(3)

 
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)