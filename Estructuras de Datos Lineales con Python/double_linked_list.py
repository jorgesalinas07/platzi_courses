
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class TwoWayNode(Node):
    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous

# >>> from double_linked_list import Node, TwoWayNode
# >>> head = TwoWayNode(1)
# >>> tail = head
# >>> for data in range(2,6):
# ...     tail.next = TwoWayNode(data, tail)
# ...     tail = tail.next
# ... 
# >>> probe = tail
# >>> while probe != None:
# ...     print(probe.data)
# ...     probe = probe.previous
# ... 
# 5
# 4
# 3
# 2
# 1