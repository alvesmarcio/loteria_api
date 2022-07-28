from random import choice


def lucky(req_numbers, adjacent=False, column=False, spread=False):
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

    def _remove_adjacent(number, excluded_adjacents):
        excluded_adjacents.add(number - 1)
        excluded_adjacents.add(number + 1)
        return excluded_adjacents

    def _remove_column(number, excluded_columns):
        column = {n for n in range(number % 10, 61, 10)}
        excluded_columns = excluded_columns.union(column)
        return excluded_columns

    def _remove_sextant(number, excluded_sextants):
        for sextant in SEXTANTS:
            if number in sextant:
                excluded_sextants = excluded_sextants.union(sextant)
                break
        return excluded_sextants

        """
        Takes in numbers as arguments and returns a list of 6 numbers from 1 to 60.

        Optional kwargs:
        adjacent: bool,
        column: bool,
        spread: bool
        """

    for number in req_numbers:
        excluded_adjacents = excluded_adjacents.union(_remove_adjacent(number, excluded_adjacents))
        excluded_columns = excluded_columns.union(_remove_column(number, excluded_columns))
        excluded_sextants = excluded_sextants.union(_remove_sextant(number, excluded_sextants))
        numbers.discard(number)

    for _ in range(len(req_numbers), 6):

        if adjacent == True:
            numbers = numbers.difference(excluded_adjacents)

        if column == True:
            numbers = numbers.difference(excluded_columns)

        if spread == True:
            numbers = numbers.difference(excluded_sextants)

        new_number = choice(tuple(numbers))
        req_numbers.add(new_number)

        excluded_adjacents = excluded_adjacents.union(_remove_adjacent(new_number, excluded_adjacents))
        excluded_columns = excluded_columns.union(_remove_column(new_number, excluded_columns))
        excluded_sextants = excluded_sextants.union(_remove_sextant(new_number, excluded_sextants))
        numbers.discard(new_number)
        
    req_numbers = list(req_numbers)
    req_numbers.sort()

    return req_numbers
