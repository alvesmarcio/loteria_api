from random import choice


class Lucky:
    numbers = set(range(1, 61))

    SEXTANT_1 = {1, 2, 3, 4, 5, 11, 12, 13, 14, 15}
    SEXTANT_2 = {6, 7, 8, 9, 10, 16, 17, 18, 19, 20}
    SEXTANT_3 = {21, 22, 23, 24, 25, 31, 32, 33, 34, 35}
    SEXTANT_4 = {26, 27, 28, 29, 30, 36, 37, 38, 39, 40}
    SEXTANT_5 = {41, 42, 43, 44, 45, 51, 52, 53, 54, 55}
    SEXTANT_6 = {46, 47, 48, 49, 50, 56, 57, 58, 59, 60}

    SEXTANTS = [
        SEXTANT_1,
        SEXTANT_2,
        SEXTANT_3,
        SEXTANT_4,
        SEXTANT_5,
        SEXTANT_6,
    ]

    excluded_adjacents = set()
    excluded_columns = set()
    excluded_sextants = set()

    def _remove_adjacent(number):
        Lucky.excluded_adjacents.add(number - 1)
        Lucky.excluded_adjacents.add(number + 1)

    def _remove_column(number):
        column = {n for n in range(number % 10, 61, 10)}
        Lucky.excluded_columns = Lucky.excluded_columns.union(column)

    def _remove_sextant(number):
        for sextant in Lucky.SEXTANTS:
            if number in sextant:
                Lucky.excluded_sextants = Lucky.excluded_sextants.union(sextant)
                break

    def get_numbers(*args, **kwargs):
        """
        Takes in numbers as arguments and returns a list of 6 numbers from 1 to 60.

        Optional kwargs:
        adjacent: bool,
        column: bool,
        spread: bool
        """

        numbers = set(args)
        adjacent = kwargs.get("adjacent")
        column = kwargs.get("column")
        spread = kwargs.get("spread")

        for number in numbers:
            Lucky._remove_adjacent(number)
            Lucky._remove_column(number)
            Lucky._remove_sextant(number)
            Lucky.numbers.discard(number)

        for _ in range(len(numbers), 6):

            if adjacent:
                Lucky.numbers = Lucky.numbers.difference(Lucky.excluded_adjacents)

            if column:
                Lucky.numbers = Lucky.numbers.difference(Lucky.excluded_columns)

            if spread:
                Lucky.numbers = Lucky.numbers.difference(Lucky.excluded_sextants)

            new_number = choice(tuple(Lucky.numbers))
            numbers.add(new_number)

            Lucky._remove_adjacent(new_number)
            Lucky._remove_column(new_number)
            Lucky._remove_sextant(new_number)
            Lucky.numbers.discard(new_number)

        numbers = list(numbers)
        numbers.sort()

        return numbers
