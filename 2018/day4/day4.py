"""Solution to Advent of Code 2018, Day 3: No Matter How You Slice It (https://adventofcode.com/2018/day/1)."""
import pathlib
import numpy
import datetime


def sortLinesByTime(lines):
    return sorted(lines, key=lambda x: datetime.datetime.strptime(x.split(']')[0][1:], '%Y-%m-%d %H:%M'))


def isANewShift(line):
    return line.split('] ')[1].split(' ')[0] == 'Guard'


def getGuardId(line):
    return int(line.split('] ')[1].split(' ')[1][1:])


def isAsleep(line):
    return line.split('] ')[1] == 'falls asleep\n'


def getMinute(line):
    return int(line.split(']')[0].split(':')[1])


def part_one(lines):
    '''
    Question:
        What is the ID of the guard you chose multiplied by the minute you chose?

    Sort the data by time, find the guard that has the most minutes asleep and
    then find on which minute does that guard spend asleep the most
    '''

    sortedLines = sortLinesByTime(lines)

    # Not optimal storage at all
    sleepingTimes = [0 for x in range(4000)]
    sleepingMinutes = [[0 for x in range(60)] for y in range(4000)]

    for line in sortedLines:
        if(isANewShift(line)):
            id = getGuardId(line)
        elif(isAsleep(line)):
            minuteAsleep = getMinute(line)
        else:
            minuteUp = getMinute(line)
            sleepingTimes[id] += minuteUp - minuteAsleep
            for minute in range(minuteAsleep, minuteUp):
                sleepingMinutes[id][minute] += 1

    sleepyGuardId = sleepingTimes.index(max(sleepingTimes))
    sleepyGuardMinute = sleepingMinutes[sleepyGuardId].index(
        max(sleepingMinutes[sleepyGuardId]))

    return sleepyGuardId * sleepyGuardMinute


def part_one(lines):
    '''
    Question:
        What is the ID of the guard you chose multiplied by the minute you chose?

    Sort the data by time, build a big array [minutes * ids] where we store
    occurences and BAM
    '''

    sortedLines = sortLinesByTime(lines)

    # Not optimal storage at all
    sleepingLog = [[0 for x in range(60)] for y in range(4000)]

    for line in sortedLines:
        if(isANewShift(line)):
            id = getGuardId(line)
        elif(isAsleep(line)):
            minuteAsleep = getMinute(line)
        else:
            minuteUp = getMinute(line)
            for minute in range(minuteAsleep, minuteUp):
                sleepingLog[id][minute] += 1


    maxOccurence = max(max(x) for x in sleepingLog)

    # It is veeeeeery likely that a smarter way exists to do this haha
    for i in range(4000):
        for j in range(60):
            if(sleepingLog[i][j] == maxOccurence):
                sleepyGuardId = i
                sleepyGuardMinute = j

    return sleepyGuardId * sleepyGuardMinute



def main():

    input_file = pathlib.Path(__file__).resolve().parent / 'input'
    lines = [str(line) for line in input_file.open()]

    print(f'Part One: {part_one(lines)}')


if __name__ == '__main__':
    main()
