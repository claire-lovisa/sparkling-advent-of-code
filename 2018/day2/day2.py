"""Solution to Advent of Code 2018, Day 2: Inventory Management System (https://adventofcode.com/2018/day/1)."""
import pathlib
import collections
import itertools


def hasOccurence(string, expected_occurence):
    """Pour chaque lettre de la string, on va compter le nb d'occurences de la
    lettre (sentence.count('a')). Des qu'on en trouve une qui va bien on repond
    1, sinon 0."""

    for letter in string:
        occurence = string.count(letter)
        if(occurence == expected_occurence):
            return 1
    return 0


def part_one(ids):
    '''
    Question:
        What is the checksum for your list of box IDs?

    Check the ids with 2 times the same letter in it, same with 3 time,
    and then multiply the two numbers.
    '''

    number_of_two_times_occurences = 0
    number_of_three_times_occurences = 0

    for n in ids:
        if(hasOccurence(n, 2)):
            number_of_two_times_occurences += 1

        if(hasOccurence(n, 3)):
            number_of_three_times_occurences += 1

    return number_of_two_times_occurences * number_of_three_times_occurences


def part_two(ids):
    '''
    Question:
            What letters are common between the two correct box IDs?
    Finds common letters by removing the different character from either ID,
    that differ by exactly one character(e.g., 'fghij' and 'fguij').
    '''

    def differ_by_one_letter(s1, s2):
        '''Compares two strings, returns True if they differ by 1 letter.'''
        alreadyDiffrent = False

        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if already_diffrent:
                    return False
                else:
                    already_diffrent = True

        return True

    def common_letters(s1, s2):
        '''
        Returns common letters between two strings by removing differing character from first string.
        Example:
            a = 'abcdef1g'
            b = 'abcdef2g'
            print(common_letters(a, b))
            'abcdefg'
        '''
        for index, (c1, c2) in enumerate(zip(s1, s2)):
            if c1 != c2:
                return s1[:index] + s1[index + 1:]

    for s1, s2 in itertools.combinations(ids, 2):
        are_different = differ_by_one_letter(s1, s2)
        if are_different:
            common_letters = common_letters(s1, s2)
            return common_letters


def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input'
    ids = [str(line) for line in input_file.open()]

    print(f'Part One: {part_one(ids)}')
    print(f'Part Two: {part_two(ids)}')


if __name__ == '__main__':
    main()
