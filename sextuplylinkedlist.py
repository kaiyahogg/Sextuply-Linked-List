from Node import Node
from Coordinate import Coordinate

class SextuplyLinkedList:
    _head: Node = None
    _RowIterator: Node = None
    _ColIterator: Node = None
    _DepIterator: Node = None
    _height = _width = _depth = 0

    # Linked list functions
    # Apply
    # Insert/Remove
    # Iterator

    def __init__(self, height, width, depth):
        self._height = height
        self._width = width
        self._depth = depth

        self._head = Node("head")
        self._RowIterator = self._ColIterator = self._DepIterator = self._head

        createHyperGrid(dz, _width, _depth)
        return

    def createHyperGrid(self, width, depth):
        for dz in height:
            for dy in depth:
                for dx in width:

                    if dy==0:
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

        return

    def getNode(self, coords: Coordinate):

        self._RowIterator = self._head

        for x in range(coords.x):
            self._RowIterator = self._RowIterator._right
        for y in range(coords.y):
            self._RowIterator = self._RowIterator._forward
        for z in range(coords.z):
            self._RowIterator = self._RowIterator._up

        return