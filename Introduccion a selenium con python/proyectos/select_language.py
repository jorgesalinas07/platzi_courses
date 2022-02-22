import unittest
from selenium import webdriver
#Para manipular los dropdown se importa:
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window
        driver.implicitly_wait(5)

    def test_select_language(self):
        exp_options=["English", "French", "German"]
        #Crear lista para almacenar las opciones de idioma escogidad
        act_options=[]

        #Seleccionar la opcion tipo "Dropdown" con comando "Select".
        select_language=Select(self.driver.find_element_by_id("select-language"))

        #Asegurarse de que se tengan los tres tipos de idiomas disponibles
        #con select_languaga.options se puede observar todas las opciones despues de seleccionar un archivo dropdown
        self.assertEqual(3, len(select_language.options))

        #Agrar los idiomas de la pagina a la lista act_options
        #act_options=[option for option in select_language.options]
        for option in select_language.options:
            act_options.append(option.text)

        #Verificar que las opciones en la pagina y las expuestas sean las mismas
        #Se utiliza assertListEqual para igual listas
        self.assertListEqual(exp_options, act_options)

        #Verificar que ingles sea el idioma por defecto disponible
        #Para obtener cúal es la primera opción de texto un dropdown con first_selected_option.text
        self.assertEqual("English", select_language.first_selected_option.text)

        #Escoger un idioma, se utiliza select_by_(tipo de busqueda).
        #En este caso el tipo de busqueda es visible que es lo que el usuario selecciona
        select_language.select_by_visible_text("German")
        #Verificar que se cambio a aleman
        self.assertTrue("store=german" in self.driver.current_url)

        #Cambiar el idioma con otro método
        select_language=Select(self.driver.find_element_by_id("select-language"))
        select_language.select_by_index(0)
 
    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)