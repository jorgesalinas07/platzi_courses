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
        driver=self.driver
        #Esta forma de hallar Gallery es refrescando la pagina cada que solo encuentre 4 elementos hasta que hayan 5
        #Esto porque el 5to elemento siempre es Gallery
        options=[]
        menu=5
        tries=1

        while len(options)<5:
            options.clear()

            for i in range(menu):
                try:
                    option_name=driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i+1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i+1} is NOT FOUND")
                    tries +=1
                    driver.refresh()

        print(f'Finished in {tries} tries')

    def tearDown(self):
        sleep(5)
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)