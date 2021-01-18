

class TwinScan:

    NR_OF_CHUCKS = 2

    def __init__(self):
        self.chuck_position = 0

    def swap_chucks(self):
        self.chuck_position = (self.chuck_position + 1) % 2