class Node():

    def __init__(self) -> None:
        self._position = (0,0)

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, newValue):

        if not len(newValue) == 2:
            raise ValueError("Position Tuple has to have 2 entries.")
        elif not -300 <= newValue[0] <= 300:
            raise ValueError("X coordinate has to between -300 and 300")
        elif not -300 <= newValue[1] <= 300:
            raise ValueError("Y coordinate has to between -300 and 300")
        
        self._position = newValue