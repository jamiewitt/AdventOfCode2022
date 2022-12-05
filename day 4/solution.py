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
        (one, two) = line.strip().split(',')
        r_one = set(range(int(one.split('-')[0]), int(one.split('-')[1])+1))
        r_two = set(range(int(two.split('-')[0]), int(two.split('-')[1])+1))
        if (r_one & r_two == r_one) or (r_one & r_two == r_two):
            total += 1

    print(total)

@profiler
def part2():
    print('Part 2')

    file1 = open('input.txt', 'r')

    lines = file1.readlines()

    total = 0

    for line in lines:
        (one, two) = line.strip().split(',')
        r_one = set(range(int(one.split('-')[0]), int(one.split('-')[1])+1))
        r_two = set(range(int(two.split('-')[0]), int(two.split('-')[1])+1))
        if (r_one & r_two):
            total += 1
            
    print(total)


if __name__ == "__main__":
    part1()
    part2()