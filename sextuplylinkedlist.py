from Node import Node


class SextuplyLinkedList:
<<<<<<< HEAD
    _head: Node = None
    _RowIterator: Node = None
    _ColIterator: Node = None
    _DepIterator: Node = None
    _height = _width = _depth = 0
=======
    _head = None
    __height = __width = __depth = 0
>>>>>>> 9f809cc3bcc3c2f6b942b2d10b56d8bbb6a8296f

    # Linked list functions
    # Apply
    # Insert/Remove
    # Iterator

<<<<<<< HEAD
    def __init__(self, height, width, depth):
        self._height = height
        self._width = width
        self._depth = depth

        self._head = Node("head")
        self._RowIterator = self._ColIterator = self._DepIterator = self._head

        #grid for each layer
        createHyperGrid(dz, _width, _depth)


    def createHyperGrid(self, width, depth):
        for dz in height:
            for dy in depth:
                for dx in width:

                    if(dy==0):
                        self._RowIterator._right = Node()
                    else:
                        self._RowIterator._right = self._RowIterator._back._right._forward

                    self._RowIterator._forward = Node()
                    self._RowIterator._up = Node()

                    #doubly link
                    self._RowIterator._right._left = self._RowIterator
                    self._RowIterator._forward._back = self._RowIterator
                    self._RowIterator._up._down = self._RowIterator

                    if (dx == 0):
                        self._ColIterator = self._RowIterator._forward
                        self._DepIterator = self._ColIterator._up

                    self._RowIterator = self._RowIterator._right

                self._RowIterator = self._ColIterator

            self._RowIterator = self._DepIterator
=======
    def __init__(self, node):
        self.__head = node
        self.__width = 1

>>>>>>> 9f809cc3bcc3c2f6b942b2d10b56d8bbb6a8296f

        return