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

class DynamicControls(unittest.TestCase):
    #Se desea usar todos los comandos que dependen del tiempo en un pagina
    #Activar un bóton y esperar que se ejecute para continuar con los siguiente comandos
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.find_element_by_link_text('Dynamic Controls').click()
        driver.implicitly_wait(5)


    def test_dynamic_controls(self):
        #Remover y agregar checkbox y luego chulearla
        driver=self.driver
        remove_add_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        remove_add_button.click()
        remove_add_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        remove_add_button.click()
        driver.find_element_by_xpath('//*[@id="checkbox"]').click()
        
        #Habilitar espacio de escritura y escribir "Jorge"
        enable__diable_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))
        enable__diable_button.click()
        #Colocar pausa para que el espacio de texto sea posible de usar
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))
        
        writespace=driver.find_element_by_css_selector('#input-example > input[type=text]')
        writespace.send_keys('Jorge')
        sleep(3)
        enable__diable_button=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))
        enable__diable_button.click()
        
        
    def tearDown(self):
        sleep(5)
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)