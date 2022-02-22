import unittest
from selenium import webdriver
from time import sleep

class Typos(unittest.TestCase):
    #Se va a confirmar que se muestre un texto en la pantalla
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.find_element_by_link_text('Typos').click()
        driver.implicitly_wait(5)
        
    def test_find_typo(self):
        driver=self.driver
        #Guardar el texto que se muestra en pantalla
        paragraph_to_check=driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        text_to_check=paragraph_to_check.text
        #Colocar assert para confirmar que text_to_check no esta vacio es un string
        self.assertTrue(isinstance(text_to_check, str) and text_to_check.strip())
        print(text_to_check)
        #Contador para mostrar las veces que se refresco la pagina
        #Variable para confirmar que se encontró o no el texto deseado
        #Variable para el texto correcto que deberia tener
        tries=1
        found=False
        correct_text="Sometimes you'll see a typo, other times you won't."

        # while text_to_check != correct_text:
        #     paragraph_to_check=driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        #     text_to_check=paragraph_to_check.text
        #     driver.refresh()
        
        while not found: 
            paragraph_to_check=driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
            text_to_check=paragraph_to_check.text   
            if text_to_check==correct_text:
                found = True
            tries +=1
            driver.refresh()

        self.assertEqual(found, True)
        
        print(f'It took {tries} tries to find the typo')
        sleep(6)

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)