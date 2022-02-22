

class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self,data):
        """Insert a value in the queue"""
        #Agregar dato con insert
        self.items.insert(0,data)
        self.size += 1
    
    def dequeue(self):
        """Delete the first value of the list"""
        data = self.items.pop()
        self.size -= 1
        return data
    
    def traverse(self):
        """ Show elements of the queue """
        total_items = self.size

        for item in range(total_items):
            print(self.items[item])

# >>> from list_based_queue import ListQueue
# >>> food = ListQueue()
# >>> food.enqueue("egg")
# >>> food.enqueue("ham")
# >>> from list_based_queue import ListQueue
# >>> food = ListQueue
# >>> food.enqueue("egg")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: enqueue() missing 1 required positional argument: 'data'
# >>> food = ListQueue
# >>> food = ListQueue()
# >>> food.enqueue("egg")
# >>> food.enqueue("ham")
# >>> food.enqueue("spam")
# >>> food.traverse()