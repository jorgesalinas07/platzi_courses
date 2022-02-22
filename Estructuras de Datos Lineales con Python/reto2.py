import random
from grid import Grid
matrix = Grid(3,3)
for row in range(matrix.get_height()):
    for column in range(matrix.get_width()):
        matrix[row][column] = row*column

print(matrix)
print(matrix.__replaceitems__())

from grid import Grid
from arreglo import Arreglo
import random
class cube():
    def __init__(self, rows, columns, deep, fill_value = None):
        #Crear array para las filas
        self.data = Grid(rows, columns)
        #Llenar de datos la filas con las columnas para hacerlo 2d
        for row in range(rows):
            for column in columns:
                self.data[row, column] = Arreglo(deep, fill_value=fill_value)

    #Obtener la altura de la matrix usando self.data que tiene la info de las filas
    def get_height(self):
        return Grid.get_height

    #Obtener el ancho de la matrix usando self.data[0] que tiene la info de las columnas porque toma el valor de la primera fila
    def get_width(self):
        #Se esta colocando un arreay sobre otro en la posición 0.
        return Grid.get_width

    def get_deep(self):
        #Se esta colocando un arreay sobre otro en la posición 0.
        return len(self.data[0,0])

    def __getitem__(self, index):
        #Se le da el valor de la row como index. Esto trae toda la fila. Se usa [] para el valor de la columna
        return self.data[index]

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for de in range(self.get_deep()):
                    result += str(self.data[row][col][de]) + " "
        #Espacio
            result += "\n"
        return str(result)

    def __replaceitems__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for de in range(self.get_deep()):
                    self.data[row][col][de] = random.randint(1,100)
                    result += str(self.data[row][col]) + " "
        result += "\n"
        return result
