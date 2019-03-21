class Prob17(object):

    def __init__(self):
        self.dict = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 15:7, 18:8}

    def count(self, num):
        if num > 0 and num <= 13:
            return self.dict[num]