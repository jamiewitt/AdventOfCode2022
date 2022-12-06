import sys
sys.path.append( '../' )

from utils import profiler
from collections import defaultdict

@profiler
def part1():
    print('Part 1')

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    result = 0

    line = lines[0].strip()

    for i in range(3, len(line)):
        buffer = line[i-3:i+1]
        if len(set(buffer)) == 4:
            result = i+1
            break

    print(result)

@profiler
def part2():
    print('Part 2')

    file1 = open('input.txt', 'r')
    lines = file1.readlines()

    result = 0

    line = lines[0].strip()

    for i in range(13, len(line)):
        buffer = line[i-13:i+1]
        if len(set(buffer)) == 14:
            result = i+1
            break

    print(result)

if __name__ == "__main__":
    part1()
    part2()