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

class Tables(unittest.TestCase):
    
    #Trabajar con tablas de una página
    
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.find_element_by_link_text('Sortable Data Tables').click()
        driver.implicitly_wait(5)

    def test_sort_tables(self):
        driver=self.driver

        #Crear lista para tomar los datos de las 5 columnas de la tabal de la página
        table_data=[[] for i in range(5) ]
        print(table_data)

        for i in range(5):
            #Las columnas de la tabla se idenfica con el xpath y no con el selector
            #Eso se hace para poder cambiar el número en el path y así poder recoger toda la tabla con un for
            #El xpath para este caso es el span
            #Se van a ir tomando los valores de las filas y las columans de la tabla de internet para guardarlos en la lista
            #Se coloca i+1 porque i inicia en 0
            header=driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i+1}]/span')
            table_data[i].append(header.text)

            #4 Porque la tabla de internet tiene 4 filas
            for j in range (4):
                #Se toma el j+1 para que vaya tomando todos los valores de fila.
                #Se toma i+1 para que tome el valor de la columna actual
                row_data=driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                table_data[i].append(row_data.text)
        print(table_data )

    def tearDown(self):
        sleep(5)
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)