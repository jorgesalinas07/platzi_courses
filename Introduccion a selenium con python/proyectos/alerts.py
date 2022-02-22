import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.implicitly_wait(5)
        
    def test_compare_products_removal_alert(self):
        #Buscar la barra de busqueda
        driver=self.driver
        search_field=driver.find_element_by_name("q")
        search_field.clear()
        #Buscar tee en el buscador
        search_field.send_keys("tee")
        search_field.submit()

        #Obtener el elemento "link to compare" y darle click
        driver.find_element_by_class_name('link-compare').click()
        self.driver.implicitly_wait(30)
        #Se accede al text del clear all. Al hacerlo, se dispara el alert
        driver.find_element_by_link_text('Clear All').click()

        #Mover el cursor hacia el alert creado
        alert = driver.switch_to.alert
        #Extrar el texto mostrado en el alert
        alert_text=alert.text

        #Confirmar que el alert recibido es el deseado
        self.assertEquals("Are you sure you would like to remove all products from your comparison?", alert_text)
        #Simular click en el aceptar en el alert
        alert.accept()



    def tearDown(self):
        self.driver.implicitly_wait(30)
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)