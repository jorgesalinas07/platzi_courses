#Importar lo necesario para el testsuite
from unittest import TestLoader, TestSuite
#Importar para generar el reporte necesario
from pyunitreport import HTMLTestRunner
#Importar los archivos y las clases de prueba de los documentos realizados
from assertions import AssertionsTest
from searchtest import SearchTests

#Cargar los tests de los casos anteriores
assertions_test=TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test=TestLoader().loadTestsFromTestCase(SearchTests)

#Construit suit de pruebas
smoke_test=TestSuite([assertions_test, search_test])

#Parametros para el reporte
#Una forma es por medio de un diccionario
#Crear diccionario
kwargs={
    "output":'smoke-report'
}
#Se generan un número de reportes iguales a los test importados. En este caso, 2
#Crear variable runner con el resporte
runner=HTMLTestRunner(**kwargs)
#Ejecutar el runner
runner.run(smoke_test)