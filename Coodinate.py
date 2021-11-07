class Coordinate:
    # Private x, y, and z coordinates
    _x = None
    _y = None
    _z = None

    def __init__(self, i, j, k):
        self._x = i
        self._y = j
        self._z = k