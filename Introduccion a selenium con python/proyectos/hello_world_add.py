#Sirve para traer las pruebas
import unittest 
#Ejecutar a orquesta las pruebas con los reportes
from pyunitreport import HTMLTestRunner
#Para comunicarse con el navegador
from selenium import webdriver


#Definir clase para todos los casos de prueba
#Los argunentos son los casos de prueba
class Helloworld(unittest.TestCase):

    #Los test features se definen como los metodos siguientes
    #SetUp prepara el entorno necesario para la prueba
    # def setUp(self):
    #     #Lo que se a hacer es ejecutar el driver de google
    #     self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
    #     #simplificar para no escribir selfdfiver constantemente
    #     driver=self.driver
    #     #Esperar 10 segundos implicitamente antes de la siguiente acción
    #     driver.implicitly_wait(10)

    #Si queremos hacer lo mismo pero que los test se realicen en una misma ventana pero en dos pestañas diferentes
    #Se utiliza el decorador classemthod
    @classmethod
    def setUpClass(cls):
         #Lo que se a hacer es ejecutar el driver de google
         cls.driver=webdriver.Chrome(executable_path=r"./chromedriver")
         #simplificar para no escribir selfdfiver constantemente
         driver=cls.driver
         #Esperar 10 segundos implicitamente antes de la siguiente acción
         driver.implicitly_wait(10)

    #La prueba unitaria. Debe enpezar con test para que la identifique el test runner
    #Realizar acciones de la prueba para que el navegador se automatice
    
    def test_hello_world(self):
        #Simplificar
        driver=self.driver
        #get = ir 
        driver.get("https://www.platzi.com")
    
    def test_visit_wikipedia(self):
        driver=self.driver
        driver.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

    
    #Feature para a salida
    #Acciones de finalización. Ej: cerrar la ventana de navegador despues de cada prueba
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    #
    unittest.main(verbosity = 2,testRunner=HTMLTestRunner(output="Reportes",report_name="hello-world-report"))
