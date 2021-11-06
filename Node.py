class Node:
    # Node state variables
    _data = None
    next_up = None
    next_down = None
    next_left = None
    next_right = None
    next_back = None
    next_forward = None
    
    def __init__(self, data):
        self._data = data
    