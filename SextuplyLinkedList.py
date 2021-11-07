from Node import Node
from Coodinate import Coordinate

class SextuplyLinkedList:
    head: Node = None
    RowIterator: Node = None
    ColIterator: Node = None
    DepIterator: Node = None
    height = width = depth = 0

    def __init__(self, height, width, depth):
        # self.data = data
        self.height = height
        self.width = width
        self.depth = depth

        self.head = Node()
        self.RowIterator = self.ColIterator = self.DepIterator = self.head

        # grid for each layer
        self.createHyperGrid(self.height, self.width, self.depth)
        return

    def createHyperGrid(self, width, depth, height):
        for dz in range(height):
            for dy in range(depth):
                for dx in range(width):

                    if dy==0:
                        self.RowIterator.right = Node()
                    else:
                        self.RowIterator.right = self.RowIterator.back.right.forward

                    if dz == 0:
                        self.RowIterator.forward = Node()
                    else:
                        self.RowIterator.forward = self.RowIterator.down.forward.up

                    self.RowIterator.up = Node()

                    # doubly link
                    self.RowIterator.right.left = self.RowIterator
                    self.RowIterator.forward.back = self.RowIterator
                    self.RowIterator.up.down = self.RowIterator

                    if (dx == 0):
                        self.ColIterator = self.RowIterator.forward
                        self.DepIterator = self.RowIterator.up

                    self.RowIterator = self.RowIterator.right

                self.RowIterator = self.ColIterator

            self.RowIterator = self.DepIterator

        return

    def getNode(self, coords: Coordinate):

        self.RowIterator = self.head

        for x in range(coords.x):
            self.RowIterator = self.RowIterator.right
        for y in range(coords.y):
            self.RowIterator = self.RowIterator.forward
        for z in range(coords.z):
            self.RowIterator = self.RowIterator.up

        return
