"""There is goig to be a stack based Queue and a list based stack"""



class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []
    
    def enqueue(self, data):
        """Add values to the inbound (list based stack"""
        self.inbound_stack.append(data)

    def dequeue(self):
        """ Remove values. Elements added to inbound stack are moved to the outbound stack"""
        #Si el stack exterior está vacio
        if not self.outbound_stack:
            #Pasar los elementos del stack interior al exterior
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        
        return self.outbound_stack.pop()


if __name__ == "__main__":
    number = Queue()
    number.enqueue(5)
    number.enqueue(6)
    number.enqueue(7)
    print(number.inbound_stack)
    print(number.outbound_stack)
    number.dequeue()
    print(number.inbound_stack)
    print(number.outbound_stack)