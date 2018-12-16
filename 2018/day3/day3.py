"""Solution to Advent of Code 2018, Day 3: No Matter How You Slice It (https://adventofcode.com/2018/day/1)."""
import pathlib
import numpy


def lineToIdPositionAndSize(line):
    '''
    Returns a dictionnary specifying the id, position and size of the claim
    '''
    id = line.split(' @ ')[0][1:]
    x = line.split(' @ ')[1].split(': ')[0].split(',')[0]
    y = line.split(' @ ')[1].split(': ')[0].split(',')[1]
    width = line.split(' @ ')[1].split(': ')[1].split('x')[0]
    height = line.split(' @ ')[1].split(': ')[1].split('x')[1].split('\n')[0]

    return {'id': id, 'x': int(x), 'y': int(y), 'width': int(width), 'height': int(height)}


def part_one(lines):
    '''
    Question:
        How many square inches of fabric are within two or more claims?

    Build a 1000x1000 array, write the claims in it and count when it is > 1
    '''

    claims = [[0 for x in range(1000)] for y in range(1000)]

    for line in lines:
        decodedLine = lineToIdPositionAndSize(line)
        x = decodedLine.get('x')
        y = decodedLine.get('y')
        width = decodedLine.get('width')
        height = decodedLine.get('height')

        for i in range(x, x + width):
            for j in range(y, y + height):
                claims[i][j] += 1

    tooClaimed = 0
    for i in range(1000):
        for j in range(1000):
            if(claims[i][j] > 1):
                tooClaimed += 1

    return tooClaimed


def checkOnlyOneClaim(claims, x, y, width, height):
    for i in range(x, x + width):
        for j in range(y, y + height):
            if(claims[i][j] > 1):
                return False

    return True


def part_two(lines):
    '''
    Question:
        What is the ID of the only claim that doesn't overlap?

    Build a 1000x1000 array, write the claims in it.
    Then for every ID, check the one that has no "2 or more" in the grid
    '''

    claims = [[0 for x in range(1000)] for y in range(1000)]

    for line in lines:
        decodedLine = lineToIdPositionAndSize(line)
        x = decodedLine.get('x')
        y = decodedLine.get('y')
        width = decodedLine.get('width')
        height = decodedLine.get('height')

        for i in range(x, x + width):
            for j in range(y, y + height):
                claims[i][j] += 1

    for line in lines:
        decodedLine = lineToIdPositionAndSize(line)
        x = decodedLine.get('x')
        y = decodedLine.get('y')
        width = decodedLine.get('width')
        height = decodedLine.get('height')

        if(checkOnlyOneClaim(claims, x, y, width, height)):
            return decodedLine.get('id')


def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input'
    lines = [str(line) for line in input_file.open()]

    print(f'Part One: {part_one(lines)}')
    print(f'Part Two: {part_two(lines)}')


if __name__ == '__main__':
    main()
