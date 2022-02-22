import unittest
from selenium import webdriver
#Importar libreria para poder usar ddt
from ddt import ddt, data, unpack

#Decorador necesario para iniciar ddt
@ddt
class SearchTests(unittest.TestCase):
    #Se van a buscar valores con el método ddt.
    #Con este decorados, la busqueda de las palabras se hacen una despues de otra, sin necesadad de hacer otro test para eso
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.implicitly_wait(5)

    #Decorador con tuplas de los terminos que se van a encontrar las palabras
    #Se colocar la parabra a buscar y el número de veces que se espera que aparezca
    @data(('dress',5),('music',5))
    #Desempaquetar tuplas para poder verlas de forma individual
    @unpack 
    #Variables adcionales para buscar el valor y el número de veces que esta
    def test_search_ddt(self, search_value, expected_count):
        driver=self.driver
        #Ubicar la barra de busqueda, limpiar en caso de que haya algo
        #Despues escrubir el objetivo de busqueda que está en "Seatch Value" y buscar
        search_field=driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        #Identificar los productos con xpath
        #La estructura es el xpath: '//donde se encuentra(Ej: h2)[nombre de la clase (Ej:@class="product-name")]/a'
        products=driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))


    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)