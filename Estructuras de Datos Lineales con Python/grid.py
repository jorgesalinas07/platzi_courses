from arreglo import Arreglo
import random
class Grid():
    def __init__(self, rows, columns, fill_value = None):
        #Crear array para las filas
        self.data = Arreglo(rows)
        #Llenar de datos la filas con las columnas para hacerlo 2d
        for row in range(rows):
            self.data[row] = Arreglo(columns, fill_value)

    #Obtener la altura de la matrix usando self.data que tiene la info de las filas
    def get_height(self):
        return len(self.data)

    #Obtener el ancho de la matrix usando self.data[0] que tiene la info de las columnas porque toma el valor de la primera fila
    def get_width(self):
        #Se esta colocando un arreay sobre otro en la posición 0.
        return len(self.data[0])

    def __getitem__(self, index):
        #Se le da el valor de la row como index. Esto trae toda la fila. Se usa [] para el valor de la columna
        return self.data[index]

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "
        #Espacio
            result += "\n"
        return str(result)

    def __replaceitems__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                self.data[row][col] = random.randint(1,100)
                result += str(self.data[row][col]) + " "
            result += "\n"
        return result

# >>> from grid import Grid
# >>> matrix = Grid(3,3)
# >>> print(matrix)
# None None None 
# None None None 
# None None None 

# >>> for row in range(matrix.get_height()):
# ...     for column in range(matrix.get_width()):
# ...             matrix[row][column] = row*column
# ... 
# >>> print(matrix)
# 0 0 0 
# 0 1 2 
# 0 2 4 

# >>> matrix.get_height()
# 3
# >>> matrix.get_width()
# 3
# >>> matrix.__getitem__(1)
# <arreglo.Arreglo object at 0x7f329e4113d0>
# >>> matrix.__getitem__(2)[0]
# 0
# >>> matrix.__getitem__(1)[1]
# 1
# >>> matrix.__str__()
# '0 0 0 \n0 1 2 \n0 2 4 \n'