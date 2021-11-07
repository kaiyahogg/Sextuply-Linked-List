from SextuplyLinkedList import SextuplyLinkedList
from Node import Node

class Driver:
    def __init__(self):
        node = Node("hi")
        
        cube = SextuplyLinkedList(node, 0, 0, 0)
        cube._width += 2
        print(cube._width)
        # print(cube.__height)

Driver()