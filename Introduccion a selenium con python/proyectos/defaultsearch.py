import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.implicitly_wait(5)
        

    def test_search_text_field(self):
        #selector de elemento search
        search_field=self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        #selector de elemento
        search_name=self.driver.find_element_by_name("q")

    def test_search_text_field_by_class(self):
        #Selector del elemento
        search_class=self.driver.find_element_by_class_name("input-text")

    def test_search_button_enaled(self):
        button=self.driver.find_element_by_class_name("button")

    #Hacer una lista de elementos
    def test_count_of_promo_banner_images(self):
        banner_list=self.driver.find_element_by_class_name("promos")
        #Selector por tags
        banners=banner_list.find_elements_by_tag_name("img")
        #Verificar si se cumple la condición con un assert
        self.assertEqual(3, len(banners))

    #Seleccionar variablaes que tienen mucha info agregada
    def test_vip_promo(self):
        #Se busca usando el xpath de la pagina
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')
    
    #Seleccional archivos CSS
    def test_shopping_cart(self):
        shopping_cart_icon=self.driver.find_element_by_css_selector("div.header-minicart span.icon")
        #Estructura para la busqueda "div.nombre de la division span.nombre del span"

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)