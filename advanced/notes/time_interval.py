class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.total_seconds = hours * 3600 + minutes * 60 + seconds # convert into seconds

    def to_hms(self):
        h = self.total_seconds // 3600
        m = (self.total_seconds % 3600) // 60
        s = self.total_seconds % 60
        return h, m, s

    def __add__(self, other):
        # 1. validate operand type
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only add TimeInterval to TimeInterval")
        
        # 2. Add using internal represenation

    def __sub__(self, other):
        pass

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

