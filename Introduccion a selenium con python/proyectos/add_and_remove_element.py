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

class AddRemoveElements(unittest.TestCase):
    #En la pagina se agregan elementos con el boton add element y se eliminan con el boto delete
    #Se realiza una automatización para agregar y remover el número de elementos que el usuario escoga
    #Se valida el error en el que el usuario quiera eliminar mas elementos de los que hay diponibles para elimnar
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.find_element_by_link_text('Add/Remove Elements').click()
        driver.implicitly_wait(5)

        
    def test_add_remove(self):
        driver=self.driver
        element_added=int(input("Escriba el valor de elemento a agregar: "))
        element_removed=int(input("Escriba el valor de elementos a remover: "))
        element_result=element_added-element_removed
        try:
            if element_result<0:
                raise TypeError
            for n in range(1,element_result+1):
                element_addition=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH , '//*[@id="content"]/div/button')))
                element_addition.click()
                
        except TypeError:
            print("Se debe ingresar un mayor número de elementos a adicionar que eliminar")
            driver.quit()

        if element_result>0:
            print(f"Hay {element_result} elementos en pantalla")
        else:
            print("Hay 0 elementos en pantalla")


    def tearDown(self):
        sleep(5)
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)