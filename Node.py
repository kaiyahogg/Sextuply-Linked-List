class Node:
    # Node state variables
    def __init__(self, data):
        self._data = data
        self._up = None
        self._down = None
        self._left = None
        self._right = None
        self._back = None
        self._forward = None
    