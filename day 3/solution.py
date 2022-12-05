import sys
sys.path.append( '../' )

from utils import profiler

@profiler
def part1():
    print('Part 1')

    file1 = open('input.txt', 'r')

    lines = file1.readlines()

    total = 0

    for line in lines:
        compartment_one = line.strip()[0:len(line.strip())//2]
        compartment_two = line.strip()[len(line.strip())//2:]
        result = list(set(compartment_one) & set(compartment_two))
        score = ((ord(result[0])-64)%32) + (int(not((ord(result[0])-64)//32)) * 26)
        total += score

    print(total)

@profiler
def part2():
    print('Part 2')

    file1 = open('input.txt', 'r')

    lines = file1.readlines()

    total = 0
    sacks = []

    for line in lines:
        sacks.append(line.strip())
        if len(sacks) == 3:
            result = list(set(sacks[0]) & set(sacks[1]) & set(sacks[2]))
            sacks = []
            score = ((ord(result[0])-64)%32) + (int(not((ord(result[0])-64)//32)) * 26)
            total += score

    print(total)

if __name__ == "__main__":
    part1()
    part2()