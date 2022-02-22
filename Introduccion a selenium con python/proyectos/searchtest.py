import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window
        driver.implicitly_wait(5)

    #Buscar la palabra tee en el buscador de la pagina
    def test_search_tee(self):
        driver=self.driver
        #Ubicar el buscador de la pagain. En este caso se identifica con q
        search_field=driver.find_element_by_name("q")
        #Metodo para linpiar campo de busqueda en el caso de que haya algun texto
        search_field.clear()
        #Enviar simulacion de escribir tee (camisa) en el buscado de la pagina
        search_field.send_keys("tee")
        #Enviar estos datos al buscador de la pagina
        search_field.submit()

    #Buscar la palabra salt shaker en el buscado de la pagina
    def test_search_salt_shaker(self):
        driver=self.driver
        search_field=driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys("salt shaker")
        search_field.submit()
        #Encontrar productor con xpath
        #products=driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[1]/div[4]/ul/li/div/h2/a')
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        
        #Usar assert para garantizar que solo se escoge un producto
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)