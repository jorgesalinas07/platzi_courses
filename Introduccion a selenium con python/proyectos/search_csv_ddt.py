import csv, unittest
from selenium import webdriver
#Importar libreria para poder usar ddt
from ddt import ddt, data, unpack


#Consultar el archivo csv para obtener el nombre de la palabra a buscar y el número de repeticiones del mismo
#Para esto, se va a crear una tabla con los elementos del archiv csv
def get_data(file_name):
    #Crear lista para el número de las filas que hay
    rows=[]
    #Importar el archivo en modo lectura y guardarlo en data_file
    data_file=open(file_name, "r")
    #La libreria csv.reader se encarga de leer los datos de data_file
    reader=csv.reader(data_file)
    #Indicar salto a la siguiente fila de datos para no tomar la cabecera
    next(reader, None)

    for row in reader:
        rows.append(row)
    
    return rows


#Decorador necesario para iniciar ddt
@ddt
class SearchCsvDDT(unittest.TestCase):
    #Se van a buscar valores con el método ddt.
    #Con este decorados, la busqueda de las palabras se hacen una despues de otra, sin necesadad de hacer otro test para eso
    #Ademas, se importara un archivo CSV con un tabla que contiene una lista de palabras a buscar con su respectivo número esperado de repeticiones
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver=self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Maximizar pantalla para evitar cambios de ubicacion dependiendo del tamaño de la vista
        driver.maximize_window()
        driver.implicitly_wait(5)

    #Decorador con tuplas de los terminos que se van a encontrar las palabras
    #Se colocar la parabra a buscar y el número de veces que se espera que aparezca
    #Se usa la función para importar los valores del archivo csv
    @data(*get_data('testdata.csv'))
    #@data(('dress',5),('music',5))
    #Desempaquetar tuplas para poder verlas de forma individual
    @unpack 
    #Variables adcionales para buscar el valor y el número de veces que esta
    def test_search_ddt(self, search_value, expected_count):
        driver=self.driver
        #Ubicar la barra de busqueda, limpiar en caso de que haya algo
        #Despues escrubir el objetivo de busqueda que está en "Seatch Value" y buscar
        search_field=driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        #Identificar los productos con xpath
        #La estructura es el xpath: '//donde se encuentra(Ej: h2)[nombre de la clase (Ej:@class="product-name")]/a'
        products=driver.find_elements_by_xpath('//h2[@class="product-name"]/a')

        #Convertir a entero el valor del archivo csv
        expected_count=int(expected_count)

        
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message=driver.find_element_by_class_name("note-msg")
            self.assertEqual('Your search returns no results', message)
        
        print(f'Found{len(products)} products')


    def tearDown(self):
        self.driver.quit()



if __name__=="__main__":
    unittest.main(verbosity=2)