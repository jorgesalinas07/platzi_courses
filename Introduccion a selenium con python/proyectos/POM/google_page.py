from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage(object):

    #Iniciar variables de busqueda
    def __init__(self,driver):
        #Varibles privada
        self._driver=driver
        self._url='https://google.com'
        self.search_locator="q"

    #Iniciar decorador para verificar que el sitio ha cargado correctamente
    @property
    def is_loaded(self):
        #Esperar a que se pueda localizar la barra de busqueda
        WebDriverWait(self._driver,10).until(EC.presence_of_element_located((By.NAME,'q')))
        return True
    
    #Iniciar decorador para ubicar el campo de busqueda
    @property
    def keyword(self):
        input_field=self._driver.find_element_by_name('q')
        return input_field.get_attribute('value')

    #Método para ingresar al url
    def open(self):
        self._driver.get(self._url)

    #Método para buscar termino en keyword
    def type_search(self, keyword):
        input_field=self._driver.find_element_by_name('q')
        input_field.send_keys(keyword)

    #Método para seleccionar submit
    def click_submit(self):
        input_field=self._driver.find_element_by_name('q')
        input_field.submit()
    
    #Método para ejecutar los dos métodos anteriores
    #Es decir, que escriba la palabra en el la barra de busqueda y lo busque
    def search(self,keyword):
        self.type_search(keyword)
        self.click_submit

