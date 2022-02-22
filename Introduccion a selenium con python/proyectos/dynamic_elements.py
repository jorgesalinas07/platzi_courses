import unittest
from unittest.case import TestCase
from selenium import webdriver
from time import sleep
#Libreria para hacer referencia a un elemento de la pagina para interactuar con el de una manera diferente
from selenium.webdriver.common.by import By
#Usar expected conditions con esperar explicitas
from selenium.webdriver.support.ui import WebDriverWait
#Importar expected conditions
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

class DynamicElements(unittest.TestCase):
    #Se desea hallar la palabra gallery en una pagina en la cuál esta palabra aparece y desaparece en cada refresh
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.find_element_by_link_text('Disappearing Elements').click()
        driver.implicitly_wait(5)


    def test_name_element(self):
        #Esté método para hayar Gallery funciona buscando el xpath y sino lo encuentra, refrescar
        driver=self.driver
        xpath_objetive='//*[@id="content"]/div/ul/li[5]/a'
        actual_xpath=0
        encontrada=False
        contador=0
        while encontrada==False:
            try:
                driver.find_element_by_xpath('//*[@id="content"]/div/ul/li[5]/a')
                encontrada==True
                break
            except:
                contador+=1
                driver.refresh()

        print(f'Se refresco la pagina {contador} hasta encontrar el botón galeria')

    def tearDown(self):
        sleep(5)
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)