import unittest
from selenium import webdriver
#Libreria para hacer referencia a un elemento de la pagina para interactuar con el de una manera diferente
from selenium.webdriver.common.by import By
#Usar expected conditions con esperar explicitas
from selenium.webdriver.support.ui import WebDriverWait
#Importar expected conditions
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWaitTests(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.implicitly_wait(5)

    #Usar elace para ir a las cuentas del sitio
    def test_account_link(self):
        #WebDriverWait hará referencia a self.driver y esparar maximo 10 segs hasta que se cumpla la condición esperada.
        #La condición esperada en este caso es una lambda. 
        #Lamda recibe como parametro "s", que es este caso es self.driver porque es la referencia, al cual se le buscará el seleccionador de idioma 
        #Esto para despues obtener la loguitud de los elementos de sus atributos (idiomas) los cuales deben ser igual a 3
        WebDriverWait(self.driver,10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length')=='3')
        #Hacer referencia al enlace donde están las cuentas
        #WebDriverWait hace referencia a self.driver y esperará maximo 10 segundos hasta que se cumpla la condición
        #La condición esperada es la expected condition que hace referencia a la visibilidad del elemento que se esta ubicando
        #Se usa By para ubicar el texto "ACCOUNT" en la pagina web
        #Dentro del visibility_of_all_elements_located debe haber doble parentesis
        #Debe ser visibility_of_element_located y no visibility_of_all_elements_located porque sino el click() no funciona. Esto porque devuelve una lista en lugar de un valor
        account=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "ACCOUNT")))
        account.click()

    def test_create_new_customer(self):
        #Seleccionar account en la pagina
        #Se debe usar ' en lugar de ""
        self.driver.find_element_by_link_text('ACCOUNT').click()

        #Usar WebDriverWait para selecionar My account hasta que se confirme que la expected condición se cumpla
        #La expected condicion de este caso es que sea visible el texto "My Account"
        #Dentro del visibility_of_element_located debe haber doble parentesis
        #Debe ser visibility_of_element_located y no visibility_of_all_elements_located porque sino el click() no funciona. Esto porque devuelve una lista en lugar de un valor
        my_account=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT, "My Account")))
        my_account.click()
        #Usar WebDriverWait para seleccionar CREATE ACCOUNT de la pagina hasta que se confirme que la expected condición se cumpla
        #La expected condition es que el boton CREATE ACCOUNT se clickable
        #Esta expected condition no necesita doble parentesis
        create_account_button=WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.LINK_TEXT, "CREATE AN ACCOUNT")))
        create_account_button.click()

        #Verificar que estamos en la pagina para creat usuario
        #Para esto se usa la expected condition de que el titulo de la página será Create New Customer Account
        WebDriverWait(self.driver,10).until(EC.title_contains("Create New Customer Account"))
 


 
    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)