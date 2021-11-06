from SextuplyLinkedList import SextuplyLinkedList
from Node import Node

class Driver:
    def __init__(self):
        node = Node("hi")
        
        cube = SextuplyLinkedList(node)
        cube.__width += 2
        print(cube.__width)
        # print(cube.__height)

Driver()