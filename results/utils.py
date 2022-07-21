from random import sample


class Lucky:
    numbers: set = range(1, 61)

    def getNumbers():

        return sample(Lucky.numbers, 6)
